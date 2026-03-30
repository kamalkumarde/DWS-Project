resource "google_storage_bucket" "lake" {
  name     = var.bucket_name
  project  = var.project_id
  location = "US"

  # Use the passed variable (not var.DEPLOY_ENV)
  force_destroy = var.deploy_env == "dev" ? true : false

  lifecycle_rule {
    condition { age = 30 }
    action {
      type          = "SetStorageClass"
      storage_class = "NEARLINE"
    }
  }

  lifecycle_rule {
    condition { age = 90 }
    action {
      type          = "SetStorageClass"
      storage_class = "COLDLINE"
    }
  }
}