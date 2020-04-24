import os
import hashlib
import hmac
import base64

from models.user import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username)

    secret = bytes(os.environ.get('SECRET_KEY'), 'utf-8')
    user_bytes = bytes(username, 'utf-8')

    pass_signature = hmac.new(secret, user_bytes, digestmod=hashlib.sha256).hexdigest()

    if hmac.compare_digest(password, pass_signature):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)