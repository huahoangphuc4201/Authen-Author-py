from flask import Blueprint, render_template
from flask_login import login_required

home = Blueprint('home', __name__, url_prefix='/home')

@home.route('/')
@login_required
def homepage():
    return render_template('home.html')