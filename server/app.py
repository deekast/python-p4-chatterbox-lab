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
# POST /messages: creates a new message with a body and username from params, and returns the newly created post as JSON.
# PATCH /messages/<int:id>: updates the body of the message using params, and returns the updated message as JSON.
# DELETE /messages/<int:id>: deletes the message from the database.

@app.get('/messages')
def messages():
    messages = Message.query.order_by(Message.created_at.asc()).all()
    return [m.to_dict() for m in messages], 200

@app.route('/messages/<int:id>')
def messages_by_id(id):
    return ''

if __name__ == '__main__':
    app.run(port=5555)
