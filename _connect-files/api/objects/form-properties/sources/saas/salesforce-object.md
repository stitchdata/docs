---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-salesforce-object"

title: "Salesforce Source Form Property"
api-type: "salesforce"
display-name: "Salesforce"

description: "{{ api.form-properties.source-forms.salesforce.description }}"

object-attributes:
  - name: "anchor_time"
    type: "string"
    required: false
    description: |
      {{ connect.common.attributes.anchor-time | replace: "[INTEGRATION]",form-property.display-name }}
    value: "{{ sample-property-data.anchor-time }}"

  - name: "api_type"
    type: "string"
    required: true
    description: "The Salesforce API Stitch should use to extract data. Possible values are `REST` or `BULK`. [Read about the pros and cons of each API here]({{ site.baseurl }}/integrations/saas/salesforce#bulk-vs-rest-api)."
    value: "BULK"

  - name: "is_sandbox"
    type: "string"
    required: false
    description: "If `true`, the Salesforce account being connected is a sandbox."
    value: "false"

  - name: "frequency_in_minutes"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]",form-property.display-name }}
    value: "{{ sample-property-data.frequency }}"

  - name: "quota_percent_per_run"
    type: "string"
    required: false
    description: "The maximum percentage of Salesforce API quota allowed per replication job."
    value: "20"

  - name: "quota_percent_total"
    type: "string"
    required: false
    description: "The maximum percentage of Salesforce API quota allowed per day."
    value: "80"

  - name: "select_fields_by_default"
    type: "string"
    required: true
    description: "If `true`, Stitch will automatically set new fields added in Salesforce to replicate."
    value: "false"

  - name: "start_date"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.start-date | replace: "[INTEGRATION]",form-property.display-name }}
    value: "{{ sample-property-data.start-date }}"
---