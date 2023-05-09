import os
from flask import Blueprint, render_template, request, jsonify
import configparser

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile/', methods=['GET', 'POST'])
def configuration():
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the config.ini file
    config_path = os.path.join(current_dir, '..', 'config', 'config.ini')

    config = configparser.ConfigParser()
    config.read(config_path)

    if 'FREQTRADE' not in config:
        config['FREQTRADE'] = {}
    if 'SERVER' not in config:
        config['SERVER'] = {}

    if request.method == 'POST':
        data = request.get_json()
        config['FREQTRADE']['freqtrade_config_path'] = data.get('freqtrade_config_path', '')
        config['FREQTRADE']['user_data_path'] = data.get('user_data_path', '')
        config['FREQTRADE']['strategies_path'] = data.get('strategies_path', '')
        config['SERVER']['servername'] = data.get('servername', '')
        with open(config_path, 'w') as configfile:
            config.write(configfile)
        print('Config saved successfully.')
        print('freqtrade_config_path:', data.get('freqtrade_config_path', ''))
        print('user_data_path:', data.get('user_data_path', ''))
        print('strategies_path:', data.get('strategies_path', ''))
        print('servername:', data.get('servername', ''))
        return jsonify({"message": "Configuration saved successfully!"})

    freqtrade_config_path = config['FREQTRADE'].get('freqtrade_config_path', '')
    user_data_path = config['FREQTRADE'].get('user_data_path', '')
    strategies_path = config['FREQTRADE'].get('strategies_path', '')
    servername = config['SERVER'].get('servername', '')
    
    print('freqtrade_config_path:', freqtrade_config_path)
    print('user_data_path:', user_data_path)
    print('strategies_path:', strategies_path)
    print('servername:', servername)

    return render_template('configuration.html', freqtrade_config_path=freqtrade_config_path,
                           user_data_path=user_data_path, strategies_path=strategies_path,
                           servername=servername)
