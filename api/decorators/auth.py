from functools import wraps
from flask import current_app, request, abort


def require_key(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        if request.headers.get('x-api-key') and request.headers.get('x-api-key') == current_app.config['API_KEY']:
            return view_function(*args, **kwargs)
        else:
            abort(403)

    return decorated_function


def require_test(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        print("Pase por aqui")
        return view_function(*args, **kwargs)

    return decorated_function
