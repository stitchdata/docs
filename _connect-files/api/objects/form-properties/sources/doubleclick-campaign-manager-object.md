---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-doubleclick-campaign-manager-object"

title: "DoubleClick Campaign Manager Source Form Property"
api-type: "doubleclick-campaign-manager"
display-name: "DoubleClick Campaign Manager"

description: "{{ api.form-properties.source-forms.doubleclick-campaign-manager.description }}"

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
---