FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files into the container
COPY . .

# Expose the port that the app will run on
EXPOSE 5000

# Set the command to run when the container starts
CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app", "--workers", "4", "--threads", "2"]
