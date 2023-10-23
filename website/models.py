from . import db
from website import create_app
from flask_login import UserMixin
# from sqlalchemy.sql import func
from itsdangerous import URLSafeSerializer as Serializer


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

