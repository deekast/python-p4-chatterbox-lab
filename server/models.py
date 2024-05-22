from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime 

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    body = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)


    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'body': self.body,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }





# "body": String.
# "username": String.
# "created_at": DateTime.
# "updated_at": DateTime.
# Don't forget to add default values for "created_at" and "updated_at"!
# (Hint - we discussed this in the Phase 3 Many-to-Many Relationships reading and gave an example in the Phase 4 Building a Get API Reading.)
