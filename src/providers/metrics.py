from google.cloud import monitoring_v3
import time

class MetricsProvider:
    def __init__(self, project_id):
        self.client = monitoring_v3.MetricServiceClient()
        self.project_path = f"projects/{project_id}"

    def report_ingestion(self, count, status="success"):
        series = monitoring_v3.TimeSeries()
        series.metric.type = "custom.googleapis.com/ingestion_count"
        series.metric.labels["status"] = status
        
        point = monitoring_v3.Point({
            "interval": {"end_time": {"seconds": int(time.time())}},
            "value": {"int64_value": count}
        })
        series.points = [point]
        self.client.create_time_series(name=self.project_path, time_series=[series])