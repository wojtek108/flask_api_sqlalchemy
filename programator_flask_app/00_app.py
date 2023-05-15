from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from flask!'

@app.route('/czesc')
@app.route('/czesc/<imie>')
def czesc(imie=None):
    return f"""


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Czesc from flask app!</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
	<h1>Hello from simple flask app!</h1>
	<h1>Hello from user {imie}!</h1>
  </body>
</html>

    """
@app.route('/hej/<imie>')
def powitanie(imie):
    return f'Czesc, {imie}'

@app.route('/users/<int:id>')
def info_user(id):
    return f'Dane uzytkownika o id: {id}'
