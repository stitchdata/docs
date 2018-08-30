---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-zendesk-object"

title: "Zendesk Source Form Property"
api-type: "zendesk"
display-name: "Zendesk"

description: "{{ api.form-properties.source-forms.zendesk.description }}"

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
      {{ connect.common.attributes.start-date | replace: "[INTEGRATION]",form-property.display-name}}
    value: "{{ sample-property-data.start-date }}"

  - name: "subdomain"
    type: "string"
    required: true
    description: |
      The prefix of the Zendesk subdomain Stitch should replicate data from.

      For example: If the address is `stitchdata.zendesk.com`, only `stitchdata` would be entered as the value.
    value: "<YOUR_ZENDESK_SUBDOMAIN>"
---