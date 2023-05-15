from flask import render_template, request, Flask
from flask_sqlalchemy import SQLAlchemy as sq

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456!#'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks_backup.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = sq(app)

class Database(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String)

with app.app_context():
    db.create_all()

def add_task(task):
    task = request.form.get(task)
    Data = Database(Name = task)
    db.session.add(Data)
    db.session.commit()
    query = Database.query.all()
    return query


@app.route('/', methods =['POST', 'GET'])
def index():
    if (request.method == 'POST'):
        N = add_task('task_frontend')
        for i in N:
            return render_template('todo.html', n=N)
    return render_template('todo.html')


if __name__ == '__main__':
    app.run(debug=True)

