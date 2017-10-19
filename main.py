from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:blog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
app.secret_key = 'spaceballs12345'

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(120))

    def __init__ (self, title, body):
        self.title = title
        self.body = body

@app.route('/newpost', methods=['POST', 'GET'])
def newpost():
    if request.method == 'POST':
        new_title = request.form['title']
        new_body = request.form['body']
        title_error = ''
        body_error = ''
        if len(new_title) == 0:
            title_error = 'Please enter a title'
        if len(new_body) == 0:
            body_error = 'Please enter a blog'
        if title_error != '' or body_error != '':
            return render_template('newpost.html', title_error=title_error,
                body_error=body_error, new_title=new_title, new_body=new_body)
        else:
            blog = Blog(new_title, new_body)
            db.session.add(blog)
            db.session.commit()
            return redirect('/blog?id=' + str(blog.id))
      
    return render_template('/newpost.html')


@app.route('/blog', methods=['POST','GET'])
def blog():
    #grab id from request
    blog_id = request.args.get('id')
    if blog_id != None:
        blog = Blog.query.get(blog_id)
        return render_template('individual.html', blog=blog)

    blogs = Blog.query.all()

    return render_template('mainblog.html', blogs=blogs)
    


if __name__ == '__main__':
    app.run()
