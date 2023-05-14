from flask import Blueprint, render_template, jsonify, request
import subprocess
import os
import re
import configparser
#xz
backtest_bp = Blueprint('backtest', __name__)

config = configparser.ConfigParser()
config.read('config/config.ini')
strategies_path = config.get('FREQTRADE', 'strategies_path')
user_data_path = config.get('FREQTRADE', 'user_data_path')

@backtest_bp.route('/backtest')
def backtest():
    strategy_files = []

    for file_name in os.listdir(strategies_path):
        if file_name.endswith('.py'):
            with open(os.path.join(strategies_path, file_name), 'r') as file:
                content = file.read()
                match = re.search(r'class\s+(\w+)\(', content)
                if match:
                    class_name = match.group(1)
                    strategy_files.append(class_name)

    return jsonify({'strategy_files': strategy_files})


@backtest_bp.route('/run_backtest', methods=['POST'])
def run_backtest():
    strategy_name = request.form.get('strategy-select')
    time_frames = request.form.getlist('time_frames[]')
    timerange = request.form.get('timerange')

    print("Selected Time Frames:", time_frames)
    print("Timerange:", timerange)

    time_frames_str = ",".join(time_frames)

    command = ['docker', 'compose', 'run', 'freqtrade', 'backtesting', '--strategy', strategy_name, '--dry-run-wallet', '1000', '--timeframe', time_frames_str]

    if timerange and timerange.strip() != "":
        command.extend(['--timerange', timerange])

    process = subprocess.Popen(command, stdout=subprocess.PIPE, cwd=user_data_path)
    output, error = process.communicate()

    if error:
        response = {'status': 'error', 'message': error.decode('utf-8')}
    else:
        response = {'status': 'success', 'message': output.decode('utf-8')}

    return jsonify(response)


