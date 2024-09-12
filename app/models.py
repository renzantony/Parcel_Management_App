from app import db

class Parcel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parcel_id = db.Column(db.String(20), unique=True, nullable=False)
    sender = db.Column(db.String(100), nullable=False)
    recipient = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(20), nullable=False)
