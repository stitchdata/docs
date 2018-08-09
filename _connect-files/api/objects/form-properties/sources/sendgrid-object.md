---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-sendgrid-object"

title: "SendGrid Source Form Property"
description: "{{ api.form-properties.source-forms.sendgrid.description }}"

object-attributes:
  - name: "api_key"
    type: "string"
    required: true
    description: "The SendGrid API key. Refer to [SendGrid's documentation](https://sendgrid.com/docs/Classroom/Basics/API/api_key_permissions.html) for info about permissions and creating keys."

  - name: "frequency_in_minutes"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]","SendGrid" }}

  - name: "start_date"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.start-date | replace: "[INTEGRATION]","SendGrid" }}

examples: 
  - code: |
      {  
       "type":"platform.sendgrid",
       "properties":{
          "api_key":"<API_KEY>",
          "frequency_in_minutes":"1440",
          "start_date":"2018-01-10T00:00:00Z"
        }
      }
---