from flask import Blueprint, session, render_template, redirect, request, url_for, g
from model import load_all, insert_all, get_user, get_user_by_id
import functools

auth_bp = Blueprint('auth_bp', __name__, static_folder='static', template_folder='templates', url_prefix='/auth')

@auth_bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = get_user(username, password)
        data = []
        error = None
        for user in users:
            data.append(user.id)
            data.append(user.username)
            data.append(user.password)

        if len(data) < 3:
            error = 'Invalid Username or Password'
            return render_template('auth.html', error=error)
            
        else:
            session.clear()
            session['user_id'] = data[0] #type: ignore 
            return redirect(url_for('home_bp.home'))
    return render_template('auth.html')

@auth_bp.route('/signup', methods=('GET', 'POST'))
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        age = request.form['age']
        phonenumber = request.form['phonenumber']
        sex = request.form['sex']

        nlist = [username, password, firstname, lastname, age, phonenumber, sex]
        error = None
        try:
            insert_all(nlist)
            return redirect(url_for('auth_bp.login'))
        except:
            error = f'User {username} or password exists already'
            return render_template('register.html', error=error)
        
        

    return render_template('register.html')


@auth_bp.before_app_request
def load_logged_in_users():
    user = session.get('user_id')

    if user is None:
        g.user = None

    else:
        g.user = get_user_by_id(user)


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth_bp.login'))
        
        return view(**kwargs)
    return wrapped_view