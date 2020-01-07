import os

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)

DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:////tmp/flask_application.db')

application.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(application)


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  email = db.Column(db.String(100))

  def __init__(self, name, email):
    self.name = name
    self.email = email


@application.route('/', methods=['GET'])
def index():
  return render_template('index.html', users=User.query.all())


@application.route('/user', methods=['POST'])
def user():
  u = User(request.form['name'], request.form['email'])
  db.session.add(u)
  db.session.commit()
  return redirect(url_for('index'))

if __name__ == '__main__':
  db.create_all()
  port = int(os.environ.get('PORT', 5000))
  application.run(host='0.0.0.0', port=port, debug=True)
