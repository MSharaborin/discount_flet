import datetime

from peewee import Model, PrimaryKeyField, IntegerField, CharField, BooleanField, DecimalField, DateTimeField, SQL
from loguru import logger

from connection import db


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'


class Discount(BaseModel):
    number = IntegerField(unique=True)
    fullname = CharField(unique=True)
    phone = CharField(unique=True)
    total_price = DecimalField(decimal_places=2)
    discount = CharField()
    is_blocked = BooleanField()
    is_notify = BooleanField()
    last_update = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])

    class Meta:
        db_table = 'discount'


if __name__ == '__main__':
    with db:
        db.create_tables([Discount])
        logger.debug('Create Database!')
