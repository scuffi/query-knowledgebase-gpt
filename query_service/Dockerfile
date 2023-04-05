# Pull the base image from tiangolo (since we are using FastAPI to write the API) from Docker Hub
FROM python:3.10-slim-buster

# Upgrade pip and install requirements.
COPY ./requirements.txt /server/requirements.txt
# COPY ./requirements.txt /server/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /server/requirements.txt

# Clean the install
RUN apt-get -y clean

# Copy all files to /app directory and move into directory.
COPY ./app /server/app
# COPY ./ /server

# Change the working directory to /authentication_service/app
WORKDIR /server/app

# Run the fast application
CMD ["python", "main.py"]