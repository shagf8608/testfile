import time
import requests
import random  # Simulates sensor data for testing

# Replace with your server's IP address or hostname
SERVER_URL = "http://192.168.1.100:5000/data"

def get_sensor_data():
    # Replace this with actual sensor data reading logic
    temperature = random.uniform(20, 30)  # Example: Simulating a temperature sensor
    return {"temperature": temperature}

def send_data_to_server(data):
    try:
        response = requests.post(SERVER_URL, json=data)
        if response.status_code == 200:
            print("Data sent successfully:", data)
        else:
            print("Failed to send data. Server responded with:", response.status_code)
    except Exception as e:
        print("Error sending data:", e)

while True:
    sensor_data = get_sensor_data()
    send_data_to_server(sensor_data)
    time.sleep(5)  # Adjust the interval as needed
