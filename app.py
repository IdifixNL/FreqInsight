# app.py
from config import __init__
from flask import Flask, render_template
from routes import main_bp
from flask import request

app = Flask(__name__)
app.register_blueprint(main_bp)

@app.route('/')
def home(message=None, output=None):
    return render_template('index.html', message=message, output=output)

if __name__ == '__main__':
    app.run(debug=True)




@app.route('/profile', methods=['POST'])
def profile():
    data = request.form['data']
    # process data here
    return 'Profile endpoint'