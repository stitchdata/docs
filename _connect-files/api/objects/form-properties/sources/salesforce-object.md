---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-salesforce-object"

title: "Salesforce"
description: "{{ api.form-properties.source-forms.salesforce.description }}"

object-attributes:
  - name: "api_type"
    type: "string"
    description: "The Salesforce API Stitch should use to extract data. Possible values are `REST` or `BULK`. [Read about the pros and cons of each API here]({{ site.baseurl }}/integrations/saas/salesforce#bulk-vs-rest-api)."

  - name: "is_sandbox"
    type: "string"
    description: "If `true`, the Salesforce account being connected is a sandbox."

  - name: "frequency_in_minutes"
    type: "string"
    description: |
      Defines how often, in minutes, Stitch should attempt to replicate data from Marketo. Accepted values are:

      - `1`
      - `10`
      - `30`
      - `60`
      - `360`
      - `720`
      - `1440`

  - name: "quota_percent_per_run"
    type: "string"
    description: "The maximum percentage of Salesforce API quota allowed per replication job."

  - name: "quota_percent_total"
    type: "string"
    description: "The maximum percentage of Salesforce API quota allowed per day."

  - name: "select_fields_by_default"
    type: "string"
    description: "If `true`, Stitch will automatically set new fields added in Salesforce to replicate."

  - name: "start_date"
    type: "string"
    description: "{{ connect.common.attributes.start-date }}"

examples:
  - code: |
      {  
       "type":"platform.salesforce",
       "properties":{
          "api_type":"BULK",
          "is_sandbox":"false",
          "frequency_in_minutes":"1440",
          "quota_percent_per_run":"25",
          "quota_percent_total":"80",
          "select_fields_by_default":"true",
          "start_date":"2018-01-10T00:00:00Z"
        }
      }
---