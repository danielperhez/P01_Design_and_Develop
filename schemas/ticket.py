from peewee import *

from schemas.user import User
from schemas.card import Card

db = SqliteDatabase('card.db')


class Retirar(Model):

    user = ForeignKeyField(User, backref='tickets')
    card = ForeignKeyField(Card, backref='tickets')
    amount = IntegerField()

    class Meta:
        database = db
