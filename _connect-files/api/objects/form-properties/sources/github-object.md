---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-github-object"

title: "GitHub Source Form Property"
api-type: "github"
display-name: "GitHub"

description: "{{ api.form-properties.source-forms.github.description }}"

object-attributes:
  - name: "access_token"
    type: "string"
    required: true
    description: "An access token which allows access to any project the user wants to replicate data from."
    value: "<ACCESS_TOKEN>"

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
      {{ connect.common.attributes.frequency | replace: "[INTEGRATION]","GitHub" }}
    value: "{{ sample-property-data.frequency }}"

  - name: "repository"
    type: "string"
    required: true
    description: "The name of the repository to be tracked."
    value: "<REPOSITORY_NAME>"

  - name: "start_date"
    type: "string"
    required: true
    description: |
      {{ connect.common.attributes.start-date | replace: "[INTEGRATION]","GitHub" }}
    value: "{{ sample-property-data.start-date }}"
---