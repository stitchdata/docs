---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-amazon-s3-csv-object"

title: "Amazon S3 CSV Source Form Property"
api-type: "s3-csv"
display-name: "Amazon S3 CSV"
integration-type: "database"
docs-name: "amazon-s3-csv"

description: |
  {{ api.form-properties.source-forms.amazon-s3-csv.description }}

object-attributes:
  - name: "anchor_time"
    type: "string"
    required: false
    description: |
      {{ connect.common.attributes.anchor-time | replace: "[INTEGRATION]",form-property.display-name }}
    value: "{{ sample-property-data.anchor-time }}"

  - name: "bucket"
    type: "string"
    required: true
    description: "The name of the bucket Stitch should replicate data from."
    value: "com-test-stitch-bucket"

  - name: "frequency_in_minutes"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]",form-property.display-name }}
    value: "{{ sample-property-data.frequency }}"

  - name: "start_date"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.start-date | replace: "[INTEGRATION]",form-property.display-name}}
    value: "{{ sample-property-data.start-date }}"

  - name: "tables"
    type: "string"
    required: true
    description: |
      [PLACEHOLDER]
    value: ""
---