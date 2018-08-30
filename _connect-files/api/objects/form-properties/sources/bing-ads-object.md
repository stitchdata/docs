---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-bing-ads-object"

title: "Bing Ads Source Form Property"
description: "{{ api.form-properties.source-forms.bing-ads.description }}"
api-type: "bing-ads"

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
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]","Bing Ads" }}
    value: "{{ sample-property-data.frequency }}"

  - name: "start_date"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.start-date replace: | "[INTEGRATION]","Bing Ads" }}
    value: "{{ sample-property-data.start-date }}"
---