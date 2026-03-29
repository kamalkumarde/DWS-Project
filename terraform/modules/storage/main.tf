variable "project_id" {}
variable "bucket_name" {}

resource "google_storage_bucket" "bucket" {
  project                     = var.project_id
  name                        = var.bucket_name
  location                    = "US"
  uniform_bucket_level_access = true
}
