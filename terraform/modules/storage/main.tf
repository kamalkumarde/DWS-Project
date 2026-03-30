variable "project_id" {}
variable "bucket_name" {}

resource "google_storage_bucket" "lake" {
  name     = var.bucket_name
  project  = var.project_id          # ← Add this line (this fixes the error)
  location = "US"

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

  # Recommended additions
  force_destroy = true   # Helpful during development
}