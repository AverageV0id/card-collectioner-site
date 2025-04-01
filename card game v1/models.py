from peewee import *
import pytz
from datetime import datetime

db = SqliteDatabase('card_list.db')


class User(Model):
    username = CharField(unique=True)
    date_register = DateField()
    is_Admin = BooleanField(default=0)

    class Meta:
        database = db


class Card(Model):
    name = CharField(unique=True)
    price = CharField(null=True)
    rarity = CharField(null=True)
    date_obtained = DateTimeField(default=datetime.now(pytz.timezone('Europe/Moscow')))
    is_obtainable = BooleanField(default=1)

    class Meta:
        database = db


Card.create_table()
User.create_table()
