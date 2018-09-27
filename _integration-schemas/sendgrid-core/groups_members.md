---
tap: "sendgrid-core"

name: "group_members"
doc-link: https://sendgrid.com/docs/API_Reference/Web_API_v3/Suppression_Management/suppressions.html#-GET
singer-schema: https://github.com/singer-io/tap-sendgrid/blob/master/tap_sendgrid/schemas/groups_members.json
description: |
  The `group_members` table contains a list of `email` and `group_id` pairs, allowing you to identify recipients and the groups they are members of.

replication-method: "Full Table"

api-method:
  name: "List all suppressions"
  doc-link: "https://sendgrid.com/docs/API_Reference/Web_API_v3/Suppression_Management/suppressions.html#-GET" 

attributes:
  - name: "email"
    type: "string"
    primary-key: true
    description: "The email address of the recipient."
    foreign-key-id: "email-id"

  - name: "group_id"
    type: "integer"
    description: "The ID of the group the recipient is a member of."
    foreign-key-id: "suppression-group-id"
---