---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-sendgrid-object"

title: "SendGrid Source Form Property"
api-type: "sendgrid"
display-name: "SendGrid"

description: "{{ api.form-properties.source-forms.sendgrid.description }}"

object-attributes:
  - name: "anchor_time"
    type: "string"
    required: false
    description: |
      {{ connect.common.attributes.anchor-time | replace: "[INTEGRATION]",form-property.display-name }}
    value: "{{ sample-property-data.anchor-time }}"

  - name: "api_key"
    type: "string"
    required: true
    description: "The SendGrid API key. Refer to [SendGrid's documentation](https://sendgrid.com/docs/Classroom/Basics/API/api_key_permissions.html) for info about permissions and creating keys."
    value: "<API_KEY>"

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
---