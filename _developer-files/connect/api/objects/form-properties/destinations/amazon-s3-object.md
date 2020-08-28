---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "destination"
key: "destination-form-properties-amazon-s3-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Amazon S3 Destination Form Property"
api-type: "s3"
display-name: "Amazon S3"

docs-name: "amazon-s3"
db-type: "s3"

property-description: |
  an {{ form-property.display-name }} bucket

description: |
  To set up an {{ form-property.display-name }} destination, users will need to:

  1. Create a bucket policy that grants Stitch permission to write to the bucket
  2. Create a "challenge file" in the bucket that allows Stitch to test the connection

  Refer to our [Amazon S3 documentation]({{ link.destinations.setup.amazon-s3 | prepend: site.baseurl | append: "#grant-verify-bucket-access" }}) for additional details.


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-common-fields: false
object-attributes:
  - name: "s3_bucket"
    type: "string"
    required: true
    read-only: false
    description: "The name of the {{ form-property.display-name }} bucket Stitch will write to."
    value: |
      "com-stitch-s3-bucket"

  - name: "sentinel_key"
    type: "string"
    required: true
    read-only: false
    description: |
      The sentinel key is the name the challenge file in the bucket must have. The challenge file is a blank file that Stitch uses to test the permissions for the bucket. **Note**: The API treats this property as a credential, which means it won't be returned in responses.

      This file:

      - Must have a name that begins with `stitch-challenge-file-`. For example: `stitch-challenge-file-af295ad1-7a4b-4881-89dc-c9be27de13a5` 
      - Must remain in the bucket even after the inital setup is complete

      Refer to our [Amazon S3 documentation]({{ link.destinations.setup.amazon-s3 | prepend: site.baseurl | append: "#verify-bucket-access" }}) for additional details.
    value: |
      "stitch-challenge-file-af295ad1-7a4b-4881-89dc-c9be27de13a5"

  - name: "output_file_format"
    type: "string"
    required: true
    read-only: false
    description: |
      Defines the type of file Stitch will write to the bucket. Possible values are:

      - `csv`, which will use CSV (`.csv`) files
      - `jsonl`, which will use JSON (`.jsonl`) files

      For examples of what data will look like in each format, refer to our [Amazon S3 documentation]({{ link.destinations.overviews.amazon-s3 | prepend: site.baseurl | append: "#data-storage-formats" }}).
    value: |
      "csv"

  - name: "csv_delimiter"
    type: "string"
    required: false
    read-only: false
    description: |
      Defines the delimiter used if `output_file_format` is `csv`. Accepted values are:

      - `,` (comma)
      - `|` (pipe)
      - `\t` (tab)
    value: |
      "|"

  - name: "csv_force_quote"
    type: "string"
    required: false
    read-only: false
    description: |
      If `true`, Stitch will place all elements of key-value pairs in quotes when `output_file_format` is `csv`.

      For example: Numerical fields will appear as `"123"` instead of `123`.
    value: "true"

  - name: "s3_key_format_string"
    type: "string"
    required: true
    read-only: false
    description: |
      Defines the naming convention Stitch should use when creating Object Keys. Object Keys are used to name tables when Stitch writes to the bucket.

      The required elements for an Object Key are:

      - `[integration_name]`
      - `[table_name]`
      - `[table_version]`
      - `[timestamp_loaded]`

      For more info on construcing an S3 Object Key, refer to our [Amazon S3 documentation]({{ link.destinations.setup.amazon-s3 | prepend: site.baseurl | append: "#define-s3-object-key" }}).
    value: |
      "[integration_name]/[table_name]/[table_version]_[timestamp_loaded].<csv|json>"
---