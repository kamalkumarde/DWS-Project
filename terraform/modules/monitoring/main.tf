resource "google_service_account" "grafana_sa" {
  account_id   = "grafana-viewer"
  display_name = "Grafana Metrics Viewer"
}

resource "google_project_iam_member" "grafana_metrics" {
  project = var.project_id
  role    = "roles/monitoring.viewer"
  member  = "service_account:${google_service_account.grafana_sa.email}"
}

# Generate a key to put into the Grafana UI
resource "google_service_account_key" "grafana_key" {
  service_account_id = google_service_account.grafana_sa.name
}