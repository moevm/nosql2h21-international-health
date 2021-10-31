import os
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()


def get_mongo_client():
    mongo_user = os.environ.get('MONGO_INITDB_ROOT_USERNAME')
    mongo_password = os.environ.get('MONGO_INITDB_ROOT_PASSWORD')

    assert mongo_user is not None
    assert mongo_password is not None

    mongo_host = os.environ.get('MONGO_HOST', '5.23.49.205')
    mongo_port = os.environ.get('MONGO_PORT', 27017)
    mongo_url = f'mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}'
    return MongoClient(mongo_url)
