from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://alebaba:admin@localhost:3306/socialmedia'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECERT_KEY'] = 'Alebaba'

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    user = db.relationship('Post', backref=db.backref('user', lazy=True))

    def __repr__(self):
        return ''.join([
            'User: ', self.firstname, ' ', self.lastname, '\r\n',
            'Email: ', self.email, ' ', self
        ])


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(255), nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return ''.join([
            'User: ', self.user_id.firstname, ' ', self.user_id.lastname,
            'Post: ', self.body,
            'Date: ', self.pub_date,
            'Likes: ', self.likes
        ])
