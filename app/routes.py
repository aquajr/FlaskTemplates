from app import app
from flask import render_template
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    """Index URL"""
    return render_template('index.html', title='Index Page')


@app.route('/about-me')
def about_me():
    """About Me URL"""
    return render_template('about_me.html', title='About Me Page')


@app.route('/login')
def login():
    """Login URL"""
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
    