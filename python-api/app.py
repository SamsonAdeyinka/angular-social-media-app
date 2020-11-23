from flask import render_template, request, jsonify, json, redirect, url_for
from flask_login import login_user, login_required
from static.models import db, app, bcrypt, login_manager
from static.models import Users, user_schema, Post, post_schema


@app.route('/api/users')
def users():
    all_users = Users.all()
    return user_schema.dump(all_users)

@app.route('/api/users/<id>')
def user_detail(id):
    user = Users.get(id)
    return user_schema.dump(user)

@app.route('/register', methods=['POST'])
def register_user():
    existing_email = Users.query.filter_by(email=request.json['email']).first()
    existing_user = Users.query.filter_by(username=request.json['username']).first()
    if existing_email or existing_user:
        response = jsonify({
            "Message": "The user already exists",
            "User": user_schema.dump(existing_user)
        })
        return response
    else:
        new_user = Users(
            firstname=request.json['firstname'],
            lastname=request.json['lastname'],
            username=request.json['username'],
            email=request.json['email'].lower(),
            password=request.json['password']
            )

        db.session.add(new_user)
        db.session.commit()

        response = jsonify({
            "Message": "New user has been added to the database",
            "User": user_schema.dump(new_user)
        })
        return response


@app.route('/login', methods=['POST'])
def login():
    email_input = request.json['email'].lower()
    pass_word = request.json['password']
    
    user = Users.query.filter_by(email=email_input).first()
    if user and pass_word == user.password:
        login_user(user)
        response = jsonify({
            "Message": "User logged in",
            "User": {
                "Username": user_schema.dump(user)
            }
        })
        return redirect(url_for('home'))
    else:
        response = jsonify({
            "Message": "The email address or password is incorrect!"
        })
        return response

@app.route('/home', methods=['POST', 'GET'])
@login_required
def home():
    return "Hello World"

@app.route('/api/posts')
def posts():
    all_posts = Post.query.all()
    return "blah"

@app.route('/api/posts/<id>')
def posts_details(id):
    post = Post.get(id)
    return post_schema.dump(post)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
