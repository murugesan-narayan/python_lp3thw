from flask import Flask
from flask import escape
from flask import url_for
from flask import render_template
from flask import request
from flask import redirect

app = Flask(__name__)

@app.route('/')
def index():
    greeting = "Hello World"
    return render_template("index.html", greeting=greeting)

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>', methods=['GET'])
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login')
def login():
    return 'login %s' % request.method

@app.route('/redirect')
def redirect_test():
    return redirect(url_for('login'))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('static', filename='style.css'))
    print(url_for('show_user_profile', username='John Doe'))

if __name__ == "__main__":
    app.run()
