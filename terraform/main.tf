module "warehouse" {
  # If modules is at the same level as environments:
  source     = "./modules/bigquery"
  project_id = var.project_id
  dataset_id = "dws_dev_warehouse"
  env        = "dev"
}

module "storage" {
  source      = "./modules/storage"
  project_id  = var.project_id
  bucket_name = "${var.project_id}-ingestion-buffer"
}
module "pubsub_ingestion" {
  source            = "./modules/pubsub"
  project_id        = var.project_id
  env               = var.DEPLOY_ENV # Or var.env, matching your root variables.tf
  topic_name        = "ingestion-topic-${var.DEPLOY_ENV}"
  subscription_name = "ingestion-sub-${var.DEPLOY_ENV}"
}