from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, leave_room, emit
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
socketio = SocketIO(app)

rooms = {}

@app.route('/')
def home():
    return render_template('index.html')

@socketio.on('create_room')
def create_room(data):
    room_id = data['room_id']
    password = data['password']
    if room_id not in rooms:
        rooms[room_id] = password
        join_room(room_id)
        emit('room_created', {'room_id': room_id}, room=room_id)
    else:
        emit('error', {'message': 'Room already exists.'})

@socketio.on('join_room')
def join_room_event(data):
    room_id = data['room_id']
    password = data['password']
    if room_id in rooms and rooms[room_id] == password:
        join_room(room_id)
        emit('room_joined', {'room_id': room_id}, room=room_id)
    else:
        emit('error', {'message': 'Invalid room ID or password.'})

@socketio.on('send_message')
def handle_message(data):
    room_id = data['room_id']
    message = data['message']
    username = data['username']
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    emit('receive_message', {
        'message': message,
        'username': username,
        'timestamp': timestamp
    }, room=room_id, broadcast=True, include_self=False)

if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)