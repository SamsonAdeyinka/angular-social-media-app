from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_login import LoginManager, UserMixin
from flask_bcrypt import Bcrypt
from datetime import datetime
from collections import OrderedDict

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://alebaba:admin@localhost/socialmedia'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Samso\\Documents\\Projects\\angular-social-media-app\\python-api\\static\\socialmedia.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Alebaba'

db = SQLAlchemy(app)
ma = Marshmallow(app)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user = db.relationship('Post', backref=db.backref('user', lazy=True))

    def __repr__(self):
        return ''.join([
            'User: ', self.firstname, ' ', self.lastname, '\r\n',
            'Username: ', self.username, '\r\n',
            'Email: ', self.email, '\r\n',
            'Date Created', self.date_created, '\r\n'
        ])
    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))
        
# User Schema
class UserSchema(ma.Schema):
    # Smart Hyperlink
    _links = ma.Hyperlinks({
        "self": ma.URLFor("user_detail", values=dict(id="<id>")),
        "collection": ma.URLFor("users")
    })
    class Meta:
        # fields to expose
        fields = ('id', 'firstname', 'lastname', 'username', 'email', 'password', 'date_created')
        ordered = True
    

# Init User Schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

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
# Post Schema
class PostSchema(ma.Schema):
    class Meta:
        # fields to expose
        fields = ('id', 'body', 'like', 'pub_date', '_links')
    # Smart Hyperlink
    _links = ma.Hyperlinks({
        "self": ma.URLFor("post_details", values=dict(id="<id>")),
        "collection": ma.URLFor("posts"),
    })

# Init Post Schema    
post_schema = PostSchema()
posts_schema = PostSchema(many=True)