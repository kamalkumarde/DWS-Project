variable "project_id" {
  description = "The GCP Project ID"
  type        = string
}

variable "bucket_name" {
  description = "Name of the storage bucket"
  type        = string
}

variable "deploy_env" {
  description = "Environment (dev or prod)"
  type        = string
}