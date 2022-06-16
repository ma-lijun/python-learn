from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import emit
from flask import request


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, logger=True, engineio_logger=True)

# The flask run command introduced in Flask 0.11 can be used to start a Flask-SocketIO development server based on Werkzeug, but this method of starting the Flask-SocketIO server is not recommended due to lack of WebSocket support. Previous versions of this package included a customized version of the flask run command that allowed the use of WebSocket on eventlet and gevent production servers, but this functionality has been discontinued in favor of the socketio.run(app) startup method shown above which is more robust.


#todo Receiving Messages
# 无命名的socket服务 ， 接受消息体为 string类型
@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)

# 无命名的socket服务 ， 接受消息体为 json 类型
@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))

# 自命名为my event的socket服务 ， 接受消息体为 json 类型
@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

# 命名服务的，
@socketio.on('my event', namespace='/test')
def handle_my_custom_namespace_event(json):
    print('received json: ' + str(json))

# todo 响应  send() and emit() functions
# SocketIO supports acknowledgment callbacks that confirm that a message was received by the client:

@socketio.on('my event')
def handle_my_custom_event(json):
    emit('my response', json, namespace='/chat')

# 收到消息后的确认回调
def ack():
    print('message was received!')


@socketio.on_error_default  # handles all namespaces without an explicit error handler
def default_error_handler(e):
    print(e)
    print(request.event["message"]) # "my error event"
    print(request.event["args"])    # (data,)

# The send() and emit() functions accept an optional to argument that cause the message to be sent to all the clients that are in the given room.
#
# All clients are assigned a room when they connect, named with the session ID of the connection, which can be obtained from request.sid. A given client can join any rooms, which can be given any names. When a client disconnects it is removed from all the rooms it was in. The context-free socketio.send() and socketio.emit() functions also accept a to argument to broadcast to all clients in a room.
#
# Since all clients are assigned a personal room, to address a message to a single client, the session ID of the client can be used as the to argument.

if __name__ == '__main__':
    socketio.run(app)