# routes/__init__.py

from flask import Blueprint

# Create the blueprint objects
main_bp = Blueprint('main', __name__)
backtest_bp = Blueprint('backtest', __name__)

# Import the routes
from .about import about_routes
from .test import test_routes
from .profile import profile_bp
from .backtest import backtest_bp

# Register the blueprints
main_bp.register_blueprint(about_routes)
main_bp.register_blueprint(test_routes)
main_bp.register_blueprint(profile_bp)
main_bp.register_blueprint(backtest_bp)
