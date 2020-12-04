from persona_api.db import db
from sqlalchemy_serializer import SerializerMixin


class Location(db.Model, SerializerMixin):
    __tablename__ = 'location'
    username = db.Column(db.String, db.ForeignKey('person.username'), primary_key=True, autoincrement=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    serialize_rules = ('-user',)
