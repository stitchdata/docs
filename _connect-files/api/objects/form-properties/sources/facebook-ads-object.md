---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-facebook-ads-object"

title: "Facebook Ads Source Form Property"
description: "{{ api.form-properties.source-forms.facebook-ads.description }}"

object-attributes:
  # - name: "aggregate_level"
  #   type: "PLACEHOLDER"
  #   description: "[PLACEHOLDER]"

  # - name: "attribution_window"
  #   type: "PLACEHOLDER"
  #   description: "[PLACEHOLDER]"

  - name: "frequency_in_minutes"
    type: "string"
    description: |
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]","Facebook Ads" }}

  - name: "include_deleted"
    type: "string"
    description: "If `true`, Stitch will replicate data for deleted campaigns, ads, and adsets. **Note**: This data will not be included alongside insights data."

  # - name: "insights_buffer_days"
  #   type: "string"
  #   description: "[PLACEHOLDER]"

  - name: "start_date"
    type: "string"
    description: |
      {{ connect.common.attributes.start-date | replace: "[INTEGRATION]","Facebook Ads" }}

examples: 
  - code: |
      {  
       "type":"platform.facebook",
       "properties":{  
          "frequency_in_minutes":"30",
          "include_deleted":"true",
          "start_date":"2018-01-10T00:00:00Z"
        }
      }
---