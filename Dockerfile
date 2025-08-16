FROM python:3.10-slim-buster

WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Expose the Flask port
EXPOSE 8080

# Run the Flask app
CMD ["python3", "app.py"]
