from peewee import *
from psycopg2.extensions import ISOLATION_LEVEL_SERIALIZABLE


db = PostgresqlDatabase(
    'postgres',
    user='postgres',
    password='postgrespw',
    host='localhost',
    port=49153,
    isolation_level=ISOLATION_LEVEL_SERIALIZABLE
)
