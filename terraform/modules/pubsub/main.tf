resource "google_pubsub_topic" "name" {
  name    = var.topic_name
  project = var.project_id

  labels = {
    env = var.env
  }
}
resource "google_pubsub_subscription" "name" {
  name    = var.subscription_name
  topic   = google_pubsub_topic.name.id
  project = var.project_id

  labels = {
    env = var.env
  }
  message_retention_duration = "600s"
  retain_acked_messages      = false
  ack_deadline_seconds       = 20
}   