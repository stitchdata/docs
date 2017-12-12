---
tap: "intercom"
# version:

name: "admins"
doc-link: https://developers.intercom.io/docs/admins
description: |
  The `admins` table contains info about the admins and teams in your Intercom account.

replication-method: "Full Table"
api-method:
  name: listAdmins
  doc-link: https://developers.intercom.io/docs/list-admins

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The admin or team ID."

  - name: "type"
    type: "string"
    description: "The admin type. This value will be either `admin` or `team`."

  - name: "name"
    type: "string"
    description: "The name of the admin or team."

  - name: "email"
    type: "string"
    description: "The email address of the admin. This will be `NULL` for teams."
---