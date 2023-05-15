from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy as sq

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '123456!#'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'


db = sq(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    location = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.now)

with app.app_context():
    db.create_all()

@app.route('/<name>/<location>')
def index(name, location):
    user = User(name=name, location=location)
    db.session.add(user)
    db.session.commit()
    return '<h1>Added new user</h1>'

#@app.route('/<name>')
#def get_user(name):
#    user = User.query.filter_by(name=name).all()
#    return f'The user is located in { user.location }'

    
@app.route('/<name>')
def get_user(name):
    user = User.query.filter_by(name=name).first()
    return f'<h1>The user is located in: { user.location }</h1>'
