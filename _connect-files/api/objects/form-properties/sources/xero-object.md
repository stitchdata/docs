---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-xero-object"

title: "Xero Source Form Property"
description: "{{ api.form-properties.source-forms.xero.description }}"

object-attributes:
  - name: "frequency_in_minutes"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]","Xero" }}

  - name: "start_date"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.start-date | replace: "[INTEGRATION]","Xero" }}

examples: 
  - code: |
      {  
       "type":"platform.xero",
       "properties":{
          "frequency_in_minutes":"1440",
          "start_date":"2018-01-10T00:00:00Z"
        }
      }
---