from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO(async_mode="threading")

def create_app():
    app = Flask(__name__)

    from project.web_app.routes import main_bp
    app.register_blueprint(main_bp)

    socketio.init_app(app)
    import project.web_app.socketio_handlers

    return app