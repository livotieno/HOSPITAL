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
    specialization = db.Column(db.String(40))
    profile_photo = db.Column(db.String(40))


class Cleaner(db.Model):
    __tablename__ = 'cleaners'

    id = db.Column(db.String(50), primary_key=True, default= generate_uuid())
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(40))
    department_id = db.Column(db.String(40), db.ForeignKey('department.id'))
    profile_photo = db.Column(db.String(40))

class Guard(db.Model):
    __tablename__ = 'guards'

    id = db.Column(db.String(50), primary_key=True, default= generate_uuid())
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(40))
    department_id = db.Column(db.String(40), db.ForeignKey('department.id'))
    profile_photo = db.Column(db.String(40))

class Cook(db.Model):
    __tablename__ = 'cooks'

    id = db.Column(db.String(50), primary_key=True, default= generate_uuid())
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(40))
    department_id = db.Column(db.String(40), db.ForeignKey('department.id'))
    profile_photo = db.Column(db.String(40))

class Receptionist(db.Model):
    __tablename__ = 'receptionists'

    id = db.Column(db.String(50), primary_key=True, default= generate_uuid())
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(40))
    department_id = db.Column(db.String(40), db.ForeignKey('department.id'))
    profile_photo = db.Column(db.String(40))

class Admin(db.Model):
    __tablename__ = 'admin'

    id = db.Column(db.String(36), db.ForeignKey('users.id'), primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    password = db.Column(db.String(50))


class Department(db.Model):

    __tablename__ = 'departments'

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid())
    name = db.Column(db.String(100))

class Service(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.String(50), primary_key=True, default= generate_uuid())
    name = db.Column(db.String(100))
    prices = db.Column(db.String(100))

class TokenBlocklist(db.Model):
    __tablename__ = 'tokenblocklist'
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, index=True)
    created_at = db.Column(db.DateTime, nullable=False)