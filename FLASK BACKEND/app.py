from flask import Flask
app = Flask(__name__)
@app.route('/', methods=['GET'])
def welcome():
    return 'Wellcome'
@app.route('/add/<a>/<b>', methods=['GET'])
def addition(a,b):
    a = int(a)
    b = int(b)
    return f'addition of {a} and {b} is {a+b}'
@app.route('/sub/<a>/<b>', methods=['GET'])
def subtraction(a,b):
    a = int(a)
    b = int(b)
    return f'addition of {a} and {b} is {a-b}'
@app.route('/mul/<a>/<b>', methods=['GET'])
def multiplication(a,b):
    a = int(a)
    b = int(b)
    return  f'multiplication of {a} and {b} is {a*b}'
@app.route('/div/<a>/<b>', methods=['GET'])
def division(a,b):
    a = int(a)
    b = int(b)
    return f'division of {a} and {b} is {a/b}'

app.run()
