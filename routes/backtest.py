from flask import Blueprint, render_template, jsonify, request
import subprocess
import os
import re
import configparser

backtest_bp = Blueprint('backtest', __name__)

# Read the config.ini file
config = configparser.ConfigParser()
config.read('config/config.ini')
strategies_path = config.get('FREQTRADE', 'strategies_path')
user_data_path = config.get('FREQTRADE', 'user_data_path')

@backtest_bp.route('/backtest')
def backtest():
    print("Accessing backtest route")
    strategy_files = []

    for file_name in os.listdir(strategies_path):
        if file_name.endswith('.py'):
            with open(os.path.join(strategies_path, file_name), 'r') as file:
                content = file.read()
                match = re.search(r'class\s+(\w+)\(', content)
                if match:
                    class_name = match.group(1)
                    strategy_files.append(class_name)

    print(strategy_files)

    return jsonify({'strategy_files': strategy_files})


@backtest_bp.route('/run_backtest', methods=['POST'])
def run_backtest():
    strategy_name = request.form.get('strategy-select')
    command = f"docker compose run freqtrade backtesting --strategy {strategy_name} --dry-run-wallet 1000 --timeframe 1d --timerange 20230425-"
    print("Running backtest command:", command)
    result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=user_data_path)
    print(result.stdout)
    print(result.stderr)

    return jsonify({'result': result.stdout})
