---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/connect-templates/destination-form-property/
## FOR INSTRUCTIONS & REFERENCE INFO


# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-ga360-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Google Analytics 360 Source Form Property"
api-type: "platform.ga360"
display-name: "Google Analytics 360"

source-type: "saas"
docs-name: "google-analytics-360"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

# Only source-specific attributes need to be listed here.
# The following attributes are considered common,
# and therefore don't need to be listed:
# anchor_time, cron_expression, frequency_in_minutes, image_version, start_date 

object-attributes:
  - name: "dataset_id"
    type: "string"
    required: true
    description: |
      The ID of a dataset within your {{ form-property.display-name }} project. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#retrieve-project-dataset-ids" }}) for instructions on obtaining this information
    value: "<YOUR_DATASET_ID>"

  - name: "page_size"
    type: "string"
    required: false
    description: "This is an internal field for Stitch use."
    value: "<PAGE_SIZE>"
    
  - name: "project_id"
    type: "string"
    required: true
    description: |
      The ID of the project where your dataset lives. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#retrieve-project-dataset-ids" }}) for instructions on obtaining this information.
    value: "<YOUR_PROJECT_ID>"
    
  - name: "service_account_json"
    type: "string"
    required: true
    description: |
      Details and credentials for the Google Cloud Platform (GCP) IAM service account Stitch will use to replicate data.

      This data is generated when a [JSON project key file](https://cloud.google.com/iam/docs/creating-managing-service-account-keys){:target="new"} is created for the service account using the GCP Console. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#create-gcp-iam-service-account" }}) for instructions on obtaining this credential.
    value: |
      {
           "type": "service_account",
           "project_id": "<YOUR_PROJECT_ID>",
           "private_key_id": "<PRIVATE_KEY_ID>",
           "private_key": "-----BEGIN PRIVATE KEY-----<PRIVATE_KEY>-----END PRIVATE KEY-----",
           "client_email": "<EMAIL>@<PROJECT_ID>.iam.gserviceaccount.com",
           "client_id": "<CLIENT_ID>",
           "auth_uri": "https://accounts.google.com/o/oauth2/auth",
           "token_uri": "https://accounts.google.com/o/oauth2/token",
           "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
           "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/<SERVICE_ACCOUNT_EMAIL>"
          }
---