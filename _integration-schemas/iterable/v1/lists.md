---
tap: "iterable"
version: "1"
key: ""

name: "lists"
doc-link: https://api.iterable.com/api/docs#lists_getLists
singer-schema: https://github.com/singer-io/tap-iterable/tree/master/tap_iterable/schemas/lists.json
description: |
  The **{{ table.name }}** tablecontains information about lists within your {{ integration.display_name }} project.

replication-method: "Full Table"

api-method:
  name: "Get lists"
  doc-link: "https://api.iterable.com/api/docs#lists_getLists"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The list ID."
    foreign-key-id: "list-id"

  - name: "createdAt"
    type: "date-time"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "listType"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

---
