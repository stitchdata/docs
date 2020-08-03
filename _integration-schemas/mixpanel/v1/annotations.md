---
tap: "mixpanel"
version: "1"
key: "annotation"

name: "annotations"
doc-link: "https://developer.mixpanel.com/docs/data-export-api#section-annotations"
singer-schema: "https://github.com/singer-io/tap-mixpanel/blob/master/tap_mixpanel/schemas/annotations.json"
description: |
  The `{{ table.name }}` table contains info about annotations.

replication-method: "Full Table"

api-method:
  name: "Get annotations"
  doc-link: "https://mixpanel.com/api/2.0/annotations"

attributes:
  - name: "date"
    type: "date-time"
    primary-key: true
    description: "The date the annotation occurred."

  - name: "description"
    type: "string"
    description: "The description of the annotation."

  - name: "id"
    type: "integer"
    description: "The annotation ID."

  - name: "project_id"
    type: "integer"
    description: "The ID of the project associated with the annotation."
    foreign-key-id: "project-id"
---