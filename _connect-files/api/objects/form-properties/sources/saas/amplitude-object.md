---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-amplitude-object"

title: "Amplitude Source Form Property"
description: "{{ api.form-properties.source-forms.amplitude.description }}"
api-type: "amplitude"
integration-type: "saas"
docs-name: "amplitude"

object-attributes:
  - name: "account"
    type: "string"
    required: true
    description: "The account ID for the Amplitude Snowflake warehouse."
    value: "<AMPLITUDE_SNOWFLAKE_ACCOUNT>"

  - name: "anchor_time"
    type: "string"
    required: false
    description: |
      {{ connect.common.attributes.anchor-time | replace: "[INTEGRATION]",form-property.display-name }}
    value: "{{ sample-property-data.anchor-time }}"

  - name: "database"
    type: "string"
    required: true
    description: "The name of the Amplitude Snowflake database."
    value: "{{ sample-property-data.database }}"

  - name: "frequency_in_minutes"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]","Amplitude" }}
    value: "{{ sample-property-data.frequency }}"

  - name: "password"
    type: "string"
    required: true
    description: "The password for the Amplitude Snowflake database user."
    value: "{{ sample-property-data.password }}"

  - name: "username"
    type: "string"
    required: true
    description: "The username for the Amplitude Snowflake user."
    value: "{{ sample-property-data.user }}"

  - name: "warehouse"
    type: "string"
    required: true
    description: "The name of the Amplitude Snowflake warehouse."
    value: "<AMPLITUDE_WAREHOUSE>"
---