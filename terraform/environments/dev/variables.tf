variable "project_id" {
  description = "The GCP Project ID where the 1 PB platform resides"
  type        = string
}

variable "region" {
  description = "The GCP region for high-throughput ingestion"
  type        = string
  default     = "us-central1"
}
variable "env" {
  type        = string
  default     = "dev"
}