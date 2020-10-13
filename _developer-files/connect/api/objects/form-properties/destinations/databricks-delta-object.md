---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "destination"
key: "destination-form-properties-databricks-delta-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Databricks Delta Lake Destination Form Property"
api-type: "databricks_delta"
display-name: "Databricks Delta Lake"

docs-name: "databricks-delta"
db-type: "databricks-delta"

description: |
  To set up an {{ form-property.display-name }} destination, users will need to:

  1. Configure access for Stitch and Databricks to an existing Amazon S3 bucket
  2. Generate a Databricks REST API token
  3. Retrieve the Databricks' cluster JDBC URL

  Depending on your Amazon Web Services (AWS) configuration, you may need to perform additional steps to successfully connect this destination.

  Refer to our [{{ form-property.display-name }} documentation]({{ link.destinations.setup.databricks-delta | prepend: site.baseurl }}) for additional details.

property-description: "a {{ form-property.display-name }} destination via an Amazon S3 bucket"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-common-fields: false
uses-ssh-fields: false

object-attributes:
  - name: "access_token"
    type: "string"
    required: true
    read-only: false
    description: |
      A Databricks REST API access token. Refer to the [{{ form-property.display-name }} documentation]({{ link.destinations.setup.databricks-delta | append:"#generate-databricks-api-access-token" }}) for instructions on generating this credential.
    value: |
      "<ACCESS_TOKEN>"

  - name: "jdbc_url"
    type: "string"
    required: true
    read-only: false
    description: |
      The JDBC URL used to connect to your Databricks cluster. Refer to the [{{ form-property.display-name }} documentation]({{ link.destinations.setup.databricks-delta | append:"#retrieve-jdbc-url" }}) for instructions on retrieving this info.
    value: |
      "jdbc:spark://<server-hostname>:<port>/default;transportMode=http;ssl=1;httpPath=<http-path>;AuthMech=3;UID=token;PWD=<personal-access-token>"

  - name: "ssh_config"
    type: "object"
    required: true
    read-only: false
    description: |
      An object containing properties for configuring SSH encryption for the destination.
    value: |
      {
           "ssh":"true",
           "ssh_host":"your-ssh-server-address",
           "ssh_port":"22",
           "ssh_user":"stitch"
          }

    subattributes:
      - name: "ssh"
        type: "string"
        required: true
        read-only: false
        description: |
          Indicates whether SSH encryption should be used to connect to the destination. Valid values are:

          - `false` - No encryption will be used.
          - `true` - SSH encryption will be used to connect to the destination. The SSH connection details should be submitted using the `ssh_host`, `ssh_port`, and `ssh_user` properties.
        value: |
          "true"

      - name: "ssh_host"
        type: "string"
        required: false
        read-only: false
        description: |
          If using SSH encryption, the host of the SSH server. Required only if `ssh` is `true`.
        value: |
          "<SSH_HOST_ADDRESS>"

      - name: "ssh_port"
        type: "string"
        required: false
        read-only: false
        description: |
          If using SSH encryption, the port of the SSH server. Required only if `ssh` is `true`.
        value: |
          "22"

      - name: "ssh_user"
        type: "string"
        required: false
        read-only: false
        description: |
          If using SSH encryption, the name of the SSH user. Required only if `ssh` is `true`.
        value: |
          "<SSH_USERNAME>"

  - name: "staging_area"
    type: "object"
    required: true
    read-only: false
    description: |
      Connection information for the Amazon S3 bucket Stitch will stage data to before loading into {{ form-property.display-name }}.
    value: |
      {
           "scheme": "s3",
           "bucket_name": "<S3-BUCKET-NAME>"
          }
    subattributes:
      - name: "scheme"
        type: "string"
        required: true
        read-only: false
        description: "This will be `s3`."
        value: |
          "s3"

      - name: "bucket_name"
        type: "string"
        required: true
        read-only: false
        description: |
          The name of the Amazon S3 bucket.

          **Note**: This must be a pre-existing bucket. Refer to the [{{ form-property.display-name }} documentation]({{ link.destinations.setup.databricks-delta }}) for instructions on configuring access to the bucket for Stitch and {{ form-property.display-name }}.
        value: |
          "stitch-databricks-delta-bucket"
---