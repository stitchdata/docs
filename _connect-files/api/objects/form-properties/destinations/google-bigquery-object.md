---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-form"
form-type: "destination"
key: "destination-form-properties-google-bigquery-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Google BigQuery Destination Form Property"
api-type: "bigquery_v2"
display-name: "Google BigQuery"

docs-name: "bigquery"
db-type: "bigquery"

description: |
  To set up a {{ form-property.display-name }} destination, users will need to:

  1. Create a Google Cloud Platform IAM service account
  2. Generate a JSON project key file

  Refer to our [{{ form-property.display-name }} documentation]({{ link.destinations.setup.bigquery | prepend: site.baseurl }}) for additional details.


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-common-fields: false
object-attributes:
  - name: "cloud_storage_location"
    type: "string"
    required: true
    read-only: false
    description: |
      The Google Cloud Storage (GCS) region to be used during the replication process. This setting determines the region of the internal GCS storage bucket Stitch will use to load data into {{ form-property.display-name }}.

      Accepted values are:

      {% for region in site.data.destinations.reference.bigquery.v2.region-list %}
      - {{ region.name | replace_regex: "^[^(]*","" | remove: "(" | remove: ")" | markdownify }}
      {% endfor %}
    value: |
      "US"

  - name: "loading_mode"
    type: "string"
    required: true
    read-only: false
    description: |
      Determines how Stitch handles changes to existing records when loading data into {{ form-property.display-name }}. **Note**: This value cannot be modified after the destination is created.

      Accepted values are:

      - `UPSERT`: Existing rows will be updated with the most recent version of the record from the source. With this option, only the most recent version of a record will exist in {{ form-property.display-name }}.

      - `APPEND_ONLY`: Existing rows aren’t updated. Newer versions of existing records are added as new rows to the end of tables. With this option, many versions of the record will exist in {{ form-property.display-name }}, capturing how a record changed over time.

      Refer to the [todo documentation]() for more info and examples.
    value: |
      "UPSERT"

  - name: "service_account_credentials"
    type: "object"
    required: true
    read-only: false
    description: |
      Details and credentials for the Google Cloud Platform (GCP) IAM service account Stitch will use to load data into {{ form-property.display-name }} from Google Cloud Storage (GCS).

      This data is generated when a [JSON project key file](https://cloud.google.com/iam/docs/creating-managing-service-account-keys){:target="new"} is created for the service account using the GCP Console. Refer to [todo]() for more info and instructions.
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

    subattributes:
      - name: "type"
        type: "string"
        required: true
        read-only: false
        description: "This will be `service_account`."
        value: |
          "service_account"

      - name: "project_id"
        type: "string"
        required: true
        read-only: false
        description: "The ID of the project associated with the service account."
        value: |
          "<PROJECT_ID>"

      - name: "private_key_id"
        type: "string"
        required: true
        read-only: false
        description: "The ID of the private key."
        value: |
          "23sdiljasd29023908sdjlasdjasdf12be"

      - name: "private_key"
        type: "string"
        required: true
        read-only: false
        description: "The private key for the service account."
        value: |
          "-----BEGIN PRIVATE KEY-----<PRIVATE_KEY>-----END PRIVATE KEY-----"

      - name: "client_email"
        type: "string"
        required: true
        read-only: false
        description: "The service account email address."
        value: |
          "<EMAIL>@<PROJECT_ID>.iam.gserviceaccount.com"

      - name: "client_id"
        type: "string"
        required: true
        read-only: false
        description: "The client ID."
        value: |
          "<CLIENT_ID>"

      - name: "auth_uri"
        type: "string"
        required: true
        read-only: false
        description: "The auth URL for the service account."
        value: |
          "https://accounts.google.com/o/oauth2/auth"

      - name: "token_uri"
        type: "string"
        required: true
        read-only: false
        description: "The token URL for the service account."
        value: |
          "https://accounts.google.com/o/oauth2/token"

      - name: "auth_provider_x509_cert_url"
        type: "string"
        required: true
        read-only: false
        description: "The auth provider x509 cert URL for the service account."
        value: |
          "https://www.googleapis.com/oauth2/v1/certs"

      - name: "client_x509_cert_url"
        type: "string"
        required: true
        read-only: false
        description: "The client x509 cert URL for the service account."
        value: |
          "https://www.googleapis.com/robot/v1/metadata/x509/<SERVICE_ACCOUNT_EMAIL>"

  - name: "project_id"
    type: "string"
    required: true
    read-only: true
    description: |
      The ID of the project associated with the service account.
    value: |
      "<READ_ONLY_PROJECT_ID>"
---