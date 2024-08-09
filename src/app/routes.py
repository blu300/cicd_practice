from flask import request

from src.app import test_app


@test_app.route('/')
@test_app.route('/index')
def index():
    return "Hello world"

@test_app.route('/test')
def test_args():
    lang = request.args.get('language', "pass an argument")
    return str(lang)

@test_app.route('/add')
def add():
    data = request.args.get('data', None)
    _list = list(map(int, data.split(',')))

    total = sum(_list)
    return "Results = " + str(total)

def sum(arg):
    try:
        total = 0
        for val in arg:
            total += val
    except Exception as e:
        return "Error occured: ", e
    
    return total