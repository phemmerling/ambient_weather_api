# This repository will not be maintained whatsoever.

# Ambient Weather API

The Ambient Weather API is a Flask-based web application that collects weather data from an Ambient Weather WS-2902D weather station and provides a simple API endpoint for retrieving weather metrics.

## Features

- Collects weather data from Ambient Weather WS-2902D weather station.
- Exposes a RESTful API endpoint for weather metrics retrieval.
- Easily deployable using Docker for containerization.
- Integrates with Prometheus for monitoring weather metrics.

## How It Works

The application uses Flask, a Python web framework, to create a lightweight web server. It communicates with the Ambient Weather WS-2902D weather station to collect weather data such as temperature, humidity, wind speed, and more. The collected data is then made available through a RESTful API endpoint `/weather` for external consumption.

## Installation

Install and run locally:
1. Install Python dependencies using pip:
   ```bash
   pip install -r requirements.txt

2. Start the Flask application locally:
   ```bash
   python app.py

Install using Docker (optional)
1. Build the Docker image:
   ```bash
   docker build -t ambient-weather-api .

2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 ambient-weather-api

### Prerequisites

- Python 3.x installed on your system
- Ambient Weather WS-2902D weather station connected and providing data
- Docker (optional, for containerized deployment)

### Clone Repository

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ambient_weather_api.git
   cd ambient_weather_api
