---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-github-object"

title: "GitHub Source Form Property"
description: "{{ api.form-properties.source-forms.github.description }}"

object-attributes:
  - name: "access_token"
    type: "string"
    required: true
    description: "An access token which allows access to any project the user wants to replicate data from."

  - name: "frequency_in_minutes"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]","GitHub" }}

  - name: "repository"
    type: "string"
    required: true
    description: "The name of the repository to be tracked."

  - name: "start_date"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.start-date | replace: "[INTEGRATION]","GitHub" }}

examples: 
  - code: |
      {  
       "type":"platform.github",
       "properties":{
          "access_token":"<ACCESS_TOKEN>",
          "frequency_in_minutes":"1440",
          "repository":"stitchdocs"
          "start_date":"2018-01-10T00:00:00Z"
        }
      }
---