from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint("auth", __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get('password')
        user =  User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                # flash("You have been logged in!", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Wrong Password!", category='error')
        else:
            flash("Email doesn't exists.", category='error')

    return render_template('login.html', user=current_user)

@auth.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        print([email, username, password1, password2])

        username_exists = User.query.filter_by(username=username).first()
        email_exists = User.query.filter_by(email=email).first()

        if email_exists:
            flash("Email is already in use.", category="error")
        elif username_exists:
            flash("Username is already in use.", category='error')
        elif password1 != password2:
            flash("Passwords don't match", category='error')
        elif len(username)<2:
            flash("Username is too short", category='error')
        elif len(email) < 4:
            flash("Email Id is too short", category='error')
        elif len(password1)<6:
            flash("Password is too short", category='error')
        else:
            new_user = User(username=username, email=email, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('User created!', category='message')
            return redirect(url_for('views.home'))
        
    return render_template('signup.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    # flash("You have been logged out!")
    return redirect(url_for("views.home"))