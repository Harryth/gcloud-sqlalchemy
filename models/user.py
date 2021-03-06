from db import db # Importing SQLAlchemy object

class UserModel(db.Model):

    # Creation of a new DB table using SQLAlchemy interface
    __tablename__ = 'users'

    # Identification of the table columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45))
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    role = db.Column(db.String(45))

    # user constructor
    def __init__(self, username, first_name, last_name, role):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
    
    # Method to save user into DB
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # Method to find user in the DB search by username
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    # Method to find user in the DB search by ID
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()