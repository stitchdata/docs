---
tap: "netsuite-suite-analytics"
version: "1"
key: "activity"

name: "activities"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/activities.html"
description: |
  The `{{ table.name }}` table contains info about activities.

  {{ integration.append-only-loading | flatify }}

replication-method: "Key-based Incremental"
loading-behavior: "Append-Only"

attributes:
  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: "The time the activity was last modified."

  - name: "access_level"
    type: "string"
    description: ""

  - name: "activity_id"
    type: "integer"
    description: ""

  - name: "assigned_to_id"
    type: "integer"
    description: ""

  - name: "case_id"
    type: "integer"
    description: ""

  - name: "contact_id"
    type: "integer"
    description: ""
    # foreign-key-id: "contact-id"

  - name: "date_0"
    type: "date-time"
    description: ""

  - name: "date_completed"
    type: "date-time"
    description: ""

  - name: "date_created"
    type: "date-time"
    description: "The date the activity was created. **Note**: According to NetSuite's documentation, this field isn't applicable to the `note` activity type."

  - name: "entity_id"
    type: "integer"
    description: ""
    # foreign-key-id: "entity-id"

  - name: "memo"
    type: "string"
    description: |
      The memo for the activity. From NetSuite's documentation:

      > Memo. Long messages may be truncated. If you need a longer message, try joining the `message` column from the `message` table.

  - name: "opportunity_id"
    type: "string"
    description: ""
    # foreign-key-id: "opportunity-id"

  - name: "owner_id"
    type: "integer"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "type_0"
    type: "string"
    description: ""
---