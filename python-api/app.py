from flask import render_template, request, jsonify, json
from static.models import db, app, bcrypt
from static.models import Users

@app.route('/', methods=['POST', 'GET'])
def getAllUsers():
    user = Users.query.all()
    for userinfo in user:
        users = {
            'User': userinfo.firstname + ' ' + userinfo.lastname,  
            'Username': userinfo.email,
            'Email': userinfo.email,
            'Password': userinfo.password
        }
    return jsonify(users)

@app.route('/register', methods=['POST'])
def registerUser():
    if request == 'POST':
        hashed_pw = bcrypt.generate_password_hashed(password.data)
        newUser = Users(
            firstname=firstnaem.data,
            lastname=lastname.data,
            username=username.data,
            email=email.data,
            password=password.data
        )
        db.session.add(newUSer)
        db.session.commit()

@app.route('/login', methods)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')