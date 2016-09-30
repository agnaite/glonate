import os
import datetime
from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

DATABASE_URL = os.getenv('DATABASE_URL') or 'glonate_development'

db = PostgresqlDatabase(DATABASE_URL)

class BaseModel(Model):
    ''' basic peewee setup '''
    class Meta:
        database = db

class User(BaseModel):
    email = CharField(unique=True)

class Message(BaseModel):
    user = ForeignKeyField(User, related_name='messages')
    body = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
