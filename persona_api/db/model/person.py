from persona_api.db import db
from .location import Location
from .website import Website
from sqlalchemy_serializer import SerializerMixin


class Person(db.Model, SerializerMixin):
    __tablename__ = 'person'
    username = db.Column(db.String, primary_key=True, autoincrement=False)
    company = db.Column(db.String)
    ssn = db.Column(db.String)
    residence = db.Column(db.String)
    blood_group = db.Column(db.String)
    name = db.Column(db.String)
    sex = db.Column(db.String)
    address = db.Column(db.String)
    mail = db.Column(db.String)
    birthdate = db.Column(db.String)

    current_location = db.relationship('Location',
                                       backref='person',
                                       uselist=False,
                                       lazy="select",
                                       cascade="all, delete-orphan")
    website = db.relationship('Website',
                              backref='person',
                              uselist=True,
                              lazy="select",
                              cascade="all, delete-orphan")

    serialize_rules = ('-current_location.person', '-current_location.username')
    serialize_types = (
        (Location, lambda l: [l.latitude, l.longitude]),
        (Website, lambda w: w.url)
    )
