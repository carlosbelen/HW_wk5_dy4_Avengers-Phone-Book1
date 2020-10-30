from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email
# The above:
# DataRequired == Making sure the field is filled in 
# EqualTo == Making sure the field(s) are the same (I.E Password and Confirm Password)
# Email == Making sure the field has a proper email given to it

# Below:
# inherits information from WTF and secetkey
class UserInfoForm(FlaskForm):
    username = StringField('Avenger Name', validators = [DataRequired()])
    phone = StringField('Phone', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    # equal to 'password' is confirming the users inputed password. lowercase p to equal the name password 2 lines above
    submit = SubmitField()
# this class funcition will be used in Routes.py where it'll be instantiated.

class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField()

class PostForm(FlaskForm):
    phone = StringField('Phone', validators = [DataRequired()])
    submit = SubmitField()

    