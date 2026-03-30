module "warehouse" {
  source     = "./modules/bigquery"
  project_id = var.project_id
  dataset_id = "dws_${var.DEPLOY_ENV}_warehouse"   # ← Make it dynamic
  env        = var.DEPLOY_ENV
}

module "storage" {
  source      = "./modules/storage"
  project_id  = var.project_id
  bucket_name = "${var.project_id}-ingestion-buffer-${var.DEPLOY_ENV}"   # ← Add env suffix
}

module "pubsub_ingestion" {
  source            = "./modules/pubsub"
  project_id        = var.project_id
  env               = var.DEPLOY_ENV
  topic_name        = "ingestion-topic-${var.DEPLOY_ENV}"
  subscription_name = "ingestion-sub-${var.DEPLOY_ENV}"
}