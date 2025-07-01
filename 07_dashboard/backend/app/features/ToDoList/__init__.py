from flask import Blueprint

todo_tracker_bp = Blueprint('todolist', __name__, url_prefix='/todo')