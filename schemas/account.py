from peewee import *

from schemas.user import User

db = SqliteDatabase('card.db')


class Account(Model):
    user = ForeignKeyField(User, backref="accounts")
    card = CharField()
    type = CharField()

    class Meta:
        database = db  # This model uses the "card.db" database.