FROM python:3.8-alpine

# Create app directory
WORKDIR /usr/src/app

# Install system dependencies
RUN apk add --update --no-cache build-base \
    linux-headers pcre-dev

# Copy application code
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose port and run app
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
