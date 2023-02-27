from peewee import *

from schemas.user import User
from schemas.card import Card

db = SqliteDatabase('card.db')


class Retirar(Model):

    amount_to_get = IntegerField()
    initial_amount = IntegerField()


    class Meta:
        database = db
