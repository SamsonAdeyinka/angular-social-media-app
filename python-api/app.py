from flask import render_template, request, jsonify, json, make_response
from static.models import db, app
from static.models import Users


@app.route('/register', methods=['POST', 'GET'])
def register():
    req = request.get_json()
    user = Users.query.filter_by(email=req.get("email")).first()
    if user:
        response = jsonify({
            "Message": "The user already exists",
            "User": json.dumps(user, indent=2)
        })
        return response, 200

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

        response = jsonify({
            "Message": "User has been added to the database",
            "User": newUser
        })
        return response, 200


@app.route('/login', methods=['POST', 'GET'])
def login():
    req = request.get_json()
    user = Users.query.filter_by(email=req.get('email')).first()
    for row in user:
        user = {
            "id": row[0],
            "firstname": row[1]
        }
        return jsonify(user)


@app.route('/posts', methods=['GET'])
def posts():
    all_posts = Posts.query.all()
    return "blah"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
