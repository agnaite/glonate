# run database migrations and what-not

from environment import *

print(db)

db.connect()
db.create_tables([User, Message])

# some seeds go here

user = User.create(email='test@example.com')
print(user)

message = Message.create(user=user, body='human gives money. human receives money. human glonates')

print(message)
