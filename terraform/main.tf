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
  env               = var.env # This fixes Error 1
  topic_name        = "ingestion-topic-${var.env}"
  subscription_name = "ingestion-sub-${var.env}" # This fixes Error 2
}