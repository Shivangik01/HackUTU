from flask import session, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from tpo_website.models import *

class RegistrationForm(FlaskForm):
    uid = StringField('College UID',validators=[DataRequired(),Length(min=1, max=20)],render_kw={"placeholder":"College UID"})
    studentname = StringField('Studentname',validators=[DataRequired(),Length(min=2, max=20)],render_kw={"placeholder":"Student Name"})
    branch=StringField('Branch',validators=[DataRequired(),Length(min=2, max=20)],render_kw={"placeholder":"Branch"})
    year=StringField('Year',validators=[DataRequired(),Length(min=2, max=10)],render_kw={"placeholder":"Year"})
    homeaddress=StringField('Address',validators=[DataRequired(),Length(min=2, max=70)],render_kw={"placeholder":"Address"})
    #secondaryboard=StringField('10th Board',validators=[DataRequired(),Length(min=2, max=20)],render_kw={"placeholder":"10th Board"})
    secondarymarks=StringField('10th Marks',validators=[DataRequired(),Length(min=2, max=10)],render_kw={"placeholder":"10th Marks"})
    #juniorcollegeboard=StringField('12th Board',validators=[DataRequired(),Length(min=2, max=20)],render_kw={"placeholder":"12th Board"})
    juniorcollegemarks=StringField('12th Marks',validators=[DataRequired(),Length(min=2, max=10)],render_kw={"placeholder":"12th Marks"})
    sem1=StringField('SEM I',validators=[DataRequired(),Length(min=2, max=3)],render_kw={"placeholder":"SEM I CGPA"})
    sem2=StringField('SEM II',validators=[DataRequired(),Length(min=2, max=3)],render_kw={"placeholder":"SEM II CGPA"})
    sem3=StringField('SEM III',validators=[DataRequired(),Length(min=2, max=3)],render_kw={"placeholder":"SEM III CGPA"})
    sem4=StringField('SEM IV',validators=[DataRequired(),Length(min=2, max=3)],render_kw={"placeholder":"SEM IV CGPA"})
    sem5=StringField('SEM V',validators=[DataRequired(),Length(min=1, max=3)],render_kw={"placeholder":"SEM V CGPA"})
    sem6=StringField('SEM VI',validators=[DataRequired(),Length(min=1, max=3)],render_kw={"placeholder":"SEM VI CGPA"})
    backlogs=StringField('Backlog',validators=[DataRequired(),Length(min=1, max=3)],render_kw={"placeholder":"Backlogs (if any)"})
    email = StringField('Email', validators=[DataRequired(), Email()],render_kw={"placeholder":"Email"})
    mobile = StringField('Mobile Number',validators=[DataRequired(), Length(min=10, max=10)],render_kw={"placeholder":"Phone Number"})
    password = PasswordField('Password', validators=[DataRequired()],render_kw={"placeholder":"Password"})
    confirmpassword = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')],render_kw={"placeholder":"Confirm Password"})
    submit = SubmitField('SUBMIT')

    def validate_uid(self, uid):
        user = User.query.filter_by(uid=uid.data).first()
        if user:
            raise ValidationError(
                'That uid is taken. Please write a valid one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    uid = StringField('UID', validators=[DataRequired()],render_kw={"placeholder":"UID"})
    password = PasswordField('Password', validators=[DataRequired()],render_kw={"placeholder":"Password"})
    remember = BooleanField('Remember Me')
    submit = SubmitField('SIGN IN')

class CompanyDetailsForm(FlaskForm): 
    company_name = StringField('Company Name',validators=[DataRequired(),Length(min=1, max=20)],render_kw={"placeholder":"Company Name"})
    company_type = StringField('Company Type',validators=[DataRequired(),Length(min=1, max=20)],render_kw={"placeholder":"Company Type"})
    company_category = StringField('Company Category',validators=[DataRequired(),Length(min=1, max=20)],render_kw={"placeholder":"Company Category"})
    position = StringField('Position Offered',validators=[DataRequired(),Length(min=1, max=20)],render_kw={"placeholder":"Position Offered"})
    details = StringField('Company details',validators=[DataRequired(),Length(min=1, max=20)],render_kw={"placeholder":"Company details"})
    submit = SubmitField('SUBMIT')


