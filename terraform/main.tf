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
module "ingestion_bus" {
  source     = "./modules/pubsub"
  project_id = var.project_id
  topic_name = "raw-events-stream"
  env        = var.env
}
