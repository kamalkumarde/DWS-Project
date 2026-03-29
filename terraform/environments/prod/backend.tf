terraform {
  backend "gcs" {
    bucket = "dws-tf-state-20260329" # Use the name from Step 1
    prefix = "terraform/state/dev"
  }
}