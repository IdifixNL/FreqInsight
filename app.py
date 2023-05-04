# Import the necessary libraries
import subprocess
from flask import Flask, render_template, request, redirect, url_for

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

# Define the route for the backtest
@app.route('/backtest', methods=['POST'])
def backtest():
    # Define the command and working directory
    command = "docker-compose up -d"
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
        message = "Docker Compose command executed successfully."
        output = result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        message = "An error occurred while executing the Docker Compose command."
        output = e.stderr.decode('utf-8')

    return home(message=message, output=output)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
