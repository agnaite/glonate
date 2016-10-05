# glonate [![Build Status](https://travis-ci.org/agnaite/glonate.svg?branch=master)](https://travis-ci.org/agnaite/glonate)


## Setup

```bash
virtualenv env
source env/bin/activate

pip install -r requirements.txt

# create postgres database
createdb glonate

# migrate & seed database
python model.py

# start the app
python server.py

# visit http://localhost:5000
```
