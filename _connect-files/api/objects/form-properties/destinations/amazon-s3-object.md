---
content-type: "api-form"
form-type: "destination"
key: "destination-form-properties-amazon-s3-object"

title: "Amazon S3 Destination Form Property"
api-type: "s3"
display-name: "Amazon S3"

docs-name: "amazon-s3"
db-type: "s3"

description: ""

uses-common-fields: false
object-attributes:
  - name: "s3_bucket"
    type: "string"
    required: true
    description: "The name of the {{ form-property.display-name }} bucket Stitch will write to."
    value: |
      "com-stitch-s3-bucket"

  - name: "output_file_format"
    type: "string"
    required: true
    description: |
      Defines the type of file Stitch will write to the bucket. Possible values are:

      - `csv`, which will use CSV (`.csv`) files
      - `json`, which will use JSON (`.jsonl`) files

      For examples of what data will look like in each format, refer to our [Amazon S3 documentation]({{ link.destinations.overviews.amazon-s3 | prepend: site.baseurl | append: "#data-storage-formats" }})

    value: |
      "csv"

  - name: "csv_delimiter"
    type: "string"
    required: true
    description: |
      Defines the delimiter used if `output_file_format` is `csv`.  Possible values are:

      - `,` (comma)
      - `|` (pipe)
      - `\t` (tab)
    value: |
      "|"

  - name: "csv_force_quote"
    type: "boolean"
    required: true
    description: |
      If `true`, Stitch will place all elements of key-value pairs in quotes when `output_file_format` is `csv`.

      For example: Numerical fields will appear as `"123"` instead of `123`.
    value: "true"

  - name: "s3_key_format_string"
    type: "string"
    required: true
    description: |
      Defines the naming convention Stitch should use when creating Object Keys. Object Keys are used to name tables when Stitch writes to the bucket.

      The required elements for an Object Key are:

      - `[integration_name]`
      - `[table_name]`
      - `[table_version]`
      - `[timestamp_loaded]`

      For more info on construcing an S3 Object Key, refer to our [Amazon S3 documentation]({{ link.destinations.setup.amazon-s3 | prepend: site.baseurl | append: "#define-s3-object-key" }}).
    value: |
      "[integration_name]/[table_name]/[table_version]_[timestamp_loaded].[output_file_format]"
---