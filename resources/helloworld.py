from flask_restful import Resource

class HelloWorld(Resource):
    def get(self):
        return {
            'name': 'Virgiawan',
            'address': 'garut',
            'age': 27
        }

    def post(self):
        return {
            'number': [1,2,3,4,5,6,7,8]
        }