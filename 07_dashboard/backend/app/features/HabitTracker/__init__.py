from flask import Blueprint

habit_tracker_bp = Blueprint('habits', __name__, url_prefix='/habits')