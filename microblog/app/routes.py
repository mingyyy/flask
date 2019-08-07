from app import app
from flask import render_template


@app.route('/index')
def index():
    user = {'username': 'Mingy'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/')
def main():
    user = {'username': 'Ming'}
    return render_template('base.html', user=user)
