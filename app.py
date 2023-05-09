from routes import main_bp
from routes.profile import profile_bp
from flask import Flask, render_template
import configparser

app = Flask(__name__)
app.config['CONFIG_PATH'] = '/home/nico/Documents/projects/trader/FreqInsight/config/config.ini'

app.register_blueprint(main_bp)
app.register_blueprint(profile_bp)

@app.route('/')
def home(message=None, output=None):
    return render_template('index.html', message=message, output=output)

if __name__ == '__main__':
    app.run(debug=True)
