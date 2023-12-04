---
tap: "lever"
version: "1"
key: "stage"

name: "stages"
doc-link: "https://hire.lever.co/developer/documentation#stages"
singer-schema: "https://github.com/singer-io/tap-lever/blob/master/tap_lever/schemas/stages.json"
description: |
  The `{{ table.name }}` table contains info about stages, or the steps in the recruiting workflow in your hiring pipeline.

replication-method: "Full Table"

api-method:
  name: "List all stages"
  doc-link: "https://hire.lever.co/developer/documentation#list-all-stages"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The stage ID."
    foreign-key-id: "stage-id"

  - name: "text"
    type: "string"
    description: "The title of the stage."
---