---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-listrak-object"

title: "Listrak Source Form Property"
api-type: "listrak"
display-name: "Listrak"

description: "{{ api.form-properties.source-forms.listrak.description }}"

object-attributes:
  - name: "anchor_time"
    type: "string"
    required: false
    description: |
      {{ connect.common.attributes.anchor-time | replace: "[INTEGRATION]",form-property.display-name }}
    value: "{{ sample-property-data.anchor-time }}"

  - name: "frequency_in_minutes"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]",form-property.display-name }}
    value: "{{ sample-property-data.frequency }}"

  - name: "password"
    type: "string"
    required: true
    description: "The password associated with the Listrak user."
    value: "{{ sample-property-data.password }}"

  - name: "start_date"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.start-date | replace: "[INTEGRATION]",form-property.display-name }}
    value: "{{ sample-property-data.start-date }}"

  - name: "username"
    type: "string"
    required: true
    description: "The user's Listrak username."
    value: "{{ sample-property-data.user }}"
---