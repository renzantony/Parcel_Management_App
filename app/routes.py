from flask import render_template, request, redirect, url_for
from app import app, db,socketio
from app.models import Parcel
import pandas as pd
import time
import random
from flask_socketio import emit 

TRACKING_STATUSES = ['In Transit', 'Out for Delivery', 'Delivered', 'Pending', 'Returned to Sender']

@app.route('/')
def index():
    return  render_template('index.html')
@app.route('/track-live')
def track_live():
    return render_template('track_live.html')

@socketio.on('track_request')
def handle_track_request(data):
    # Simulate real-time parcel status update
    status_list = ['In Transit', 'Out for Delivery', 'Delivered', 'Delayed']
    live_status = random.choice(status_list)
    emit('track_update', {'status': live_status})

@app.route('/parcels', methods=['GET', 'POST'])
def parcel_list():
    if request.method == 'POST':
        parcel_id = request.form['parcel_id']
        sender = request.form['sender']
        recipient = request.form['recipient']
        status = request.form['status']
        date = request.form['date']
        new_parcel = Parcel(parcel_id=parcel_id, sender=sender, recipient=recipient, status=status, date=date)
        db.session.add(new_parcel)
        db.session.commit()
        return redirect(url_for('parcel_list'))
        # Filtering functionality
    query = Parcel.query
    sender_filter = request.args.get('sender')
    date_filter = request.args.get('date')
    parcel_id_filter = request.args.get('parcel_id')

    if sender_filter:
        query = query.filter(Parcel.sender.ilike(f'%{sender_filter}%'))
    if date_filter:
        query = query.filter(Parcel.date == date_filter)
    if parcel_id_filter:
        query = query.filter(Parcel.parcel_id.ilike(f'%{parcel_id_filter}%'))

    
    parcels = Parcel.query.all()
    return render_template('parcel_list.html', parcels=parcels)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_parcel(id):
    parcel = Parcel.query.get(id)
    if request.method == 'POST':
        parcel.sender = request.form['sender']
        parcel.recipient = request.form['recipient']
        parcel.status = request.form['status']
        parcel.date = request.form['date']
        db.session.commit()
        return redirect(url_for('parcel_list'))
    
    return render_template('update_parcel.html', parcel=parcel)

@app.route('/track/<int:id>',methods=['GET'])
def track_parcel(id):
    parcel = Parcel.query.get(id)
 
    live_status = random.choice(TRACKING_STATUSES)   
    return render_template('track_parcel.html', parcel=parcel, live_status=live_status)


@app.route('/report')
def report():
    # Dummy report data
    progress = 75  # For example, 75% completion
    return render_template('report.html', progress=progress)

@app.route('/bulk_process')
def bulk_process():
    # Simulate bulk processing of parcels
    total_parcels = 100  # Example
    for i in range(total_parcels):
        time.sleep(0.1)  # Simulating processing time
        progress = int((i + 1) / total_parcels * 100)
        socketio.emit('progress', {'progress': progress})

    return render_template('bulk_process.html')


