from peewee import SqliteDatabase

from schemas.card import Card
from schemas.ticket import Retirar
from schemas.user import User

db_card = SqliteDatabase('card.db')
db_card.create_tables([User,Card,Retirar])
