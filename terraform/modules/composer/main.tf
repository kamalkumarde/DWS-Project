resource "google_service_account" "composer_sa" {
  account_id   = "composer-worker-sa"
  display_name = "Airflow Service Account"
}

resource "google_composer_environment" "airflow" {
  name   = "dws-orchestrator"
  region = var.region

  config {
    software_config {
      image_version = "composer-2.1.0-airflow-2.3.3"
    }
    node_config {
      service_account = google_service_account.composer_sa.email
    }
  }
}

# IAM: Give Composer permission to read GCS and write to BigQuery
resource "google_project_iam_member" "composer_gcs" {
  project = var.project_id
  role    = "roles/storage.objectViewer"
  member  = "service_account:${google_service_account.composer_sa.email}"
}

resource "google_project_iam_member" "composer_bq" {
  project = var.project_id
  role    = "roles/bigquery.dataEditor"
  member  = "service_account:${google_service_account.composer_sa.email}"
}