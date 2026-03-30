terraform {
  required_version = ">= 1.7.0"

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 6.0"
    }
  }

  backend "gcs" {}
}

provider "google" {
  project = var.project_id
  region  = "us-central1"
}

module "warehouse" {
  source     = "./modules/bigquery"
  project_id = var.project_id
  dataset_id = "dws_${var.DEPLOY_ENV}_warehouse" # ← Make it dynamic
  env        = var.DEPLOY_ENV
}

module "storage" {
  source      = "./modules/storage"
  project_id  = var.project_id
  bucket_name = "${var.project_id}-ingestion-buffer-${var.DEPLOY_ENV}"

}
module "pubsub_ingestion" {
  source            = "./modules/pubsub"
  project_id        = var.project_id
  env               = var.DEPLOY_ENV
  topic_name        = "ingestion-topic-${var.DEPLOY_ENV}"
  subscription_name = "ingestion-sub-${var.DEPLOY_ENV}"
}
# Add more modules as needed, following the same pattern