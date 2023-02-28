from peewee import *

db = SqliteDatabase('card.db')


class User(Model):
    name = CharField()
    phone_number = CharField()
    email = CharField()
    address = CharField()
    password = CharField()

    class Meta:
        database = db  # This model uses the "card.db" database.
