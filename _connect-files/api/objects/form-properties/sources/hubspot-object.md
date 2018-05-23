---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-hubspot-object"

title: "HubSpot Source Form Property"
description: "{{ api.form-properties.source-forms.hubspot.description }}"

object-attributes:
  - name: "frequency_in_minutes"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]","HubSpot" }}

  - name: "anchor_time"
    type: "string"
    required: false
    description: |
      {{ connect.common.attributes.anchor-time }}

  - name: "start_date"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.start-date | replace: "[INTEGRATION]","HubSpot" }}

examples: 
  - code: |
      {  
       "type":"platform.hubspot",
       "properties":{  
          "frequency_in_minutes":"30",
          "anchor_time":"",
          "start_date":"2018-01-10T00:00:00Z"
        }
      }
---