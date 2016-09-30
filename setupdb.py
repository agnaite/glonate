# run database migrations and what-not

from environment import *
import os
import psycopg2
import urlparse

print(db)

db.connect()
db.create_tables([User, Message])

# urlparse.uses_netloc.append("postgres")
# url = urlparse.urlparse(os.environ["DATABASE_URL"])

# conn = psycopg2.connect(
#     database=url.path[1:],
#     user=url.username,
#     password=url.password,
#     host=url.hostname,
#     port=url.port
# )

# some seeds go here

user = User.create(email='user@example.com')
messenger = User.create(email='messenger@example.com')

Message.create(user=user, body='human needs money')
Message.create(user=messenger, body='human gives money')
Message.create(user=user, body='human says ty')
