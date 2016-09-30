import os
import datetime
from peewee import *
import urlparse
from playhouse.sqlite_ext import SqliteExtDatabase

db_proxy = Proxy()

if 'HEROKU' in os.environ:
    urlparse.uses_netloc.append('postgres')
    url = urlparse.urlparse(os.environ['DATABASE_URL'])
    DATABASE = {
        'engine': 'peewee.PostgresqlDatabase',
        'name': url.path[1:],
        'user': url.username,
        'password': url.password,
        'host': url.hostname,
        'port': url.port,
    }
else:
    DATABASE = 'glonate_development'

db = PostgresqlDatabase(DATABASE)
db_proxy.initialize(db)

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
