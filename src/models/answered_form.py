from src.server import db

class Answered(db.Model):
    __tablename__ = 'answered'

    id = db.Column(db.Integer,
                   primary_key=True)

    user_id = db.Column(db.Integer,
                    db.ForeignKey('user.id'))

    schema_id = db.Column(db.Integer,
                    db.ForeignKey('schema.id'))
    
    posted = db.Column(db.DateTime)

    form = db.Column(db.JSON)

    