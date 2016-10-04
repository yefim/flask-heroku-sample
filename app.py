import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
  return "Hello"

@app.route('/costam')
def costam():
  return "costam"

@app.route('/yay')
def yay():
  return "Nope."
