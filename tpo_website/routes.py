from flask import render_template, request, Response, redirect, url_for, flash
from tpo_website import app, db, bcrypt
from tpo_website.forms import *
from tpo_website.models import *
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import or_


@app.route('/',methods=['GET', 'POST'])
@app.route('/index',methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(uid=form.uid.data).first()
        if user and bcrypt.check_password_hash(user.password,
                                               form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f'You have successfully logged in!',
              'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password',
                  'danger')
    return render_template('/index.html',title='TPO Login Form', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('/student/dashboard.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(uid=form.uid.data,
        studentname=form.studentname.data,
        email=form.email.data,
        mobile=form.mobile.data,
        sem1=form.sem1.data,
        sem2=form.sem2.data,
        sem3=form.sem3.data,
        sem4=form.sem4.data,
        sem5=form.sem5.data,
        sem6=form.sem6.data,
        backlogs=form.backlogs.data,
        juniorcollegemarks=form.juniorcollegemarks.data,
        secondarymarks=form.secondarymarks.data,
        homeaddress=form.homeaddress.data,
        branch=form.branch.data,
        year=form.year.data,
        password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created for {form.studentname.data}!',
              'success')
        return redirect(url_for('dashboard')) 
    return render_template('/signup.html', title='SignUp Form', form=form)

@app.route('/company_det')
def company_det():
    return render_template('/student/company_det.html')

@app.route('/comp_indi')
def comp_indi():
    return render_template('/student/comp_indi.html')

@app.route('/student_profile')
def student_profile():
    return render_template('/student/student_profile.html')

@app.route('/calendar')
def calendar():
    return render_template('/student/calendar.html')
