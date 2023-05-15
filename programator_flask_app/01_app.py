from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('glowna.html')

@app.route('/czesc')
@app.route('/czesc/<imie>')
def czesc(imie=None):
    return render_template('czesc.html', imie=imie)
    

@app.route('/users/<int:id>')
def info_user(id):
    return f'Dane uzytkownika o id: {id}'

@app.route('/todo', methods=['GET', 'POST'])
def todo():
    tasks =['task 1', 'task 2']
    return render_template('todo.html', tasks=tasks)
