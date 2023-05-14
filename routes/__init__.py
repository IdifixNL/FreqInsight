# routes/__init__.py

from flask import Blueprint

# Create the blueprint object
main_bp = Blueprint('main', __name__)

# Import the routes
from .about import about_routes
from .test import test_routes
from .profile import profile_bp

# Register the blueprints
main_bp.register_blueprint(about_routes)
main_bp.register_blueprint(test_routes)
main_bp.register_blueprint(profile_bp)
