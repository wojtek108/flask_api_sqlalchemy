from flask import render_template, request, Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy as sq

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456!#'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks_backup.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = sq(app)

class Database(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    
    def to_dict(self):
        return {'id': self.id, 'name': self.name}


with app.app_context():
    db.create_all()

def add_task(task):
    task = request.form.get(task)
    data = Database(name = task)
    db.session.add(data)
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


@app.route('/api/task', methods=['GET'])
def list_tasks():
    tasks = Database.query.all()
    tasks_data = [task.to_dict() for task in tasks]
    return jsonify(tasks_data)


@app.route('/api/task', methods=['POST'])
def create_task():
    task_name = request.json['name']
    task = Database(name = task_name)
    db.session.add(task)
    db.session.commit()
    response_data = jsonify(task.to_dict())
    return make_response(response_data, 201)


@app.route('/api/task/<int:task_id>', methods=['GET'])
def task_details(task_id):
    task = Database.query.get(task_id)
    if task is None:
        return make_response(' ', 404)
    else:
        return jsonify(task.to_dict())


@app.route('/api/task/<int:task_id>', methods=['PUT'])
def modify_task(task_id):
    task = Database.query.get_or_404(task_id)
    task.name = request.json["name"]
    db.session.commit()
    return jsonify(task.to_dict())

@app.route('/api/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Database.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return make_response('', 204)




if __name__ == '__main__':
    app.run(debug=True)

