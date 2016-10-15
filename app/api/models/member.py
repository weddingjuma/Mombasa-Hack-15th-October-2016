from app import db


class Member(db.Model):

    __tablename__ = 'members'
    
    phoneNumber = db.Column(db.String(20), primary_key = True)
    gender      = db.Column(db.String(20), nullable = False)
    name        = db.Column(db.String(50), nullable = False)
    age         = db.Column(db.String(10), nullable = False)
    preference  = db.Column(db.String(10), nullable = False)
    status      = db.Column(db.String(10), nullable = False)

    def __repr__(self):
        return '<name %r>' % self.name
