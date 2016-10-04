import os

from flask import Flask

app = Flask(__name__)

@app.route('/costam')
def costam():
  return "costam"

@app.route('nowa_metoda')
def nowa_metoda():
	return 'void'

@app.route('/')
def hello():
  return "Hello"

@app.route('foo')
def foo():
  c+_)(*&
  return 'barbar'


@app.route('/yay')
def yay():
  return "Nope."

@app.route('/doit')
  return 'just DO IT!'

def nieznampytona():
  return "nie znam pythona"

x = 100;
