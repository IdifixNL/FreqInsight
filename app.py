# app.py
from config import __init__
from flask import Flask, render_template
from routes import main_bp

app = Flask(__name__)
app.register_blueprint(main_bp)

@app.route('/')
def home(message=None, output=None):
    return render_template('index.html', message=message, output=output)

if __name__ == '__main__':
    app.run(debug=True)


