from peewee import *

from schemas.user import User
from schemas.card import Card

db = SqliteDatabase('card.db')


class Retirar(Model):

    user = ForeignKeyField(User, backref='tickets')
    card = ForeignKeyField(Card, backref='tickets')
    balance = IntegerField()
    cut = register_date = DateTimeField()
    type = CharField()

    class Meta:
        database = db
