import os
import hashlib
import hmac
import base64

# Importing the User model DB functions
from models.user import UserModel

# JWT function callback passed to the JWT constructor on app.py
def authenticate(username, password):
    user = UserModel.find_by_username(username) # Finds the user in the DB

    secret = bytes(str(os.environ.get('SECRET_KEY')), 'utf-8') # Loads secret from enviroment variable
    user_bytes = bytes(username, 'utf-8') # Converts the username in a bytes array compatible with the hmac funtion

    pass_signature = hmac.new(secret, user_bytes, digestmod=hashlib.sha256).hexdigest() #Sign the username + secret and return a hex string

    if hmac.compare_digest(password, pass_signature): # Compares password with calculated signature if True returns the user
        return user

# identity function passed to the JWT callback constructor
def identity(payload):
    user_id = payload['identity'] # Extracts the user ID from the JWT payload
    return UserModel.find_by_id(user_id) # Finds the user from his ID in the DB