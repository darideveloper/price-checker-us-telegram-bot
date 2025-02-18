# Use Python 3.12 slim image
FROM python:3.12-slim

# Env variables
ARG WEBHOOK
ARG PRICE_CHECKER_HOST
ARG PRICE_CHECKER_API_KEY
ARG DB_SERVER
ARG DB_DATABASE
ARG DB_USERNAME
ARG DB_PASSWORD
ARG DB_PORT

ENV WEBHOOK=$WEBHOOK
ENV PRICE_CHECKER_HOST=$PRICE_CHECKER_HOST
ENV PRICE_CHECKER_API_KEY=$PRICE_CHECKER_API_KEY
ENV DB_SERVER=$DB_SERVER
ENV DB_DATABASE=$DB_DATABASE
ENV DB_USERNAME=$DB_USERNAME
ENV DB_PASSWORD=$DB_PASSWORD
ENV DB_PORT=$DB_PORT

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app/

# Install system dependencies (e.g., for PostgreSQL support)
RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port that Flask will run on
EXPOSE 5000

# Run scripts
CMD ["python", "./scripts/set_webhook.py"]

# Command to run Flask in production with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]