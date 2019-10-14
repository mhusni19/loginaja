from flask import Blueprint
from flask_mysqldb import MySQL

main = Blueprint('main',__name__)

@main.route('/')
def index():
    return 'Index'


@main.route('/profile')
def profile():
    return 'Profile'