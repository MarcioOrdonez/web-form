from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from src.server import db

class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer,
                   primary_key=True)

    email = db.Column(db.String(80),
                      index=True,
                      unique=False,
                      nullable=False)
    
    password = db.Column(db.String(200),
                         primary_key=False,
                         unique=False,
                         nullable=False)


