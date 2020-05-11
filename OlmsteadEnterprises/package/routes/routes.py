from package import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request
from package.forms import SignUpForm, LoginForm
from package.database import User, Post
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    if current_user.is_authenticated:
        flash(f'You are logged in as {current_user.username}', 'success')
    form = SignUpForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(firstname=form.firstname.data, lastname=form.lastname.data, username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        #login_user(user)
        flash(f'Your Account has been created!', 'success')
        return redirect(url_for('profile'))

    return render_template('home.html', title='Home', form=form)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash(f'You are already logged in as {current_user.username}', 'success')
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            flash(f'Successful Login! {current_user.username}', 'success')
            return redirect(url_for('profile'))
        else:
            flash(f'Login Unsuccessful!  Please check email and password!', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash(f'You have been logged out!', 'danger')
    return redirect(url_for('login'))

@app.route('/profile')
@login_required
def profile():
    fname = current_user.firstname
    lname = current_user.lastname
    username = current_user.username
    email = current_user.email
    return render_template("profile.html", fname=fname, lname=lname, username=username, email=email)

@app.route('/library', methods=['GET', 'POST'])
def library():
    return render_template('library.html', title='Library')
