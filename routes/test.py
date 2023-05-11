# routes/test.py

import subprocess
import json
from flask import Blueprint, jsonify

test_routes = Blueprint('test', __name__)

@test_routes.route('/test', methods=['POST'])
def test():
    # Define the command and working directory
    command = "docker compose ps --format json"
    working_directory = "/home/nico/Documents/projects/trader/dev-freq/ft_userdata"

    # Run the command and capture the output
    try:
        result = subprocess.run(
            command.split(),
            cwd=working_directory,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        message = "Test command executed successfully."
        output = result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        message = "An error occurred while executing the Test command."
        output = e.stderr.decode('utf-8')

    # Parse the JSON output and extract the desired information
    try:
        containers = json.loads(output)
        name = ""
        state = ""
        for container in containers:
            if container["Name"] == "freqtrade":
                name = container["Name"]
                state = container["State"]
                break
    except json.JSONDecodeError:
        name = "Error"
        state = "Invalid JSON output. Raw output: " + output

    return jsonify({'message': message, 'name': name, 'state': state, 'raw_output': output})
