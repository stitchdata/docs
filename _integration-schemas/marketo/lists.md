---
tap: "marketo"
# version: ""

name: "lists"
doc-link: http://developers.marketo.com/rest-api/endpoint-reference/lead-database-endpoint-reference/#!/Static_Lists/getListsUsingGET
singer-schema: https://github.com/singer-io/tap-marketo/blob/master/tap_marketo/schemas/lists.json
description: |
  The `leads` table contains info about the static lists in your {{ integration.display_name }} account. 

  Note that due to some of the limitations in Marketo’s API, only static lists will be replicated.

notes:

replication-method: "Key-based Incremental"
api-method:
  name: "getLists"
  doc-link: "http://developers.marketo.com/rest-api/endpoint-reference/lead-database-endpoint-reference/#!/Static_Lists/getListsUsingGET"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the list."

  - name: "updatedAt"
    type: "date-time"
    replication-key: true
    description: "The datetime when the list was most recently updated."

  - name: "name"
    type: "string"
    description: "The name of the list."

  - name: "description"
    type: "string"
    description: "The description of the list."

  - name: "programName"
    type: "string"
    description: "The name of the program associated with the list."

  - name: "workspaceName"
    type: "string"
    description: "The name of the parent workspace, if applicable."

  - name: "createdAt"
    type: "date-time"
    description: "The datetime the list was created."
---