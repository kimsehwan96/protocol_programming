
import random
import os
from flask import Flask, render_template, session
from flask_socketio import SocketIO, emit
import threading

async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode, cors_allowed_origins='*')
TEST_VALUE = None

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect', namespace='/mynamespace')
def connect():
    emit("response", {'data': 'Connected'})

@socketio.on('disconnect', namespace='/mynamespace')
def disconnect():
    session.clear()
    print("Disconnected")

@socketio.on('message')
def handle_message(message=TEST_VALUE):
    print('received message: ' + message)

def background_thread():
    count = 0
    while True:
        socketio.sleep(1)
        count += 1
        socketio.emit('test_data',
                      {'data': 'Server generated event', 'count': count}, namespace='/mynamespace')

def making_number():
    global TEST_VALUE
    TEST_VALUE = random.randint(1,100)
    threading.Timer(1,making_number).start()


if __name__ == '__main__':
    making_number()
    app.run()
    socketio.run(app)