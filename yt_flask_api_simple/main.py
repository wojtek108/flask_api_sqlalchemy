from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)

names = {
        'tim': {'age': 100, 'mood': 'great'},
        'bill': {'age': 10, 'mood': 'depressed'},
        'phil': {'age': 50, 'mood': 'extatic'}
        }


class HelloWorld(Resource):
    def get(self, name):
        #return {'data': 'Hello, world!'}
        #return {'data': name}
        if name in names:
            return names[name]
        else:
            return 'No such name'

    def post(self, name):
        #return {'data': 'posted'}
        return {'data': name}

class Data(Resource):
    def get(self):
        return names


api.add_resource(HelloWorld, '/data/<string:name>')
api.add_resource(Data, '/data/')

if __name__ == '__main__':
    app.run(debug=True)

