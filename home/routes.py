from flask import Blueprint

home_mod = Blueprint('home',__name__)

@home_mod.route('/')
def index():
    return '<h1>Estas en el home</h1>'