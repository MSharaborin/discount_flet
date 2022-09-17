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


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'


class Discount(BaseModel):
    number = IntegerField()
    fullname = CharField()
    phone = CharField()
    total_price = CharField()
    discount = CharField()

    class Meta:
        db_table = 'discount'


if __name__ == '__main__':
    db.connect()
    db.create_tables([Discount])
    print('DONE')

