---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-fullstory-object"

title: "FullStory Source Form Property"
api-type: "fullstory"
display-name: "FullStory"

description: |
  {{ api.form-properties.source-forms.fullstory.description }}

  **Note**: To use this integration, the user must have a FullStory account with the [FullStory Data Export Pack add-on](https://help.fullstory.com/technical-questions/data-export). This is a paid addition that allows users to export raw event data, and is required to use FullStory's Data Export REST API.

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
    description: |
      A FullStory API key, used to authenticate to FullStory's Data Export API.
    value: "<API_KEY>"

  - name: "frequency_in_minutes"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]","FullStory" }}
    value: "{{ sample-property-data.frequency }}"

  - name: "start_date"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.start-date | replace: "[INTEGRATION]","FullStory" }}
    value: "{{ sample-property-data.start-date }}"
---