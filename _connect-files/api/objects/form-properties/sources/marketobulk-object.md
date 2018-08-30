---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-marketo-bulk-object"

title: "Marketo Bulk Source Form Property"
api-type: "marketobulk"
display-name: "Marketo Bulk"

description: "{{ api.form-properties.source-forms.marketo-bulk.description }}"

object-attributes:
  - name: "anchor_time"
    type: "string"
    required: false
    description: |
      {{ connect.common.attributes.anchor-time | replace: "[INTEGRATION]",form-property.display-name }}
    value: "{{ sample-property-data.anchor-time }}"

  - name: "client_id"
    type: "string"
    required: true
    description: "The user's Marketo client ID."
    value: "<MARKETO_CLIENT_ID>"

  - name: "client_secret"
    type: "string"
    required: true
    description: "The user's Marketo client secret."
    value: "<MARKETO_CLIENT_SECRET>"

  - name: "frequency_in_minutes"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]",form-property.display-name }}
    value: "{{ sample-property-data.frequency }}"

  - name: "endpoint"
    type: "string"
    required: true
    description: "The user's Marketo REST endpoint URL. For example: `https://457-RFG-234.mktorest.com/rest`"
    value: "https://<some-id-here>.mktorest.com/rest"

  - name: "identity"
    type: "string"
    required: true
    description: "The user's Marketo REST identity URL. For example: `https://457-RFG-234.mktorest.com/identity`"
    value: "https://<some-id-here>.mktorest.com/identity"

  - name: "start_date"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.start-date | replace: replace: "[INTEGRATION]",form-property.display-name }}
    value: "{{ sample-property-data.start-date }}"
---