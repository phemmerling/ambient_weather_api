import re
from flask import Flask, request
from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Define Prometheus metrics
temperature_indoor = Gauge('temperature_indoor', 'Indoor Temperature in Fahrenheit')
humidity_indoor = Gauge('humidity_indoor', 'Indoor Humidity in percentage')
barometer_relative_indoor = Gauge('barometer_relative_indoor', 'Relative Barometer Pressure Indoor')
barometer_absolute_indoor = Gauge('barometer_absolute_indoor', 'Absolute Barometer Pressure Indoor')
temperature_outdoor = Gauge('temperature_outdoor', 'Outdoor Temperature in Fahrenheit')
battery_outdoor = Gauge('battery_outdoor', 'Outdoor Battery Level')
humidity_outdoor = Gauge('humidity_outdoor', 'Outdoor Humidity in percentage')
wind_direction = Gauge('wind_direction', 'Wind Direction in Degrees')
wind_speed = Gauge('wind_speed', 'Wind Speed in mph')
wind_gust = Gauge('wind_gust', 'Wind Gust Speed in mph')
max_daily_gust = Gauge('max_daily_gust', 'Max Daily Wind Gust Speed in mph')
hourly_rain = Gauge('hourly_rain', 'Hourly Rainfall in inches')
event_rain = Gauge('event_rain', 'Event Rainfall in inches')
daily_rain = Gauge('daily_rain', 'Daily Rainfall in inches')
weekly_rain = Gauge('weekly_rain', 'Weekly Rainfall in inches')
monthly_rain = Gauge('monthly_rain', 'Monthly Rainfall in inches')
total_rain = Gauge('total_rain', 'Total Rainfall in inches')
solar_radiation = Gauge('solar_radiation', 'Solar Radiation in W/m^2')
uv_index = Gauge('uv_index', 'UV Index')
temperature_extra1 = Gauge('temperature_extra1', 'Extra Temperature Sensor 1 in Fahrenheit')
humidity_extra1 = Gauge('humidity_extra1', 'Extra Humidity Sensor 1 in percentage')
battery_extra1 = Gauge('battery_extra1', 'Extra Battery Level 1')
battery_co2 = Gauge('battery_co2', 'CO2 Sensor Battery Level')

# Define a regex pattern to extract metrics from the GET query string
pattern = re.compile(r'(\w+)=(\d+\.?\d*)')

@app.route('/weather', methods=['GET'])
def receive_weather_data():
    # Extract data from the query string in the GET request
    data = request.query_string.decode('utf-8')
    metrics = dict(re.findall(pattern, data))

    # Update Prometheus metrics
    temperature_indoor.set(float(metrics.get('tempinf', 0)))
    humidity_indoor.set(float(metrics.get('humidityin', 0)))
    barometer_relative_indoor.set(float(metrics.get('baromrelin', 0)))
    barometer_absolute_indoor.set(float(metrics.get('baromabsin', 0)))
    temperature_outdoor.set(float(metrics.get('tempf', 0)))
    battery_outdoor.set(float(metrics.get('battout', 0)))
    humidity_outdoor.set(float(metrics.get('humidity', 0)))
    wind_direction.set(float(metrics.get('winddir', 0)))
    wind_speed.set(float(metrics.get('windspeedmph', 0)))
    wind_gust.set(float(metrics.get('windgustmph', 0)))
    max_daily_gust.set(float(metrics.get('maxdailygust', 0)))
    hourly_rain.set(float(metrics.get('hourlyrainin', 0)))
    event_rain.set(float(metrics.get('eventrainin', 0)))
    daily_rain.set(float(metrics.get('dailyrainin', 0)))
    weekly_rain.set(float(metrics.get('weeklyrainin', 0)))
    monthly_rain.set(float(metrics.get('monthlyrainin', 0)))
    total_rain.set(float(metrics.get('totalrainin', 0)))
    solar_radiation.set(float(metrics.get('solarradiation', 0)))
    uv_index.set(float(metrics.get('uv', 0)))
    temperature_extra1.set(float(metrics.get('temp1f', 0)))
    humidity_extra1.set(float(metrics.get('humidity1', 0)))
    battery_extra1.set(float(metrics.get('batt1', 0)))
    battery_co2.set(float(metrics.get('batt_co2', 0)))

    return 'Weather data received successfully', 200

@app.route('/metrics', methods=['GET'])
def prometheus_metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
