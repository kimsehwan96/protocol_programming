from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
async_mode = None
CORS(app)
socketio = SocketIO(app, async_mode=async_mode, cors_allowed_origins='*')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    send(message)

def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(1)
        count += 1
        socketio.emit('test_rtdata',
                      {'data': 'Server generated event', 'count': count}, namespace='/data')

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))

@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))


if __name__ == '__main__':
    background_thread()
    socketio.run(app)