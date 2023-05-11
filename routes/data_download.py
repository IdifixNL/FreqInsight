from flask import Blueprint, request, render_template
import subprocess
import os
import configparser

data_download_bp = Blueprint('data_download', __name__)

config = configparser.ConfigParser()
config.read('config/config.ini')
user_data_path = config.get('FREQTRADE', 'user_data_path')

@data_download_bp.route('/download_data', methods=['POST'])
def download_data():
    command = ['docker', 'compose', 'run', 'freqtrade', 'download-data', '--days', '60', '-t', '1d']
    cwd = user_data_path
    process = subprocess.Popen(command, stdout=subprocess.PIPE, cwd=cwd)
    output, error = process.communicate()
    if error:
        return {'status': 'error', 'message': error.decode('utf-8')}
    return {'status': 'success', 'message': output.decode('utf-8')}

@data_download_bp.route('/datadownload')
def datadownload():
    return render_template('datadownload.html')
