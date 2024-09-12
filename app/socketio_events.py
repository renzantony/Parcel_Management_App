from app import socketio
from flask_socketio import emit

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('start_processing')
def handle_processing(data):
    import time
    for i in range(5):
        time.sleep(1)
        socketio.emit('progress_update', {'progress': (i + 1) * 20})
        
@socketio.on('track_parcel')
def handle_track_parcel(data):
    # Here you would implement the logic to track parcel status
    # For demonstration purposes, we send a dummy update
    emit('parcel_status', {'status': 'Parcel is in transit'}, broadcast=True)
