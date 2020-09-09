from flask import Blueprint, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_user

from src.server import db
from src.models import User

module = Blueprint('authentication',__name__)

@module.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return 'Selection screen '
    if request.method == 'GET':
        return 'Login screen'
    else:
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again!')
            return redirect(url_for('authentication.login'))

        login_user(user)

        return 'Selection screen  '
@module.route('/create', methods=['GET','POST'])
def create():
    if current_user.is_authenticated:
        return 'Selection screen'
    if request.method == 'GET':
        return 'Sign up screen'
    else:
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email address already exists.')
            return redirect(url_for('authentication.create'))
        
        user = User(email,password=generate_password_hash(password,method='sha256'))

        db.session.add(user)
        db.session.commit()

        return 'Selection screen'


@module.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('authentication.login'))