---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-amplitude-object"

title: "Amplitude Source Form Property"
description: "{{ api.form-properties.source-forms.amplitude.description }}"

object-attributes:
  - name: "account"
    type: "string"
    required: true
    description: "The account ID for the Amplitude Snowflake warehouse."

  - name: "database"
    type: "string"
    required: true
    description: "The name of the Amplitude Snowflake database."

  - name: "frequency_in_minutes"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]","Amplitude" }}

  - name: "password"
    type: "string"
    required: true
    description: "The password for the Amplitude Snowflake database user."

  - name: "username"
    type: "string"
    required: true
    description: "The username for the Amplitude Snowflake user."

  - name: "warehouse"
    type: "string"
    required: true
    description: "The name of the Amplitude Snowflake warehouse."

examples:
  - code: |
      {  
       "type":"platform.amplitude",
       "properties":{  
          "account":"<AMPLITUDE_SNOWFLAKE_ACCOUNT>",
          "database":"<AMPLITUDE_SNOWFLAKE_DATABASE>",
          "frequency_in_minutes":"1440",
          "password":"<AMPLITUDE_SNOWFLAKE_PASSWORD>",
          "username":"<AMPLITUDE_SNOWFLAKE_USERNAME>",
          "warehouse":"<AMPLITUDE_SNOWFLAKE_WAREHOUSE>"
        }
      }
---