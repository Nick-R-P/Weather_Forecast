# Project Infrastructure
provider "google" {
  project = "weather-prediction"
  region  = "northamerica-northeast1"
  version = 
  provider = 
}

# Variables
locals{
  project_id   = "weather-prediction"
  region       = "northamerica-northeast1"
  zone         = "northamerica-northeast1-b"
  owner        = "nick-pavicic"
  snow_queue   = "am_aps_cloud"
}

#Service Account Roles
resource "google_project_iam_member" "bigquery_user_binding" {
  project = "weather-prediction"
  role    = "roles/bigquery.user"
  member  = "user:nr.pavicic@gmail.com"
}

resource "google_project_iam_member" "storage_owner_binding" {
  project = "weather-prediction"
  role    = "roles/storage.admin"
  member  = "user:nr.pavicic@gmail.com"
}

# Bigquery Datasets
resource "google_bigquery_dataset" "example_dataset" {
  dataset_id                  = "weather_prediction"
  project                     = "weather-prediction"
  location                    = local.region
}

# GCP Storage Buckets
# Create a Cloud Storage bucket
resource "google_storage_bucket" "weather_bucket" {
  name     = "weather_bucket"
  location = local.region
  project  = local.project_id
}