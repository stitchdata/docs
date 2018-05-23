---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-salesforce-object"

title: "Salesforce Source Form Property"
description: "{{ api.form-properties.source-forms.salesforce.description }}"

object-attributes:
  - name: "api_type"
    type: "string"
    required: true
    description: "The Salesforce API Stitch should use to extract data. Possible values are `REST` or `BULK`. [Read about the pros and cons of each API here]({{ site.baseurl }}/integrations/saas/salesforce#bulk-vs-rest-api)."

  - name: "is_sandbox"
    type: "string"
    required: false
    description: "If `true`, the Salesforce account being connected is a sandbox."

  - name: "frequency_in_minutes"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]","Salesforce" }}

  - name: "anchor_time"
    type: "string"
    required: false
    description: |
      {{ connect.common.attributes.anchor-time }}

  - name: "quota_percent_per_run"
    type: "string"
    required: false
    description: "The maximum percentage of Salesforce API quota allowed per replication job."

  - name: "quota_percent_total"
    type: "string"
    required: false
    description: "The maximum percentage of Salesforce API quota allowed per day."

  - name: "select_fields_by_default"
    type: "string"
    required: true
    description: "If `true`, Stitch will automatically set new fields added in Salesforce to replicate."

  - name: "start_date"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.start-date | replace: "[INTEGRATION]","Salesforce" }}

examples:
  - code: |
      {  
       "type":"platform.salesforce",
       "properties":{
          "api_type":"BULK",
          "is_sandbox":"false",
          "frequency_in_minutes":"1440",
          "anchor_time":"",
          "quota_percent_per_run":"25",
          "quota_percent_total":"80",
          "select_fields_by_default":"true",
          "start_date":"2018-01-10T00:00:00Z"
        }
      }
---