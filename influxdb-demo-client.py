import time
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

# Token för InfluxDB
token = "EghXfkhCaa_1KN6GjVv66dTgqmVfrBZUfIviHnOrWn_DEbIPdsNCJSokO98Og5lQvxAxHGmpMaRH6aeFrztbpw=="

# Inställningar för InfluxDB
url = "http://influxdb:8086"
org = "my-org"
bucket = "battery_data"

# Skapa klient för InfluxDB
client = InfluxDBClient(url=url, token=token, org=org)

# Skapa Write API
write_api = client.write_api(write_options=SYNCHRONOUS)

# Skapa och skicka testdata
for i in range(10):
    battery_level = 100 - i * 5  # Exempel på batterinivå
    point = Point("battery_measurement")\
        .tag("device", "sensor_1")\
        .field("battery_level", battery_level)\
        .time(time.time_ns())
    
    # Skicka data till InfluxDB
    write_api.write(bucket=bucket, org=org, record=point)
    
    print(f"Skickade batterinivå: {battery_level}%")
    time.sleep(5)  # Vänta 5 sekunder mellan varje datapunkt

# Stäng klienten
client.close()