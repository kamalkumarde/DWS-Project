variable "project_id" {}
variable "bucket_name" {}
resource "google_storage_bucket" "lake" {
  name          = var.bucket_name
  project       = var.project_id # ← Must have this
  location      = "US"
  force_destroy = var.DEPLOY_ENV == "dev" ? true : false # safer for prod

  lifecycle_rule {
    condition { age = 90 }
    action {
      type          = "SetStorageClass"
      storage_class = "COLDLINE"
    }
  }

  # Recommended additions

}