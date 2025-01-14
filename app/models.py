from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime, server_default=db.func.now())
    phone = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"<User {self.username}>"
