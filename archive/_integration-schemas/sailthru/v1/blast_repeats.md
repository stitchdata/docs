---
tap: "sailthru"
version: "1"
key: ""

name: "blast_repeats"
doc-link: "https://getstarted.sailthru.com/developers/api/blast_repeat/"
singer-schema: "https://github.com/singer-io/tap-sailthru/blob/master/tap_sailthru/schemas/blast_repeats.json"
description: |
  The `{{ table.name }}` table contains information about recurring campaigns in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "get BlastRepeat"
    doc-link: "https://getstarted.sailthru.com/developers/api/blast_repeat/"

attributes:
  - name: "repeat_id"
    type: "string"
    primary-key: true
    description: "The repeat ID."
    #foreign-key-id: "repeat-id"

  - name: "modify_time"
    type: "date-time"
    description: "The time the recurring campaign was last modified."
    replication-key: true
      
  - name: "create_time"
    type: "date-time"
    description: ""
  - name: "create_user"
    type: "string"
    description: ""
  - name: "days"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""
  - name: "days_month"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "integer"
        description: ""
  - name: "end_date"
    type: "date-time"
    description: ""
  - name: "error_time"
    type: "date-time"
    description: ""
  - name: "errors"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""
  - name: "generate_time"
    type: "integer"
    description: ""
  - name: "is_static"
    type: "boolean"
    description: ""
  - name: "list"
    type: "string"
    description: "The list ID."
    foreign-key-id: "list-id"
  - name: "message_criteria"
    type: "string"
    description: ""
  
  - name: "modify_user"
    type: "string"
    description: ""
  - name: "name"
    type: "string"
    description: ""
  - name: "previous_blast_id"
    type: "integer"
    description: ""
  
  - name: "report_email"
    type: "string"
    description: ""
  - name: "seed_emails"
    type: "string"
    description: ""
  - name: "send_time"
    type: "string"
    description: ""
  - name: "start_date"
    type: "date-time"
    description: ""
  - name: "status"
    type: "string"
    description: ""
  - name: "suppress_list"
    type: "string"
    description: ""
  - name: "template"
    type: "string"
    description: ""
  - name: "template_id"
    type: "integer"
    description: ""
---
