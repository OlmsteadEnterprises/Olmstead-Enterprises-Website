from package import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request
from package.forms import SignUpForm, LoginForm
from package.database import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from datetime import date


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    if current_user.is_authenticated:
        flash(f'You are logged in as {current_user.username}', 'success')
    form = SignUpForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(firstname=form.firstname.data, lastname=form.lastname.data, username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash(f'Your Account has been created!', 'success')
        return redirect(url_for('profile'))

    return render_template('index.html', title='Home', form=form)

@app.route('/investments', methods=['GET', 'POST'])
def investments():
    return render_template("investments.html", title='Investments')

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
    return render_template("profile.html", fname=fname, lname=lname, username=username, email=email, title='Profile')

@app.route('/january_cash_flow', methods=['GET', 'POST'])
def january_cash_flow():
    return render_template("cash-flow/jan.html", title='January Cash Flow')
@app.route('/february_cash_flow', methods=['GET', 'POST'])
def february_cash_flow():
    return render_template("cash-flow/feb.html", title='February Cash Flow')
@app.route('/march_cash_flow', methods=['GET', 'POST'])
def march_cash_flow():
    return render_template("cash-flow/mar.html", title='March Cash Flow')
@app.route('/april_cash_flow', methods=['GET', 'POST'])
def april_cash_flow():
    return render_template("cash-flow/apr.html", title='April Cash Flow')
@app.route('/may_cash_flow', methods=['GET', 'POST'])
def may_cash_flow():
    return render_template("cash-flow/may.html", title='May Cash Flow')
@app.route('/june_cash_flow', methods=['GET', 'POST'])
def june_cash_flow():
    return render_template("cash-flow/june.html", title='June Cash Flow')
@app.route('/july_cash_flow', methods=['GET', 'POST'])
def july_cash_flow():
    return render_template("cash-flow/july.html", title='July Cash Flow')