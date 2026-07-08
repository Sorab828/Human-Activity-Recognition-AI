import requests
import time

PHONE_IP = "192.168.29.182"
BASE_URL = f"http://{PHONE_IP}:8080"

print("Connected to phyphox...")

while True:
    try:
        r = requests.get(BASE_URL, timeout=2)
        print("Connected! Status:", r.status_code)
        break
    except Exception as e:
        print("Waiting for phyphox...", e)
        time.sleep(2)