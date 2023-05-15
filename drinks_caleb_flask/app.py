from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy as sq

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456!#'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drinks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = sq(app)


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f'{self.name} - {self.description}'

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return 'Hello!'

@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    output = []
    for drink in drinks:
        drink_data = {'name': drink.name, 'description': drink.description}
        output.append(drink_data)
    return {'drinks': output}

@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {"name": drink.name, "description": drink.description}

@app.route('/drinks', methods =['POST'])
def add_drink():
    drink = Drink(name=request.json['name'], description = request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id': drink.id}

@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {"error": "not found"}
    db.session.delete(drink)
    db.session.commit()
    return {"message": "yeet!@"}

if __name__ == '__main__':
    app.run(debug=True)
