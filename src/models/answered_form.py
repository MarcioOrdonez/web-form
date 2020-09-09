from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from src.server import db

class Answered(UserMixin, db.Model):
    __tablename__ = 'Answered'

    id = db.Column(db.Integer,
                   primary_key=True)

    user_id = db.Column(db.Integer,
                    db.ForeignKey('user.id'))

    schema_id = db.Column(db.Integer,
                    db.ForeignKey('schema.id'))

    