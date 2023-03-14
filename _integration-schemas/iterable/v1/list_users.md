---
tap: "iterable"
version: "1"
key: ""

name: "list_users"
doc-link: https://api.iterable.com/api/docs#lists_getLists_0
singer-schema: https://github.com/singer-io/tap-iterable/tree/master/tap_iterable/schemas/list_users.json
description: |
  The **{{ table.name }}** table contains information about users in a list in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "Get users in a list"
  doc-link: "https://api.iterable.com/api/docs#lists_getLists_0"  

attributes:
  - name: "email"
    type: "string"
    primary-key: true
    description: "The user email."
    foreign-key-id: "email-id"

  - name: "listId"
    type: "integer"
    primary-key: true
    description: "The list ID."
    foreign-key-id: "list-id"

  - name: "updatedAt"
    type: "date-time"
    description: ""

---
