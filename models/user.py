from db import db

class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45))
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    role = db.Column(db.String(45))

    def __init__(self, username, first_name, last_name, role):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()