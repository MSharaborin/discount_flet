import peewee

from connection import db
from models import Discount


def create(
        number: int,
        fullname: str,
        phone: str,
        total_price: float,
        discount: str,
        is_notify: bool) -> bool:
    with db:
        request = Discount(
            number=number,
            fullname=fullname,
            phone=phone,
            total_price=total_price,
            discount=discount,
            is_blocked=False,
            is_notify=is_notify
        )
        request.save()
    return True


