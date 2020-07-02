---
tap: "trello"
version: "1"
key: "user"

name: "users"
doc-link: "https://developer.atlassian.com/cloud/trello/rest/#api-boards-id-members-get"
singer-schema: "https://github.com/singer-io/tap-trello/blob/master/tap_trello/schemas/users.json"
description: |
  The {{ table.name }} table contains information about users who are members of boards that the [authorizing user](#data-replication-board-membership) is also a member of.

replication-method: "Full Table"

api-method:
    name: "Get the members of a board"
    doc-link: "https://developer.atlassian.com/cloud/trello/rest/#api-boards-id-members-get"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The user ID."
    foreign-key-id: "user-id"

  - name: "boardId"
    type: "string"
    primary-key: true
    description: "The board ID."
    foreign-key-id: "board-id"
    
  - name: "fullName"
    type: "string"
    description: ""

  - name: "username"
    type: "string"
    description: ""
---
