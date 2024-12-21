from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)


class Court(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    reserved = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    sport = db.Column(db.String(80), nullable=False)
    num = db.Column(db.Integer, nullable=False)

    user = db.relationship('User', backref=db.backref('courts', lazy=True))
