---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-google-adwords-object"

title: "Google AdWords Source Form Property"
description: "{{ api.form-properties.source-forms.google-adwords.description }}"

object-attributes:
  - name: "frequency_in_minutes"
    type: "string"
    description: |
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]","Google AdWords" }}

  - name: "start_date"
    type: "string"
    description: |
      {{ connect.common.attributes.start-date | replace: "[INTEGRATION]","Google AdWords" }}

examples: 
  - code: |
      {  
       "type":"platform.adwords",
       "properties":{  
          "frequency_in_minutes":"30",
          "start_date":"2018-01-10T00:00:00Z"
        }
      }
---