"""
Simple Hit Counter using websockets, redis, and flask.
"""
import redis
from flask import Flask, render_template
from flask.ext.socketio import SocketIO

app = Flask(__name__)
kv_store = redis.Redis("localhost")
socketio = SocketIO(app)

@app.route('/')
def main():
    c = kv_store.incr('hit_count')
    return render_template("main.html", count=c)

@socketio.on('connect', namespace="/count")
def ws_connect():
    c = kv_store.get('hit_count')
    socketio.emit('message', {'count': c}, namespace="/count")

if __name__ == '__main__':
    socketio.run(app)
