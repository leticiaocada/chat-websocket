from flask import Flask, jsonify, request, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@socketio.on('connect')
def handle_connect(sid):
    socketio.emit("welcome-message", {"message": "Welcome to the chat"}, to=sid)

@socketio.on('message')
def handle_message(data):
    socketio.emit("message", data)

if __name__ == '__main__':
    socketio.run(app, debug=True, port=3000)