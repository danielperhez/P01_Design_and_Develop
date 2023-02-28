from peewee import *

db = SqliteDatabase('card.db')


class User(Model):
    names = CharField()
    first_name = CharField()
    second_name = CharField()
    phone_number = CharField()
    email = CharField()
    address = CharField()
    extern_number = IntegerField()

    class Meta:
        database = db  # This model uses the "card.db" database.
