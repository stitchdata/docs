---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-amazon-s3-csv-object"

title: "Amazon S3 CSV Source Form Property"
description: |
  {{ api.form-properties.source-forms.amazon-s3-csv.description }}

object-attributes:
  - name: "anchor_time"
    type: "string"
    required: false
    description: "{{ connect.common.attributes.anchor-time }}"
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
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]","Amazon S3 CSV" }}
    value: "{{ sample-property-data.frequency }}"

  - name: "start_date"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.start-date | replace: "[INTEGRATION]","Amazon S3 CSV" }}
    value: "{{ sample-property-data.start-date }}"

  - name: "tables"
    type: "string"
    required: true
    description: |
      [PLACEHOLDER]
    value: ""


examples: 
  - code: |
      {  
       "type":"platform.s3-csv",
       "properties":{
          "anchor_time":"",
          "bucket":"com-test-stitch-bucket",
          "frequency_in_minutes":"1440",
          "start_date":"2018-01-10T00:00:00Z",
          "tables":""
        }
      }
---