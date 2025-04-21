from sqlalchemy import create_engine
from config.config import DB_CONFIG

def get_engine():
    user = DB_CONFIG['user']
    password = DB_CONFIG['password']
    host = DB_CONFIG['host']
    port = DB_CONFIG['port']
    dbname = DB_CONFIG['dbname']

    return create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')
