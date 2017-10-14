from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build_a-blog:blog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(120))

    def __init__ (self, title, body):
        self.title = title
        self.body = body

@app.route('/blog', methods=['POST', 'GET'])

@app.route('/newpost', methods=['POST', 'GET'])



@app.route('/', methods=['POST','GET'])
def index():

    return render_template('newpost.html')


if __name__ == '__main__':
    app.run()
