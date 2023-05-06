# Import the necessary libraries
import subprocess
import json
from flask import Flask, render_template, request, redirect, url_for, jsonify

# Create the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home(message=None, output=None):
    return render_template('index.html', message=message, output=output)

# Define the route for the about page
@app.route('/about')
def about():
    return "This is the About page."

@app.route('/test', methods=['POST'])
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

    return {'message': message, 'name': name, 'state': state, 'raw_output': output}

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
