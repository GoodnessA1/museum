from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Auth(db.Model):
    __tablename__ = "auth"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(100), unique=True)
    firstname = db.Column(db.Text)
    lastname = db.Column(db.Text)
    age = db.Column(db.Integer)
    phonenumber = db.Column(db.String(100), unique=True)
    sex = db.Column(db.Text)
    

def insert_all(x):
    add_details = Auth( #type: ignore
        username=x[0],
        password=x[1],
        firstname=x[2],
        lastname=x[3],
        age = x[4],
        phonenumber = x[5],
        sex = x[6]
        )
     
    db.session.add(add_details)
    db.session.commit()
    print("<--Data added successfully-->")
    return (0)

def load_all():
    data = Auth.query.all()
    return (data)

def get_user(name, password):
    user = Auth.query.filter_by(username=name, password=password)
    return (user)

def get_user_by_id(id):
    user = Auth.query.filter_by(id=id)
    return(user)