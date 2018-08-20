---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-doubleclick-campaign-manager-object"

title: "DoubleClick Campaign Manager Source Form Property"
description: "{{ api.form-properties.source-forms.doubleclick-campaign-manager.description }}"

object-attributes:
  - name: "frequency_in_minutes"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]","DoubleClick Campaign Manager" }}

examples: 
  - code: |
      {  
       "type":"platform.doubleclick-campaign-manager",
       "properties":{
          "frequency_in_minutes":"1440"
        }
      }
---