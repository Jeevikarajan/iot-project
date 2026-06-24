import requests
import random
import time

URL = "https://iot-project-onab.onrender.com/sensor-data"

while True:
    data = {
        "device_id": f"sensor_{random.randint(1,3)}",
        "temperature": round(random.uniform(20, 40), 2),
        "humidity": round(random.uniform(40, 80), 2)
    }

    res = requests.post(URL, json=data)
    print(res.json())
    print("STATUS:", res.status_code)
    print("RESPONSE:", res.text)
    time.sleep(2)