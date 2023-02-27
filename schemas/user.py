from peewee import *

db = SqliteDatabase('prueba_union.db')


class User(Model):
    names = CharField()
    first_name = CharField()
    second_name = CharField()
    phone_number = CharField()
    email = CharField()
    #Bday = DateField()
    adress = CharField()
    ExternNumber = IntegerField()

    class Meta:
        database = db  # This model uses the "movies.db" database.
