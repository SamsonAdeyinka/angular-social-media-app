from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import Flask

app = Flask(__name__)
# bcrypt = Bcrypt(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://alebaba:admin@localhost/socialmedia'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Samso\\Documents\\Projects\\angular-social-media-app\\python-api\\static\\socialmedia.db'
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
            'Username: ', self.username, '\r\n',
            'Email: ', self.email, '\r\n'
        ])


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(255), nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return ''.join([
            'User: ', self.user_id.firstname, ' ', self.user_id.lastname, '\r\n',
            'Post: ', self.body, '\r\n',
            'Date: ', self.pub_date, '\r\n',
            'Likes: ', self.likes
        ])
