from app import db


class JobPosition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.String(120))
    description = db.Column(db.String(120))
    requirements = db.Column(db.String(120))
    picture = db.Column(db.String(60))

    def __repr__(self):
        return '<User %r>' % (self.nickname)


