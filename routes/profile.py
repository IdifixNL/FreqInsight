import configparser
import os
from flask import Blueprint, render_template, request

profile_bp = Blueprint('profile', __name__)

# Get the path of the config file
config_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'config.ini')


@profile_bp.route('/configuration')
def configuration():
    return render_template('configuration.html')


@profile_bp.route('/profiles', methods=['POST'])
def profiles_form():
    # Get the form data
    servername = request.form.get('servername')
    freqtrade_config_path = request.form.get('freqtrade_config_path')
    user_data_path = request.form.get('user_data_path')
    strategies_path = request.form.get('strategies_path')

    # Create a ConfigParser object and add the values to the 'Profile' section
    config = configparser.ConfigParser()
    config.read(config_path)
    section_name = 'Profile' + str(len(config.sections()) + 1)
    config.add_section(section_name)
    config.set(section_name, 'servername', servername)
    config.set(section_name, 'freqtrade_config_path', freqtrade_config_path)
    config.set(section_name, 'user_data_path', user_data_path)
    config.set(section_name, 'strategies_path', strategies_path)

    # Write the changes to the config file
    with open(config_path, 'w') as config_file:
        config.write(config_file)

    return {'result': 'success'}
