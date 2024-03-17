# Ambient Weather API

The Ambient Weather API is a Flask-based web application that collects weather data from an Ambient Weather WS-2902D weather station and provides a simple API endpoint for retrieving weather metrics.

## Features

- Collects weather data from Ambient Weather WS-2902D weather station.
- Exposes a RESTful API endpoint for weather metrics retrieval.
- Easily deployable using Docker for containerization.
- Integrates with Prometheus for monitoring weather metrics.

## Updates

- Instructions for installing and configuring Prometheus have been added to README.md.
- Grafana dashboard template JSON file added to repo.

## Future Updates

- Add instructions for installing and configuring Grafana

## How It Works

The application uses Flask, a Python web framework, to create a lightweight web server. It communicates with the Ambient Weather WS-2902D weather station to collect weather data such as temperature, humidity, wind speed, and more. The collected data is then made available through a RESTful API endpoint `/weather` for external consumption.

### Prerequisites

- Python 3.x installed on your system
- Ambient Weather WS-2902D weather station connected and providing data
- Docker (optional, for containerized deployment)

## Clone Repository

   ```bash
   git clone https://github.com/your-username/ambient_weather_api.git
   cd ambient_weather_api

## Ambient Weather API Installation

Install and run locally:
1. Install Python dependencies using pip:
   ```bash
   pip3 install -r requirements.txt

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

## Prometheus Installation

1. Update Package Index:
   ```bash
   sudo apt update

2. Install Necessary Packages:
   ```bash
   sudo apt install curl tar

3. Download and Extract Prometheus:
   ```bash
   ## You can get the latest version of Prometheus from the official website.
   ## Replace `X.Y.Z` with the actual version number.

   PROM_VERSION="X.Y.Z"
   curl -LO "https://github.com/prometheus/prometheus/releases/download/v${PROM_VERSION}/prometheus-${PROM_VERSION}.linux-amd64.tar.gz"
   tar xvfz prometheus-${PROM_VERSION}.linux-amd64.tar.gz

4. Move Prometheus Files:
   ```bash
   sudo mv prometheus-${PROM_VERSION}.linux-amd64/prometheus /usr/local/bin/
   sudo mv prometheus-${PROM_VERSION}.linux-amd64/promtool /usr/local/bin/

5. Create Prometheus Configuration Directory:
   ```bash
   sudo mkdir /etc/prometheus

6. Create Prometheus Data Directory:
   ```bash
   sudo mkdir -p /var/lib/prometheus/data

7. Create Prometheus Configuration File:
   ```bash
   sudo nano /etc/prometheus/prometheus.yml

8. Add Contents to File:
   ```bash
   global:
     scrape_interval: 15s

   scrape_configs:
     - job_name: 'my_flask_app'
     static_configs:
       - targets: ['localhost:5000']

9. Set Permissions:
   ```bash
   sudo chown -R prometheus:prometheus /etc/prometheus /var/lib/prometheus

10. Create Prometheus Service File:
    ```bash
    sudo nano /etc/systemd/system/prometheus.service

11. Add Contents to File:
    ```bash
    [Unit]
    Description=Prometheus Monitoring System
    Wants=network-online.target
    After=network-online.target

    [Service]
    User=prometheus
    Group=prometheus
    Type=simple
    ExecStart=/usr/local/bin/prometheus \
      --config.file=/etc/prometheus/prometheus.yml \
      --storage.tsdb.path=/var/lib/prometheus/data

    [Install]
    WantedBy=multi-user.target

12. Reload systemd and Start Prometheus:
    ```bash
    sudo systemctl daemon-reload
    sudo systemctl start prometheus

13. Verify Prometheus Installation:
    Open Prometheus in your web browser by visiting `http://localhost:9090`. You should see the Prometheus web interface.

## Contributing

Contributions are welcome! If you have suggestions, feature requests, or bug reports, please open an issue or submit a pull request.
