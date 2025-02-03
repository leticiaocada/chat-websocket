from flask import Flask, jsonify, request, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@socketio.on('connect')
def handle_connect():
    socketio.emit("welcome-message", {"message": "Welcome to the chat"})

if __name__ == '__main__':
    socketio.run(app, debug=True)