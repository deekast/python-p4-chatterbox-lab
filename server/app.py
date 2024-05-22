from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)


# GET /messages: returns an array of all messages as JSON, ordered by created_at in ascending order.
@app.get('/messages')
def get_all_messages():
    messages = Message.query.order_by(Message.created_at.asc()).all()
    return [m.to_dict() for m in messages], 200


# POST /messages: creates a new message with a body and username from params, and returns the newly created post as JSON.
@app.post('/messages')
def post_message():
    message = Message(
        body=request.json.get('body'),
        username=request.json.get('username')
    )

    db.session.add(message)
    db.session.commit()

    return message.to_dict(), 201


# PATCH /messages/<int:id>: updates the body of the message using params, and returns the updated message as JSON.

@app.patch('/messages/<int:id>')
def patch_message(id):
    message = Message.query.where(Message.id == id).first()

    if message:
        for key in request.json.keys():
            setattr(message, key, request.json[key])
        db.session.add(message)
        db.session.commit()
        return message.to_dict(), 202

    else:
        return { 'error': 'Not found' }, 404
    
# DELETE /messages/<int:id>: deletes the message from the database.
@app.delete('/messages/<int:id>')
def delete_message(id):
    message = Message.query.where(Message.id == id).first()

    if message:
        db.session.delete(message)
        db.session.commit()
        return {}, 204
    else:
        return { 'error': 'Not found' }, 404





if __name__ == '__main__':
    app.run(port=5555)
