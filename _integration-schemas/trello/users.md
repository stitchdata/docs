---
tap: "trello"
version: "1"
key: ""

name: "users"
doc-link: "https://developer.atlassian.com/cloud/trello/rest/#api-boards-id-members-get"
singer-schema: "https://github.com/singer-io/tap-trello/blob/master/tap_trello/schemas/users.json"
description: |
  The {{ table.name }} table contains information about users on your boards on your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
    name: "Get the Members of a Board"
    doc-link: "https://developer.atlassian.com/cloud/trello/rest/#api-boards-id-members-get"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The user ID."
    #foreign-key-id: "users-id"

  - name: "boardId"
    type: "string"
    description: "The board ID."
    foreign-key-id: "boards-id"
    
  - name: "fullName"
    type: "string"
    description: ""
  - name: "username"
    type: "string"
    description: ""
---
