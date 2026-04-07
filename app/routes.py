from flask import Blueprint, render_template, request, jsonify
from .utils import format_response
from .chat import ChatManager

main = Blueprint('main', __name__)

chat_manager = ChatManager()

@main.route('/')
def index():
    return render_template('chat.html')


@main.route('/api/chat', methods=['POST'])
def chat():
    data = request.json

    user_message = data.get('message')
    model = data.get('model')

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    # Pass model to ChatManager
    ai_response = chat_manager.get_response(user_message, model=model)

    formatted_response = format_response(ai_response)

    return jsonify({"response": formatted_response})