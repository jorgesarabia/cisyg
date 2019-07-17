from flask import Blueprint
from flask import render_template

user_mod = Blueprint('users',__name__,template_folder='templates')

@user_mod.route('/users')
def index():
    return render_template('users/home.html')
