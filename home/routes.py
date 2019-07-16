from flask import Blueprint
from flask import render_template

home_mod = Blueprint('home',__name__)

@home_mod.route('/')
def index():
    return render_template('home.html')