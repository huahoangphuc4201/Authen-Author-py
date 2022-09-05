from functools import wraps
from flask import flash, render_template
from flask_login import current_user

def role_required(has_role=[], at_least=[]):
    def decorator(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            roles = list(map(lambda role: role.name, current_user.roles))
            if len(has_role) == 0 and any(role in roles for role in at_least):
                return f(*args, **kwargs)
            elif all(role in roles for role in has_role):
                if len(at_least) == 0 or any(role in roles for role in at_least):
                    return f(*args, **kwargs)
            else:
                flash("Unauthorized")
                return render_template('unauthorized.html')
        return wrap
    return decorator
