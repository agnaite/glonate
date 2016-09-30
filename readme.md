# glonate [![Build Status](https://travis-ci.org/agnaite/glonate.svg?branch=master)](https://travis-ci.org/agnaite/glonate)


## Setup

```bash
virtualenv env
source venv/bin/activate

pip install -r requirements.txt

# creates my_database.db with seed data
# you might need to rm my_database.db if it already exists
python setupdb.py

# start the app
python server.py

# visit http://localhost:5000
```
