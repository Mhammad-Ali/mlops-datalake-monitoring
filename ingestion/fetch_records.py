import requests
import time

URL = "http://149.40.228.124:6500/records"
RETRY_DELAY = 5  # seconds

while True:
    try:
        response = requests.get(URL, timeout=5)

        if response.status_code == 200:
            data = response.json()
            print("✅ Data lake available")
            print("Keys:", data.keys())
            break  # stop for now (we’ll loop later)

        elif response.status_code == 503:
            print("⚠️ Data lake unavailable (503). Retrying...")
            time.sleep(RETRY_DELAY)

        else:
            print("Unexpected status:", response.status_code)
            time.sleep(RETRY_DELAY)

    except requests.exceptions.RequestException as e:
        print("❌ Request failed:", e)
        time.sleep(RETRY_DELAY)
