from flask import Blueprint, render_template
from flask_login import login_required
from app.authorized import role_required

home = Blueprint('home', __name__, url_prefix='/home')

@home.route('/')
@login_required
def homepage():
    return render_template('home.html')


@home.route('/admin')
@login_required
@role_required(has_role=['Admin'])
def admin():
    return "ADMIN"


@home.route('/user')
@login_required
@role_required(has_role=['User'])
def user():
    return "USER"


@home.route('/superuser')
@login_required
@role_required(has_role=['User', 'Admin'])
def superuser():
    return "SUPERUSER"