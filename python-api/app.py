from flask import render_template, request, jsonify, json, make_response
from static.models import db, app
from static.models import Users


@app.route('/register', methods=['POST', 'GET'])
def registerUser():
    req = request.get_json()
    if Users.query.filter_by(email=req.get("email")).first():
        return jsonify({"Message": "The user already exists"})

    else:
        newUser = Users(
            firstname=req.get("firstname"),
            lastname=req.get("lastname"),
            username=req.get("username"),
            email=req.get("email"),
            password=req.get("password")
        )
        db.session.add(newUser)
        db.session.commit()

        return jsonify({"Message": "User has been added to the database"}), 200

@app.route('/login', methods=['GET'])
def login():
    return "something"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
