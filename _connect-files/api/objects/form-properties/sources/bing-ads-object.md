---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-bing-ads-object"

title: "Bing Ads Source Form Property"
description: "{{ api.form-properties.source-forms.bing-ads.description }}"

object-attributes:
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

  - name: "anchor_time"
    type: "string"
    required: true
    description: "{{ connect.common.attributes.anchor-time }}"
    value: "{{ sample-property-data.anchor-time }}"

examples: 
  - code: |
      {  
       "type":"platform.bing-ads",
       "properties":{
          "frequency_in_minutes":"1440",
          "start_date":"2018-01-10T00:00:00Z",
          "token":"<TOKEN>"
        }
      }
---