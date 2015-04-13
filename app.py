import os

from flask import Flask, render_template, request, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy

username = os.environ.get('PG_USER')
password = os.environ.get('PG_PASSWORD')
dbhost = os.environ.get('PG_HOST')
dbport = os.environ.get('PG_PORT')
db = os.environ.get('PG_DATABASE')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://'+username+':'+password+'@'+dbhost+':'+dbport+'/'+db
db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  email = db.Column(db.String(100))
  def __init__(self, name, email):
    self.name = name
    self.email = email

@app.route('/')
def index():
  return render_template('index.html', users = User.query.all())

@app.route('/user', methods=['POST'])
def user():
  if request.method == 'POST':
    u = User(request.form['name'], request.form['email'])
    db.session.add(u)
    db.session.commit()
  return redirect(url_for('index'))

if __name__ == '__main__':
  db.create_all()
  port = int(os.environ.get('PORT',5000))
  app.run(host='0.0.0.0', port=port)
