from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from random import random
app = Flask(__name__)
io = SocketIO(app)

@app.route('/')
def index():
    return 'test\n async_mode {}'.format(io.async_mode)

@app.route('/source')
def source():
    return render_template('source.html')

@app.route('/destination')
def destination():
    return render_template('destination.html')

@io.on("source image")
def sendToDestination(data):
    print("got data {}".format(random()))

if __name__ == '__main__':
    io.run(app, debug=True)