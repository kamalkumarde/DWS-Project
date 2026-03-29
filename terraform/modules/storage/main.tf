variable "project_id" {}
variable "bucket_name" {}
resource "google_storage_bucket" "lake" {
  name     = var.bucket_name
  location = "US"
  
  lifecycle_rule {
    condition { age = 30 }
    action { 
      type = "SetStorageClass"
      storage_class = "NEARLINE" 
    }
  }
  
  lifecycle_rule {
    condition { age = 90 }
    action { 
      type = "SetStorageClass"
      storage_class = "COLDLINE" 
    }
  }
}