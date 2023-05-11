FROM python:3.8

WORKDIR /app

# Install Git
RUN apt-get update && \
    apt-get install -y git

# Clone the repository and switch to the latest branch
RUN git clone https://github.com/IdifixNL/FreqInsight.git . && \
    git checkout migrate/flask && \
    git pull

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
