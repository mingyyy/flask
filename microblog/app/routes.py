from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        # get_flashed_messages() will render the messages stored in flash which will be deleted after
        # the flash function is called.
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


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
