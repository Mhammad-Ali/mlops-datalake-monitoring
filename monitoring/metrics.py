# monitoring/metrics.py

metrics = {
    "records_processed_total": 0,
    "datalake_unavailable": 0,
    "feature_added": 0,
    "feature_removed": 0
}

def increment(metric_name, value=1):
    if metric_name not in metrics:
        metrics[metric_name] = 0
    metrics[metric_name] += value

def get_metrics():
    return metrics
