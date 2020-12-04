from persona_api.db import db
from sqlalchemy_serializer import SerializerMixin


class Website(db.Model, SerializerMixin):
    __tablename__ = 'website'
    username = db.Column(db.String, db.ForeignKey('person.username'), primary_key=True, autoincrement=False)
    url = db.Column(db.String, primary_key=True, autoincrement=False)

    serialize_rules = ('-user',)