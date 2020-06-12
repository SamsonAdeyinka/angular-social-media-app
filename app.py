from flask import Flask, render_template, request
from static.models import db, app

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)