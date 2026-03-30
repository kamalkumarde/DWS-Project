terraform {
  required_version = ">= 1.5.0"

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = "us-central1"
}

locals {
  env = lower(var.DEPLOY_ENV)
}

module "warehouse" {
  source     = "./modules/bigquery"
  project_id = var.project_id
  dataset_id = "dws_${local.env}_warehouse"
  env        = local.env
}

module "storage" {
  source      = "./modules/storage"
  project_id  = var.project_id
  bucket_name = "${var.project_id}-ingestion-buffer-${local.env}"
  deploy_env  = local.env
}

module "pubsub_ingestion" {
  source            = "./modules/pubsub"
  project_id        = var.project_id
  env               = local.env
  topic_name        = "ingestion-topic-${local.env}"
  subscription_name = "ingestion-sub-${local.env}"
}