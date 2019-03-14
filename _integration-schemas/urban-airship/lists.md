---
tap: "urban_airship"
# version:

name: "lists"
doc-link: http://docs.urbanairship.com/api/ua.html#static-lists
singer-schema: https://github.com/singer-io/tap-urban-airship/blob/master/tap_urban_airship/schemas/lists.json
description: |
  The `lists` table contains info about device lists.

replication-method: "Key-based Incremental"
api-method:
  name: allLists
  doc-link: https://docs.urbanairship.com/api/ua/#all-lists

attributes:
  - name: "name"
    type: "string"
    primary-key: true
    description: "The name of the list."

  - name: "created"
    type: "date-time"
    replication-key: true
    description: "The time the list was created."

  - name: "last_modified"
    type: "date-time"
    replication-key: true
    description: "The time the list was last updated."

  - name: "description"
    type: "string"
    description: "A description of the list."

  - name: "extra"
    type: "array"
    description: "A list of the arbitrary, user-provided JSON values associated with the list."
    subattributes:
      - name: "key"
        type: "string"
        description: "The key to the associated value."

      - name: "value"
        type: "string"
        description: "The value associated with the given key."

  - name: "channel_count"
    type: "integer"
    description: "A count of resolved channels for the last uploaded and successfully processed identifier list."

  - name: "status"
    type: "string"
    description: |
      The status of the list. Possible values:

      - `ready`
      - `processing`
      - `failure : > * ready` - Indicates the list was processed successfully and is ready for sending.
---