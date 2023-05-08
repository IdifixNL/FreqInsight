# routes/about.py

from flask import Blueprint

about_routes = Blueprint('about', __name__)

@about_routes.route('/about')
def about():
    return "This is the About page."
