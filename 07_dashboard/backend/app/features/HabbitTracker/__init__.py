from flask import Blueprint

habit_tracker_bp = Blueprint('habit', __name__, url_prefix='/habit')