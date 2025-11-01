# Flask Application with Docker Testing

A simple Flask web application containerized with Docker.

## Quick Start

### Local
python -m venv venv
venv\Scripts\activate # Windows
pip install -r requirements.txt
python app.py
Open http://localhost:5000

### Docker
docker build -t flask-app:v1 .
docker run -d -p 5000:5000 flask-app:v1
Open http://localhost:5000

### Docker Hub
docker run -d -p 5000:5000 yourusername/flask-app:v1

## Routes
- `/` - Home page
- `/about` - About page

## Tech Stack
- Python 3.11
- Flask 3.0.0
- Docker