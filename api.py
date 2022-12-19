from flask import Flask
from flask_restful import Api
from logics.operation import *
from resources.helloworld import *
from resources.operation import *
from resources.selfdata import *

app = Flask(__name__)
api = Api(app)


api.add_resource(HelloWorld, '/hello')
api.add_resource(OperationMath, '/operation')
api.add_resource(SelfData, '/info/<id>')

if __name__ == '__main__':
    app.run(debug=True)



# basic structure
# from flask import Flask
# from flask_restful import Resource, Api

# app = Flask(__name__)
# api = Api(app)

# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}

# api.add_resource(HelloWorld, '/')

# if __name__ == '__main__':
#     app.run(debug=True)