---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-amazon-s3-csv-object"

title: "Amazon S3 CSV Source Form Property"
api-type: "s3-csv"
display-name: "Amazon S3 CSV"

source-type: "database"
docs-name: "amazon-s3-csv"
db-type: "s3-csv"

description: ""

uses-common-fields: false
object-attributes:
  - name: "bucket"
    type: "string"
    required: true
    description: "The name of the bucket Stitch should replicate data from."
    value: "com-test-stitch-bucket"

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