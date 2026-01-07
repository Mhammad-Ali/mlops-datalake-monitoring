# ingestion/fetch_records.py

import time
import requests
from monitoring.metrics import increment, get_metrics
from ingestion.schema_tracker import track_schema

URL = "http://149.40.228.124:6500/records"
RETRY_DELAY = 5

def fetch_records():
    while True:
        try:
            response = requests.get(URL, timeout=5)

            if response.status_code == 200:
                data = response.json()

                records = data.get("records", [])
                for record in records:
                    track_schema(record)
                    increment("records_processed_total")

                print(f"✅ Processed {len(records)} records")
                print("📊 Metrics:", get_metrics())

            elif response.status_code == 503:
                print("⚠️ Data lake unavailable (503)")
                increment("datalake_unavailable")

            else:
                print(f"❌ Unexpected status code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print("❌ Request failed:", e)
            increment("datalake_unavailable")

        time.sleep(RETRY_DELAY)

if __name__ == "__main__":
    fetch_records()
