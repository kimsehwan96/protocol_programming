from flask import Flask, render_template, request, jsonify
#from flask.ext.socketio import SOcketIO, emit

import random
import threading

TEST_VALUE = None

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'secret!'
#socketio = SOcketIO(app)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/index/')
def render_index(var=TEST_VALUE):
    var = TEST_VALUE
    return render_template('index.html',var=var)

#api ?
@app.route('/data')
def data_api():
    return jsonify({
        "InputValue_1" : random.randint(1, 100),
        "InputValue_2" : random.randint(1, 100),
        "InputValue_3" : random.randint(1, 100),
        "RTDValue_1" : random.randint(1, 100)
    })

def making_number():
    global TEST_VALUE
    TEST_VALUE = random.randint(1,100)
    threading.Timer(1,making_number).start()

#TODO: socketIO 적용

if __name__ == '__main__':
    making_number()
    app.run(debug=True)
