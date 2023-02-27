from peewee import SqliteDatabase

from schemas.card import Card
from schemas.ticket import Ticket
from schemas.user import User

db = SqliteDatabase('prueba_union.db')
db.create_tables([User, Card, Ticket])