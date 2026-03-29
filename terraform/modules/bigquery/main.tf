variable "project_id" {}
variable "dataset_id" {}
variable "env" {
  description = "The environment name (dev/prod)"
  type        = string
}

resource "google_bigquery_dataset" "dataset" {
  project    = var.project_id
  dataset_id = var.dataset_id
  location   = "US"
  lifecycle {
    prevent_destroy = true
  }
  labels = {
    environment = var.env
    data_tier   = "warehouse"
  }
}
