import os
import configparser

config_path = os.path.join(os.path.dirname(__file__), 'config.ini')

if not os.path.exists(config_path):
    config = configparser.ConfigParser()
    config.add_section('Settings')
    config.set('Settings', 'freqtrade_config_path', '/path/to/freqtrade/config.json')
    with open(config_path, 'w') as config_file:
        config.write(config_file)

config = configparser.ConfigParser()
config.read(config_path)

freqtrade_config_path = config.get('Settings', 'freqtrade_config_path')
user_data_path = config.get('Settings', 'user_data_path')
strategies_path = config.get('Settings', 'strategies_path')