---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-hubspot-object"

title: "HubSpot Source Form Property"
api-type: "hubspot"
display-name: "HubSpot"

description: "{{ api.form-properties.source-forms.hubspot.description }}"

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

  - name: "start_date"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.start-date | replace: "[INTEGRATION]",form-property.display-name }}
    value: "{{ sample-property-data.start-date }}"
---