from pymongo import MongoClient, ASCENDING, DESCENDING
from backend.settings import MONGODB_USER, MONGODB_PASSWORD, MONGODB_HOST, MONGODB_PORT, DB_NAME


def get_mongo_client() -> MongoClient:
    mongo_url = f'mongodb://{MONGODB_USER}:{MONGODB_PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}'
    return MongoClient(mongo_url)


async def get_direction(ascending: bool) -> int:
    return ASCENDING if ascending else DESCENDING
