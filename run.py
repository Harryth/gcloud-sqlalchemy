from app import app
from db import db

# Init the DB
db.init_app(app)

# ASLAlchemy will create the DB tables before the first request
@app.before_first_request
def create_tables():
    db.create_all()