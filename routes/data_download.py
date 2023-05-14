from flask import Blueprint, request, render_template
import subprocess
import os
import configparser

data_download_bp = Blueprint('data_download', __name__)

# Read the config.ini file
config = configparser.ConfigParser()
config.read('config/config.ini')
user_data_path = config.get('FREQTRADE', 'user_data_path')

@data_download_bp.route('/download_data', methods=['POST'])
def download_data():
    data = request.json  # Expect JSON data
    days = data.get('days')
    time_frames = data.get('time_frames')
    print(f"Days: {days}, Time frames: {time_frames}")

    if not time_frames:
        return {'status': 'error', 'message': 'No time frames selected'}

    response = {}
    for time_frame in time_frames:
        command = ['docker', 'compose', 'run', 'freqtrade', 'download-data', '--days', days, '-t', time_frame]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, cwd=user_data_path)
        output, error = process.communicate()
        if error:
            response[time_frame] = {'status': 'error', 'message': error.decode('utf-8')}
        else:
            response[time_frame] = {'status': 'success', 'message': output.decode('utf-8')}

    return response




@data_download_bp.route('/datadownload')
def datadownload():
    return render_template('datadownload.html')
