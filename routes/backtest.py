from flask import Blueprint, render_template, jsonify
import os
import re

backtest_bp = Blueprint('backtest', __name__)

@backtest_bp.route('/backtest')
def backtest():
    print("Accessing backtest route")
    strategy_dir = '/home/nico/Documents/projects/trader/dev-freq/ft_userdata/user_data/strategies'
    strategy_files = []

    for file_name in os.listdir(strategy_dir):
        if file_name.endswith('.py'):
            with open(os.path.join(strategy_dir, file_name), 'r') as file:
                content = file.read()
                match = re.search(r'class\s+(\w+)\(', content)
                if match:
                    class_name = match.group(1)
                    strategy_files.append(class_name)

    print(strategy_files)

    return jsonify({'strategy_files': strategy_files})
from flask import Blueprint, render_template, jsonify
import os
import re

backtest_bp = Blueprint('backtest', __name__)

@backtest_bp.route('/backtest')
def backtest():
    print("Accessing backtest route")
    strategy_dir = '/home/nico/Documents/projects/trader/dev-freq/ft_userdata/user_data/strategies'
    strategy_files = []

    for file_name in os.listdir(strategy_dir):
        if file_name.endswith('.py'):
            with open(os.path.join(strategy_dir, file_name), 'r') as file:
                content = file.read()
                match = re.search(r'class\s+(\w+)\(', content)
                if match:
                    class_name = match.group(1)
                    strategy_files.append(class_name)

    print(strategy_files)

    return jsonify({'strategy_files': strategy_files})
