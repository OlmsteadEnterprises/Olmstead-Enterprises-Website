from wtforms import StringField, PasswordField, SubmitField, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError
from package.database import User, Post

class SignUpForm(FlaskForm):
    firstname = StringField('First Name: ', validators=[DataRequired()], render_kw={"placeholder":"First Name: "})
    lastname = StringField('Last Name: ', validators=[DataRequired()], render_kw={"placeholder":"Last Name: "})
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=20)], render_kw={"placeholder":"Username: "})
    email = StringField('Email', validators=[DataRequired(), Length(min=5, max=30)], render_kw={"placeholder":"Email: "})
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password')],
                             render_kw={"placeholder":"Password: "})
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')],
                                     render_kw={"placeholder":"Confirm Password: "})
    submit = SubmitField('Submit')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exists!  Please choose another!')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists!  Please choose another!')

class LoginForm(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired()], render_kw={"placeholder":"Email"})
    password = PasswordField('Password: ', validators=[DataRequired()], render_kw={"placeholder":"Password"})
    remember_me = BooleanField('Remember Me')
    submit = SubmitField(render_kw={"placeholder":"Login"})