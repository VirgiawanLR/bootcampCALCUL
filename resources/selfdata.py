from flask_restful import Resource, reqparse

class SelfData(Resource):
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, location='args')
        parser.add_argument('password', type=str, location='args')
        parser.add_argument('age', type=int)
        parser.add_argument('address', type=dict, action='append')
        parser_args = parser.parse_args()

        address_nested = reqparse.RequestParser()
        address_nested.add_argument('city', type=str, location=('address'))
        address_nested.add_argument('province', type=str, location=('address'))
        # address_arg = address_nested.parse_args(req=parser_args)
        # print(address_arg)

        try:
            id = int(id)
        except:
            return {"messages": "invalid path"}, 400
            
        parser_args['id'] = id
        return parser_args, 200
