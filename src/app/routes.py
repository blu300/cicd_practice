from src.app import test_app
from flask import request

@test_app.route('/')
@test_app.route('/index')
def index():
    return "Hello world"

@test_app.route('/test')
def test_args():
    lang = request.args.get('language')
    return 

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