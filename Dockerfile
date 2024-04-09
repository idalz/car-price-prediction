FROM python:3.8-slim-buster

# Update package lists and install awscli
RUN apt update -y && \
    apt install awscli -y && \
    apt clean

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Command to run the application
CMD ["python3", "app.py"]