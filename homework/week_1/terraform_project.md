## Setting up Terraform
### Downloading and preparing necessary files and system config
- Copy and Extract Terraform Binary on my VM (You can use AWS, Azure or even Github Codespace instead of GCP)
- [Install gcloud CLI](https://cloud.google.com/sdk/docs/install). I find that it works if I choose "signed-by not supported" and "keyring not supported" option. I am running Ubuntu Server 20.04 LTS inside a VM.
- Copy the Service Account's private key to the VM then create an environment variable whose value is the file path.
- Run `gcloud auth application-default login` and proceed as instructed.

### Running terraform
- Copy the main.tf and variable.tf to the VM and edit as needed.
- Run `terraform init`
- Run `terraform plan`
- Run `terraform apply`

### Results of running
```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # google_bigquery_dataset.dataset will be created
  + resource "google_bigquery_dataset" "dataset" {
      + creation_time              = (known after apply)
      + dataset_id                 = "trips_data_all"
      + default_collation          = (known after apply)
      + delete_contents_on_destroy = false
      + etag                       = (known after apply)
      + id                         = (known after apply)
      + is_case_insensitive        = (known after apply)
      + labels                     = (known after apply)
      + last_modified_time         = (known after apply)
      + location                   = "us-west1"
      + max_time_travel_hours      = (known after apply)
      + project                    = "my-project-id"
      + self_link                  = (known after apply)
      + storage_billing_model      = (known after apply)
    }

  # google_storage_bucket.data-lake-bucket will be created
  + resource "google_storage_bucket" "data-lake-bucket" {
      + force_destroy               = true
      + id                          = (known after apply)
      + labels                      = (known after apply)
      + location                    = "US-WEST1"
      + name                        = "dtc_data_lake_my-project-id"
      + project                     = (known after apply)
      + public_access_prevention    = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + uniform_bucket_level_access = true
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type = "Delete"
            }
          + condition {
              + age                   = 30
              + matches_prefix        = []
              + matches_storage_class = []
              + matches_suffix        = []
              + with_state            = (known after apply)
            }
        }

      + versioning {
          + enabled = true
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

google_bigquery_dataset.dataset: Creating...
google_storage_bucket.data-lake-bucket: Creating...
google_bigquery_dataset.dataset: Creation complete after 1s [id=projects/my-project-id/datasets/trips_data_all]
google_storage_bucket.data-lake-bucket: Creation complete after 2s [id=dtc_data_lake_my-project-id]
```
