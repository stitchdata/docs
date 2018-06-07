---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-zendesk-object"

title: "Zendesk Source Form Property"
description: "{{ api.form-properties.source-forms.zendesk.description }}"

object-attributes:
  - name: "frequency_in_minutes"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]","Zendesk" }}

  - name: "start_date"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.start-date | replace: "[INTEGRATION]","Zendesk" }}

  - name: "subdomain"
    type: "string"
    required: true
    description: |
      The prefix of the Zendesk subdomain Stitch should replicate data from.

      For example: If the address is `stitchdata.zendesk.com`, only `stitchdata` would be entered as the value.

examples:
  - code: |
      {  
       "type":"platform.zendesk",
       "properties":{
          "frequency_in_minutes":"1440",
          "start_date":"2018-01-10T00:00:00Z",
          "subdomain":"stitchdata"
        }
      }
---