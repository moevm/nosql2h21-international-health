from csv import DictReader
from datetime import datetime
from os import listdir

from backend.helper import get_batch, get_mongo_client, to_mongo

if __name__ == '__main__':
    client = get_mongo_client()
    source_dir_path = './source'

    for file in listdir(source_dir_path):
        if not file.endswith('.csv'):
            continue
        with open(f'{source_dir_path}/{file}', newline='', encoding='utf-8-sig') as csvfile:
            reader = DictReader(csvfile)
            for batch in get_batch(reader):
                to_mongo(client, file.replace('.csv', ''), batch)
                print(f'{datetime.utcnow()}: insert {len(batch)} notes of {file} collection')
