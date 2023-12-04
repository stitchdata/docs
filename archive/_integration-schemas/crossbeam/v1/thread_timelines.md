---
tap: "crossbeam"
version: "1"
key: ""

name: "thread_timelines"
doc-link: "https://developers.crossbeam.com/#6315ece6-1805-4132-9337-13bf4607e77a"
singer-schema: "https://github.com/singer-io/tap-crossbeam/blob/master/tap_crossbeam/schemas/thread_timelines.json"
description: |
  The `{{ table.name }}` table contains information about the activity for any given `thread-id` in your {{ integration.display_name }} account. This is a child table of `threads`.

replication-method: "Full Table"

api-method:
    name: "get ThreadTimeline"
    doc-link: "https://developers.crossbeam.com/#6315ece6-1805-4132-9337-13bf4607e77a"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The thread ID of the timeline."

  - name: "acting_organization_id"
    type: "integer"
    description: ""
  - name: "created_at"
    type: "date-time"
    description: ""
  - name: "event_data"
    type: "object"
    description: ""
    subattributes:
      - name: "acting_user_id"
        type: "integer"
        description: ""
  - name: "event_type"
    type: "string"
    description: ""
  
  - name: "is_private"
    type: "boolean"
    description: ""
  - name: "message"
    type: "object"
    description: ""
    subattributes:
      - name: "content"
        type: "string"
        description: ""
      - name: "edited_at"
        type: "date-time"
        description: ""
      - name: "is_deleted"
        type: "boolean"
        description: ""
      - name: "user_id"
        type: "integer"
        description: ""
---
