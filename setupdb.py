# run database migrations and what-not

from environment import *

print(db)

db.connect()
db.create_tables([User, Message])

# some seeds go here

user = User.create(email='user@example.com')
messenger = User.create(email='messenger@example.com')

Message.create(user=user, body='human needs money')
Message.create(user=messenger, body='human gives money')
Message.create(user=user, body='human says ty')

print(message)
