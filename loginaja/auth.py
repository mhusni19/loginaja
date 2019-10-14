from flask import Blueprint
from flask_mysqldb import MySQL

auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return 'Login'

@auth.route('/signup')
def signup():
    return 'Signup'

@auth.route('/logout')
def logout():
    return 'Logout'
