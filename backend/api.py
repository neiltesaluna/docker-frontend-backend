# Product Service
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        return 'Welcome to Home Base'

class Products(Resource):
    def get(self):
        return {
            'products': ['Ice cream',
                        'Chocolate',
                        'Fruit']
        }

api.add_resource(Home, '/')
api.add_resource(Products, '/products')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
