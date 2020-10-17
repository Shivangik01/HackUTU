from tpo_website import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    uid=db.Column(db.String(20), unique=True, nullable=False)
    studentname = db.Column(db.String(20), unique=True, nullable=False)
    branch=db.Column(db.String(20), nullable=False)
    year=db.Column(db.Integer, nullable=False)
    homeaddress=db.Column(db.String(50), nullable=False)
    secondaryboard=db.Column(db.String(30), nullable=True)
    secondarymarks=db.Column(db.String(2), nullable=True)
    juniorcollegeboard=db.Column(db.String(30), nullable=True)
    juniorcollegemarks=db.Column(db.String(2), nullable=True)
    sem1=db.Column(db.String(2), nullable=True)
    sem2=db.Column(db.String(2), nullable=True)
    sem3=db.Column(db.String(2), nullable=True)
    sem4=db.Column(db.String(2), nullable=True)
    sem5=db.Column(db.String(2), nullable=True)
    sem6=db.Column(db.String(2), nullable=True)
    #sem7=db.Column(db.Numeric(2,2), nullable=False)
    #sem8=db.Column(db.Numeric(2,2), nullable=False)
    backlogs=db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    mobile = db.Column(db.Integer, unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"User('{self.username}' , '{self.email}', '{self.mobile}')"
