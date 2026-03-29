variable "project_id" {
  type        = string
  description = "The GCP Project ID"
}

variable "topic_name" {
  type        = string
  description = "Name of the Pub/Sub topic"
}

variable "env" {
  type        = string
  description = "Environment (dev/prod)"
}