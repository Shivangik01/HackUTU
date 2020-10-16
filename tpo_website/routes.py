from flask import render_template, request, Response, redirect, url_for, flash
from tpo_website import app
from tpo_website.forms import *
from tpo_website.models import *
#from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import or_


@app.route('/')
@app.route('/index')
def index():
    return render_template('/index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('/dashboard.html')

@app.route('/company_det')
def company_det():
    return render_template('/company_det.html')

@app.route('/comp_indi')
def comp_indi():
    return render_template('/comp_indi.html')

