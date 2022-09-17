import flet
import peewee
from flet import ElevatedButton, Page, TextField, Checkbox, Text, colors, Column, Container, theme
from loguru import logger

from crud_utils import create


def main(page: Page):
    page.title = "Discount table"
    page.vertical_alignment = "center"

    number = TextField(
        text_align="right",
        expand=True,
        label='Номер',
    )
    fullname = TextField(
        text_align="right",
        expand=True,
        label='ФИО'
    )
    phone = TextField(text_align="right", expand=True, label='Номер телефона')
    total_price = TextField(text_align="right", expand=True, label='Сумма')
    discount = TextField(text_align="right", expand=True, label='Скидка')
    is_notify = Checkbox(value=True, expand=True, label='Включать уведомления')
    error_message = Text(color=colors.RED_200, size=20)

    def add_customer(e):
        try:
            create(
                number.value,
                fullname.value,
                phone.value,
                total_price.value,
                discount.value + '%',
                is_notify.value
            )
            logger.info(f'Create number {number.value}, {fullname}.')
        except peewee.IntegrityError as error:
            error_message.value = error
        number.value, fullname.value, phone.value, total_price.value, discount.value = '', '', '', '', ''
        page.update()

    page.add(
        Column(
            [
                Container(number),
                Container(fullname),
                Container(phone),
                Container(total_price),
                Container(discount),
                Container(is_notify),
                Container(ElevatedButton('Добавить', on_click=add_customer)),
                Container(error_message),
            ]
        ),
    )


flet.app(target=main, port=6060, )
