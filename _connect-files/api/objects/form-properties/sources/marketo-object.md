---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-marketo-object"

title: "Marketo"
description: "{{ api.form-properties.source-forms.marketo.description }}"

object-attributes:
  - name: "client_id"
    type: "string"
    description: "The user's Marketo client ID."

  - name: "client_secret"
    type: "string"
    description: "The user's Marketo client secret."

  - name: "frequency_in_minutes"
    type: "string"
    description: |
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]",form-property.title }}

  - name: "endpoint"
    type: "string"
    description: "The user's Marketo REST endpoint URL. For example: `https://457-RFG-234.mktorest.com/rest`"

  - name: "identity"
    type: "string"
    description: "The user's Marketo REST identity URL. For example: `https://457-RFG-234.mktorest.com/identity`"

  - name: "max_daily_calls"
    type: "string"
    description: "The maximum number of daily API calls that Stitch may make to the Marketo API."

  - name: "start_date"
    type: "string"
    description: "{{ connect.common.attributes.start-date }}"

examples: 
  - code: |
      {  
       "type":"platform.marketo",
       "properties":{
          "client_id":"<CLIENT_ID>",
          "client_secret":"<CLIENT_SECRET>",
          "frequency_in_minutes":"1440",
          "endpoint":"https://457-RFG-234.mktorest.com/rest",
          "identity":"https://457-RFG-234.mktorest.com/identity",
          "max_daily_calls":"8,000",
          "start_date":"2018-01-10T00:00:00Z"
        }
      }
---