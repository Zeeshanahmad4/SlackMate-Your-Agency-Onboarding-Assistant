# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable for Slack API Token (Should be overridden at runtime)
ENV SLACK_API_TOKEN=your_slack_api_token_here

# Run main.py when the container launches
CMD ["python", "src/main.py"]
