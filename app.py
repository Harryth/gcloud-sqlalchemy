import os
import datetime
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

# Importing endpoint resources
from resources.user import User
# Importing security handler for JWT auth
from security import authenticate, identity

# Create an instance of the Flask and Flask-RESTful API
app = Flask(__name__)
api = Api(app)
# Configuration of the app variables
app.config.update(
    SECRET_KEY=os.urandom(24), # Setting the JWT secret as a random string
    JWT_EXPIRATION_DELTA=datetime.timedelta(seconds=7200), # Set JWT 'exp' as 2h
    SQLALCHEMY_DATABASE_URI=os.environ.get('DB_PATH') # Get DB path from env variable
    #SQLALCHEMY_DATABASE_URI='mysql+pymysql://user:MicroREC@/testdb?unix_socket=/cloudsql/app-sql-275122:us-east1:test-db'
)

print(os.environ.get('DB_PATH'))
print(os.environ.get('SECRET_KEY'))

# Seting the JWT authentication process at {url}/auth
jwt = JWT(app, authenticate, identity)

# Connect Resource with Endpoint
api.add_resource(User, '/register')

# Running app only if is called from app entrypoint
## Getting port from OS or using default 5000
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True, host='127.0.0.1',port=int(os.environ.get('PORT', 5000)))