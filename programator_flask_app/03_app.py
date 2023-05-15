from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SECRET_KEY'] = '123456!#'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
def add_task(task):
    task = request.form.get('task')
    new_task = Task(name=task)
    db.session.add(new_task)
    db.session.commit()

@app.route('/', methods=['GET', 'POST'])
def todo():
    #tasks = []
    #if request.method == 'POST':
        #tasks.append(request.form['task'])
    if (request.method == 'POST'):
        lista_todo = add_task('task')
        for task in lista_todo:
            return render_template('todo.html', tasks=tasks)
    return render_template('todo.html')
@app.route('/hello')
def hello():
    return render_template('glowna.html')
