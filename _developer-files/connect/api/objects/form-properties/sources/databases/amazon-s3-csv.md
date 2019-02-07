---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-amazon-s3-csv-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Amazon S3 CSV Source Form Property"
api-type: "s3-csv"
display-name: "Amazon S3 CSV"

source-type: "database"
docs-name: "amazon-s3-csv"
db-type: "s3-csv"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-common-fields: false
uses-feature-fields: false

object-attributes:
  - name: "bucket"
    type: "string"
    required: true
    description: "The name of the bucket Stitch should replicate data from."
    value: "com-test-stitch-bucket"

  - name: "external_id"
    type: "string"
    required: true
    description: |
      The external ID associated with the Amazon Web Services (AWS) Identity Access Management (IAM) role used by Stitch.

      In AWS, external IDs are used to increase role security when granting access to accounts that you don't own or have administrative access to. Stitch will provide this ID when accessing {{ form-property.display-name }}.
    value: "stitch_connection_12345"

  - name: "role_name"
    type: "string"
    required: true
    description: |
      The name of the AWS IAM role Stitch should assume when extracting data from Amazon S3. This role will have the permissions in the IAM policy associated with the role.

      Refer to our [{{ form-property.display-name }} documentation]({{ doc-link | append: "#grant-access-bucket-iam" }}){:target="new"} for more info about the IAM policy, role, and how to create them in AWS.
    value: "<ROLE_NAME>"

# Commenting this out for now.
# The sources team is working on making this attribute
# More user-friendly.

  # - name: "tables"
  #   type: "string"
  #   required: true
  #   description: |
  #     [PLACEHOLDER]
  #   value: ""
---

