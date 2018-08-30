---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-bronto-object"

title: "Bronto Source Form Property"
display-name: "Bronto"
api-type: "bronto"

description: "{{ api.form-properties.source-forms.bronto.description }}"

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
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]","Bronto" }}
    value: "{{ sample-property-data.frequency }}"

  - name: "start_date"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.start-date | replace: "[INTEGRATION]","Bronto" }}
    value: "{{ sample-property-data.start-date }}"

  - name: "token"
    type: "string"
    required: true
    description: "The API token for the Bronto account Stitch should replicate data from."
    value: "<API_TOKEN>"
---