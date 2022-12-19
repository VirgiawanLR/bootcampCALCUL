from logics.operation import *
from flask_restful import Resource, reqparse

class OperationMath(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('num1', type=int, location='args')
        parser.add_argument('num2', type=int, location='args')
        parser.add_argument('oper', type=int, location='args')
        x = parser.parse_args()

        operType = x['oper']

        num1 = x['num1']
        num2 = x['num2']

        if operType == 1:
            result = add(num1, num2)
        elif operType == 2:
            result = subs(num1, num2)
        elif operType == 3:
            result = multiply(num1, num2)
        elif operType == 4:
            result = div(num1, num2)
        else:
             return {
                'result':'invalid Operation'
            }, 400



        return {
            'result': result
        }, 200
