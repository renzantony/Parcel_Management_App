from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = '099b87a6fcf755824ed276ad8e8d865b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///parcels.db'  # Use MySQL URI for MySQL
db = SQLAlchemy(app)
socketio = SocketIO(app)

from app import routes, socketio_events
