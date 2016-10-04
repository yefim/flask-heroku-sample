import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
  return "Hello"


@app.route('foo')
def foo():
  return 'barbar'


@app.route('/yay')
def yay():
  return "Nope."
