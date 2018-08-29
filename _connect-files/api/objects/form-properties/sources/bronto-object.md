---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-bronto-object"

title: "Bronto Source Form Property"
description: "{{ api.form-properties.source-forms.bronto.description }}"

object-attributes:
  - name: "frequency_in_minutes"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]","Bronto" }}

  - name: "start_date"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.start-date | replace: "[INTEGRATION]","Bronto" }}

  - name: "token"
    type: "string"
    required: true
    description: "The API token for the Bronto account Stitch should replicate data from."

examples: 
  - code: |
      {  
       "type":"platform.bronto",
       "properties":{
          "frequency_in_minutes":"1440",
          "start_date":"2018-01-10T00:00:00Z",
          "token":"<TOKEN>"
        }
      }
---