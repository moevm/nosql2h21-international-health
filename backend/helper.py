from csv import DictReader
from typing import Union
from fastapi.responses import FileResponse
import pandas as pd
from fastapi import HTTPException, status
from pymongo import ASCENDING, DESCENDING, MongoClient

from backend.settings import (DB_NAME, MONGODB_HOST, MONGODB_PASSWORD,
                              MONGODB_PORT, MONGODB_USER)


def get_mongo_client() -> MongoClient:
    mongo_url = f'mongodb://{MONGODB_USER}:{MONGODB_PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}'
    return MongoClient(mongo_url)


async def get_direction(ascending: bool) -> int:
    return ASCENDING if ascending else DESCENDING


def to_mongo(client: MongoClient, collection_name: str, notes: list[dict]):
    db = client[DB_NAME][collection_name]
    db.insert_many(notes)


def get_batch(reader: Union[DictReader, list[dict]], n: int = 40000):
    batch = []
    for line in reader:
        for key, value in line.items():
            try:
                line[key] = int(value)
            except ValueError:
                try:
                    line[key] = float(value)
                except ValueError:
                    pass

        batch.append(line)
        if len(batch) % n == 0:
            yield batch
            batch.clear()
    yield batch


async def import_file(file, mongo_client: MongoClient, collection: str):
    if mongo_client[DB_NAME][collection].count() != 0:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Collection already exists')
    content = await file.read()
    table_view = content.decode('utf-8-sig').split('\r\n')
    if len(table_view) < 2:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Empty csv file')
    data = [i.split(',') for i in table_view[1:]]
    columns = table_view[0].split(',')
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(f'./source/{collection}.csv')
    to_mongo_data = [vls for _, vls in df.iloc[:-1].to_dict('index').items()]
    for batch in get_batch(to_mongo_data, 30000):
        to_mongo(mongo_client, collection, batch)
    return {'success': True}


async def export_file(collection: str, mongo_client: MongoClient):
    if mongo_client[DB_NAME][collection].count() == 0:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Collection not exists')
    return FileResponse(f'./source/{collection}.csv', filename=f'{collection}.csv')
