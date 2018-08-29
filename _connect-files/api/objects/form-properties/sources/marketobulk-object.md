---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-marketo-bulk-object"

title: "Marketo Bulk Source Form Property"
description: "{{ api.form-properties.source-forms.marketo-bulk.description }}"

object-attributes:
  - name: "client_id"
    type: "string"
    required: true
    description: "The user's Marketo client ID."

  - name: "client_secret"
    type: "string"
    required: true
    description: "The user's Marketo client secret."

  - name: "frequency_in_minutes"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]","Marketo" }}

  - name: "endpoint"
    type: "string"
    required: true
    description: "The user's Marketo REST endpoint URL. For example: `https://457-RFG-234.mktorest.com/rest`"

  - name: "identity"
    type: "string"
    required: true
    description: "The user's Marketo REST identity URL. For example: `https://457-RFG-234.mktorest.com/identity`"

  - name: "start_date"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.start-date replace: "[INTEGRATION]","Marketo" }}

examples: 
  - code: |
      {  
       "type":"platform.marketobulk",
       "properties":{
          "client_id":"<CLIENT_ID>",
          "client_secret":"<CLIENT_SECRET>",
          "frequency_in_minutes":"1440",
          "endpoint":"https://457-RFG-234.mktorest.com/rest",
          "identity":"https://457-RFG-234.mktorest.com/identity",
          "start_date":"2018-01-10T00:00:00Z"
        }
      }
---