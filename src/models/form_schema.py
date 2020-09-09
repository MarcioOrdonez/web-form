from src.server import db

class Schema(db.Model):
    __tablename__ = 'schema'

    id = db.Column(db.Integer,
                   primary_key=True)

    user_id = db.Column(db.Integer,
                    db.ForeignKey('user.id'))

    created = db.Column(db.DATE)
    
    schema = db.Column(db.JSON)