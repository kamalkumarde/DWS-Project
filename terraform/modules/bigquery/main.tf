variable "project_id" {}
variable "dataset_id" {}
variable "env" {
  description = "The environment name (dev/prod)"
  type        = string
}

resource "google_bigquery_dataset" "dataset" {
  dataset_id  = var.dataset_id
  project     = var.project_id # <--- ENSURE THIS LINE EXISTS
  location    = "US"
  description = "Warehouse for ${var.env} environment"

  #  Prevents accidental deletion of data
  delete_contents_on_destroy = false
}

