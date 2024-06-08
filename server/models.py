from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

db = SQLAlchemy()

def generate_uuid():
    return str(uuid.uuid4())


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(50), primary_key = True, default = generate_uuid())
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    role = db.Column(db.String(50))
    email = db.Column(db.String(50))
    created_at = db.Column(db.Datetime, nullable = False, default=datetime.utcnow)

class Doctor(db.Model):
    __tablename__ = 'doctors'

    id = db.Column(db.String(50), primary_key=True, default= generate_uuid())
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(40))
    department_id = db.Column(db.String(40), db.ForeignKey('department.id'))
    profile_photo = db.Column(db.String(40))
