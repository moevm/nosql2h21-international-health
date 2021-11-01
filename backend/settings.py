from os import getenv

from dotenv import load_dotenv


load_dotenv()

MONGODB_USER = getenv('MONGODB_USER')
MONGODB_PASSWORD = getenv('MONGODB_PASSWORD')
BACKEND_PORT = int(getenv('BACKEND_PORT'))
MONGODB_PORT = int(getenv('MONGODB_PORT'))
BACKEND_HOST = getenv('BACKEND_HOST')
MONGODB_HOST = getenv('MONGODB_HOST')
DB_NAME = getenv('DB_NAME')
