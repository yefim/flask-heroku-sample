Flask Heroku Sample
====================

## Steps

* Create Procfile with `web: gunicorn -b 0.0.0.0:$PORT app:app`

* Run `virtualenv venv`

* Run `source venv/bin/activate`

* Run `pip install flask` (no sudo needed)

* Run `pip install gunicorn`

* Run `pip install flask-sqlalchemy`

* Run `pip freeze > requirements.txt`

* Add `psycopg2` to the end of requirements.txt

* Run `heroku create`

* Run `heroku addons:create heroku-postgresql:hobby-dev`

* Run `git push heroku master`
