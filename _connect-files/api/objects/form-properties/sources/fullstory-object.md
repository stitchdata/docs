---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-fullstory-object"

title: "FullStory Source Form Property"
description: |
  {{ api.form-properties.source-forms.fullstory.description }}

  **Note**: To use this integration, the user must have a FullStory account with the Data Export Pack add-on. This is a paid addition that allows users to export raw event data, and is required to use FullStory's Data Export REST API.

object-attributes:
  - name: "api_key"
    type: "string"
    required: true
    description: |
      A FullStory API key, used to authenticate to FullStory's Data Export API.

  - name: "frequency_in_minutes"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]","FullStory" }}

  - name: "start_date"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.start-date | replace: "[INTEGRATION]","FullStory" }}

examples: 
  - code: |
      {  
       "type":"platform.fullstory",
       "properties":{  
          "frequency_in_minutes":"30",
          "start_date":"2018-01-10T00:00:00Z"
        }
      }
---