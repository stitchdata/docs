---
tap: "sailthru"
version: "0.2"
key: ""

name: "blasts"
doc-link: "https://getstarted.sailthru.com/developers/api/blast/"
singer-schema: "https://github.com/singer-io/tap-sailthru/blob/master/tap_sailthru/schemas/blasts.json"
description: |
  The `{{ table.name }}` table contains infomation about your specific {{ integration.display_name }} campaigns, or information about campaigns by status types: `sent`, `sending`, `scheduled`, `unscheduled`.

replication-method: "Key-based Incremental"

api-method:
    name: "get Blasts"
    doc-link: "https://getstarted.sailthru.com/developers/api/blast/"

attributes:
  - name: "blast_id"
    type: "integer"
    primary-key: true
    description: "The blast ID."
    foreign-key-id: "blast-id"

  - name: "modify_time"
    type: "date-time"
    description: "The time the campaign was last modified."
    replication-key: true  

  - name: "copy_template"
    type: "string"
    description: ""
  - name: "data_feed_url"
    type: "string"
    description: ""
  - name: "email_count"
    type: "integer"
    description: ""
  - name: "list"
    type: "string"
    description: "The list ID."
    foreign-key-id: "list-id"
  - name: "mode"
    type: "string"
    description: ""
  
  - name: "modify_user"
    type: "string"
    description: ""
  - name: "name"
    type: "string"
    description: ""
  - name: "schedule_time"
    type: "date-time"
    description: ""
  - name: "sent_count"
    type: "integer"
    description: ""
  - name: "start_time"
    type: "date-time"
    description: ""
  - name: "stats"
    type: "object"
    description: ""
    subattributes:
      - name: "total"
        type: "object"
        description: ""
        subattributes:
          - name: "beacon_noclick"
            type: "integer"
            description: ""
          - name: "count"
            type: "integer"
            description: ""
          - name: "open_total"
            type: "integer"
            description: ""
          - name: "pv"
            type: "integer"
            description: ""
  - name: "status"
    type: "string"
    description: ""
  - name: "subject"
    type: "string"
    description: ""
---
