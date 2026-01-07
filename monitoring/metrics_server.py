from fastapi import FastAPI
from monitoring.metrics import get_metrics

app = FastAPI()

@app.get("/metrics")
def metrics():
    metrics_data = get_metrics()
    output = []

    for key, value in metrics_data.items():
        output.append(f"{key} {value}")

    return "\n".join(output)
