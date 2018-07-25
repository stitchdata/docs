---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-listrak-object"

title: "Listrak Source Form Property"
description: "{{ api.form-properties.source-forms.listrak.description }}"

object-attributes:
  - name: "frequency_in_minutes"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]","Listrak" }}

  - name: "password"
    type: "string"
    required: true
    description: "The password associated with the Listrak user."

  - name: "start_date"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.start-date | replace: "[INTEGRATION]","Listrak" }}

  - name: "username"
    type: "string"
    required: true
    description: "The user's Listrak username."

examples: 
  - code: |
      {  
       "type":"platform.listrak",
       "properties":{  
          "frequency_in_minutes":"30",
          "password":"<PASSWORD>",
          "start_date":"2018-01-10T00:00:00Z",
          "username":"stitch",
        }
      }
---