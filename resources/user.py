from flask_restful import Resource, reqparse

from models.user import UserModel

# Create a new resource that will handle petitions (on /hello/ endpoint)
class User(Resource):

    # Checking data sent on body
    ## Must receive and required argument called name type string (default)
    ## If no value will response with help
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        required=True,
        help='This field cannot be blank.')
    parser.add_argument('first_name',
        required=True,
        help='This field cannot be blank.')
    parser.add_argument('last_name',
        required=True,
        help='This field cannot be blank.')
    parser.add_argument('role',
        required=True,
        help='This field cannot be blank.')

    # Methog that will handle petition over POST 
    @classmethod
    def post(cls):

        # Reading data from petition body
        data = cls.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'User already exist'}, 400

        user = UserModel(**data)

        user.save_to_db()

        # Returning a message: Hello {name}!
        return {'message': 'User {} created successfuly.'.format(data['username'])}, 201
