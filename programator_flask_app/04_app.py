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

@app.route('/', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        task = Task(name=request.form['task_frontend'])
        db.session.add(task)
        db.session.commit()
    tasks = Task.query.all()
    return render_template('todo.html', tasks=tasks)

@app.route('/hello')
def hello():
    return render_template('glowna.html')



#from flask import render_template, request, url_for, Flask
#from flask_sqlalchemy import SQLAlchemy as sq
#
#app = Flask(__name__)
#app.config['SECRET_KEY'] = '123456!#'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
#db = sq(app)
#
#class Database(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    Name = db.Column(db.String)
#
#with app.app_context():
#    db.create_all()
#
#def add_data(name):
#    name = request.form.get(name)
#    Data = Database(Name = name)
#    db.session.add(Data)
#    db.session.commit()
#    query = Database.query.all()
#    return query
#
#
#@app.route('/', methods =['POST', 'GET'])
#def index():
#    if (request.method == 'POST'):
#        N = add_data('Fname')
#        for i in N:
#            return render_template('index.html', n=N)
#    return render_template('index.html')
#
#
#if __name__ == '__main__':
#    app.run(debug=True)
#
