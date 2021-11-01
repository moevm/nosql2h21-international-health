from csv import DictReader
from datetime import datetime
from os import listdir

from pymongo import MongoClient

from backend.helper import get_mongo_client
from backend.settings import DB_NAME


def to_mongo(client: MongoClient, db_name: str, collection_name: str, notes: list[dict]):
    collection_name = collection_name.replace('.csv', '')
    db = client[db_name][collection_name]
    db.insert_many(notes)


def get_notes(reader: DictReader):
    result = []
    for line in reader:
        for key, value in line.items():
            try:
                line[key] = int(value)
            except ValueError:
                try:
                    line[key] = float(value)
                except ValueError:
                    pass

        result.append(line)
        if len(result) % 30000 == 0:
            yield result
            result.clear()
    yield result


if __name__ == '__main__':
    client = get_mongo_client()
    source_dir_path = './source'

    for file in listdir(source_dir_path):
        if not file.endswith('.csv'):
            continue
        with open(f'{source_dir_path}/{file}', newline='', encoding='utf-8-sig') as csvfile:
            reader = DictReader(csvfile)
            for batch in get_notes(reader):
                to_mongo(client, DB_NAME, file, batch)
                print(f'{datetime.utcnow()}: insert {len(batch)} notes of {file} collection')
