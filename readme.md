Flask Heroku Sample
====================

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Development Setup

* `virtualenv venv`

* `source venv/bin/activate`

* `pip install -r requirements.txt`

## Deploy

* `heroku create`

* `heroku addons:create heroku-postgresql:hobby-dev`

* `git push heroku master`

* `heroku run python`

* `> from app import db`

* `> db.create_all()`

## Contributors

* [Yefim](https://twitter.com/yefim)
