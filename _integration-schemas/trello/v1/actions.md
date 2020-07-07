---
tap: "trello"
version: "1"
key: "action"

name: "actions"
doc-link: "https://developer.atlassian.com/cloud/trello/rest/#api-boards-boardId-actions-get"
singer-schema: "https://github.com/singer-io/tap-trello/blob/master/tap_trello/schemas/actions.json"
description: |
  The {{ table.name }} table contains information about the actions within each board the [authorizing user](#data-replication-board-membership) is a member of.

replication-method: "Key-based Incremental"

api-method:
    name: "Get actions of a board"
    doc-link: "https://developer.atlassian.com/cloud/trello/rest/#api-boards-boardId-actions-get"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The action ID."
    foreign-key-id: "action-id"

  - name: "date"
    type: "string"
    replication-key: true
    description: "The date the action was created."  

  - name: "data"
    type: "object"
    description: ""
    subattributes:
      - name: "board"
        type: "object"
        description: ""
        subattributes:
          - name: "id"
            type: "string"
            description: "The board ID."
            foreign-key-id: "board-id"

          - name: "name"
            type: "string"
            description: ""

          - name: "prefs"
            type: "object"
            description: ""
            subattributes:
              - name: "background"
                type: "string"
                description: ""

          - name: "shortLink"
            type: "string"
            description: ""

      - name: "card"
        type: "object"
        description: ""
        subattributes:
          - name: "closed"
            type: "boolean"
            description: ""

          - name: "desc"
            type: "string"
            description: ""

          - name: "id"
            type: "string"
            description: ""
            foreign-key-id: "card-id"

          - name: "idList"
            type: "string"
            description: ""
            foreign-key-id: "list-id"

          - name: "idMembers"
            type: "array"
            description: ""
            subattributes:
              - name: "value"
                type: "string"
                description: ""
                foreign-key-id: "user-id"

          - name: "idShort"
            type: "integer"
            description: ""

          - name: "name"
            type: "string"
            description: ""

          - name: "pos"
            type: "number"
            description: ""

          - name: "shortLink"
            type: "string"
            description: ""

      - name: "cardSource"
        type: "object"
        description: ""
        subattributes:
          - name: "id"
            type: "string"
            description: ""

          - name: "idShort"
            type: "integer"
            description: ""

          - name: "name"
            type: "string"
            description: ""

          - name: "shortLink"
            type: "string"
            description: ""

      - name: "deactivated"
        type: "boolean"
        description: ""

      - name: "idMember"
        type: "string"
        description: ""
        foreign-key-id: "user-id"

      - name: "idMemberAdded"
        type: "string"
        description: ""
        foreign-key-id: "user-id"

      - name: "idMemberInviter"
        type: "string"
        description: ""
        foreign-key-id: "user-id"

      - name: "list"
        type: "object"
        description: ""
        subattributes:
          - name: "closed"
            type: "boolean"
            description: ""

          - name: "id"
            type: "string"
            description: ""
            foreign-key-id: "list-id"

          - name: "name"
            type: "string"
            description: ""

          - name: "pos"
            type: "number"
            description: ""

      - name: "listAfter"
        type: "object"
        description: ""
        subattributes:
          - name: "id"
            type: "string"
            description: ""
            foreign-key-id: "list-id"

          - name: "name"
            type: "string"
            description: ""

      - name: "listBefore"
        type: "object"
        description: ""
        subattributes:
          - name: "id"
            type: "string"
            description: ""
            foreign-key-id: "list-id"

          - name: "name"
            type: "string"
            description: ""

      - name: "member"
        type: "object"
        description: ""
        subattributes:
          - name: "id"
            type: "string"
            description: ""
            foreign-key-id: "user-id"

          - name: "name"
            type: "string"
            description: ""

      - name: "memberType"
        type: "string"
        description: ""

      - name: "method"
        type: "string"
        description: ""

      - name: "old"
        type: "object"
        description: ""
        subattributes:
          - name: "closed"
            type: "boolean"
            description: ""

          - name: "desc"
            type: "string"
            description: ""

          - name: "idList"
            type: "string"
            description: ""
            foreign-key-id: "list-id"

          - name: "idMembers"
            type: "array"
            description: ""
            subattributes:
              - name: "value"
                type: "string"
                description: ""
                foreign-key-id: "user-id"

          - name: "name"
            type: "string"
            description: ""

          - name: "pos"
            type: "number"
            description: ""

          - name: "prefs"
            type: "object"
            description: ""
            subattributes:
              - name: "background"
                type: "string"
                description: ""
      
      - name: "organization"
        type: "object"
        description: ""
        subattributes:
          - name: "id"
            type: "string"
            description: ""
            foreign-key-id: "organization-id"

          - name: "name"
            type: "string"
            description: ""

      - name: "text"
        type: "string"
        description: ""
  
  - name: "idMemberCreator"
    type: "string"
    description: ""
    foreign-key-id: "user-id"

  - name: "limits"
    type: "object"
    description: ""
    subattributes:
      - name: "reactions"
        type: "object"
        description: ""
        subattributes:
          - name: "perAction"
            type: "object"
            description: ""
            subattributes:
              - name: "disableAt"
                type: "integer"
                description: ""

              - name: "status"
                type: "string"
                description: ""

              - name: "warnAt"
                type: "integer"
                description: ""

          - name: "uniquePerAction"
            type: "object"
            description: ""
            subattributes:
              - name: "disableAt"
                type: "integer"
                description: ""

              - name: "status"
                type: "string"
                description: ""

              - name: "warnAt"
                type: "integer"
                description: ""

  - name: "member"
    type: "object"
    description: ""
    subattributes:
      - name: "activityBlocked"
        type: "boolean"
        description: ""

      - name: "avatarHash"
        type: "string"
        description: ""

      - name: "avatarUrl"
        type: "string"
        description: ""

      - name: "fullName"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""
        foreign-key-id: "user-id"

      - name: "idMemberReferrer"
        type: "string"
        description: ""

      - name: "initials"
        type: "string"
        description: ""

      - name: "nonPublicAvailable"
        type: "boolean"
        description: ""

      - name: "username"
        type: "string"
        description: ""

  - name: "memberCreator"
    type: "object"
    description: ""
    subattributes:
      - name: "activityBlocked"
        type: "boolean"
        description: ""

      - name: "avatarHash"
        type: "string"
        description: ""

      - name: "avatarUrl"
        type: "string"
        description: ""

      - name: "fullName"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""
        foreign-key-id: "user-id"

      - name: "idMemberReferrer"
        type: "string"
        description: ""
        foreign-key-id: "user-id"

      - name: "initials"
        type: "string"
        description: ""

      - name: "nonPublicAvailable"
        type: "boolean"
        description: ""

      - name: "username"
        type: "string"
        description: ""

  - name: "type"
    type: "string"
    description: ""
---