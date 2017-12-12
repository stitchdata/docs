---
tap: "autopilot"
# version: 

name: "lists"
doc-link: http://docs.autopilot.apiary.io/#reference/api-methods/lists/get-list-of-lists
singer-schema: https://github.com/singer-io/tap-autopilot/blob/master/tap_autopilot/schemas/lists.json
description: |
  The `lists` table contains info about the available lists in your Autopilot account.

replication-method: "Full Table"
api-method:
  name: getListofLists
  doc-link: http://docs.autopilot.apiary.io/#reference/api-methods/lists/get-list-of-lists

attributes:
  - name: "list_id"
    type: "string"
    primary-key: true
    description: "The ID of the list."

  - name: "title"
    type: "string"
    description: "The title of the list."
---