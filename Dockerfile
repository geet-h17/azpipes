# Use OWASP Juice Shop as the base image
# FROM bkimminich/juice-shop
FROM ubuntu

# Install Python and Flask dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install flask

# Copy your Flask app to the container
COPY app.py /flask-app/app.py

# Expose an additional port for Flask
EXPOSE 5000

# Start both Juice Shop and Flask app
CMD /juice-shop/docker/start.sh & python3 /flask-app/app.py
