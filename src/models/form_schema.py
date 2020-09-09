from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from src.server import db

class Schema(UserMixin, db.Model):
    __tablename__ = 'schema'

    id = db.Column(db.Integer,
                   primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    