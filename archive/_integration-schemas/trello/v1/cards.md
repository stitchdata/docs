---
tap: "trello"
version: "1"
key: "card"

name: "cards"
doc-link: "https://developer.atlassian.com/cloud/trello/rest/#api-cards-id-get"
singer-schema: "https://github.com/singer-io/tap-trello/blob/master/tap_trello/schemas/cards.json"
description: |
  The {{ table.name }} table contains info about all of the cards on boards that [authorizing user](#data-replication-board-membership) is a member of.

  #### Custom field support

  Custom fields are supported for this table.

replication-method: "Full Table"

supports-custom-fields: true

api-method:
    name: "Get filtered cards on a board"
    doc-link: "https://developer.atlassian.com/cloud/trello/rest/#api-boards-id-cards-filter-get"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The card ID."
    foreign-key-id: "card-id"

  - name: "badges"
    type: "object"
    description: ""
    subattributes:
      - name: "attachments"
        type: "integer"
        description: ""

      - name: "attachmentsByType"
        type: "object"
        description: ""
        subattributes:
          - name: "trello"
            type: "object"
            description: ""
            subattributes:
              - name: "board"
                type: "integer"
                description: ""

              - name: "card"
                type: "integer"
                description: ""

      - name: "checkItems"
        type: "integer"
        description: ""

      - name: "checkItemsChecked"
        type: "integer"
        description: ""

      - name: "checkItemsEarliestDue"
        type: "date-time"
        description: ""

      - name: "comments"
        type: "integer"
        description: ""

      - name: "description"
        type: "boolean"
        description: ""

      - name: "due"
        type: "date-time"
        description: ""

      - name: "dueComplete"
        type: "boolean"
        description: ""

      - name: "fogbugz"
        type: "string"
        description: ""

      - name: "location"
        type: "boolean"
        description: ""

      - name: "subscribed"
        type: "boolean"
        description: ""

      - name: "viewingMemberVoted"
        type: "boolean"
        description: ""

      - name: "votes"
        type: "integer"
        description: ""

  - name: "checkItemStates"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "anything"
        description: ""

  - name: "closed"
    type: "boolean"
    description: ""

  - name: "cover"
    type: "object"
    description: ""
    subattributes:
      - name: "brightness"
        type: "string"
        description: ""

      - name: "color"
        type: "string"
        description: ""

      - name: "idAttachment"
        type: "string"
        description: ""

      - name: "idUploadedBackground"
        type: "boolean"
        description: ""

      - name: "size"
        type: "string"
        description: ""

  - name: "customFieldItems"
    type: "array"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""

      - name: "idCustomField"
        type: "string"
        description: ""

      - name: "idModel"
        type: "string"
        description: ""

      - name: "idValue"
        type: "string"
        description: ""

      - name: "modelType"
        type: "string"
        description: ""

      - name: "value"
        type: "object"
        description: ""
        subattributes:
          - name: "checked"
            type: "string"
            description: ""

          - name: "date"
            type: "string"
            description: ""

          - name: "number"
            type: "string"
            description: ""

          - name: "option"
            type: "string"
            description: ""

          - name: "text"
            type: "string"
            description: ""

  - name: "dateLastActivity"
    type: "date-time"
    description: "The date the card last had activity on it."
  
  - name: "desc"
    type: "string"
    description: ""

  - name: "descData"
    type: "object"
    description: ""
    subattributes:
      - name: "emoji"
        type: "object"
        description: ""

  - name: "due"
    type: "date-time"
    description: ""

  - name: "dueComplete"
    type: "boolean"
    description: ""

  - name: "dueReminder"
    type: "string"
    description: ""
  
  - name: "idAttachmentCover"
    type: "string"
    description: ""

  - name: "idBoard"
    type: "string"
    description: ""
    foreign-key-id: "board-id"

  - name: "idChecklists"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""
        foreign-key-id: "checklist-id"

  - name: "idLabels"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""
        # foreign-key-id: "label-id"

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

  - name: "idMembersVoted"
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

  - name: "isTemplate"
    type: "boolean"
    description: ""

  - name: "labels"
    type: "array"
    description: ""
    subattributes:
      - name: "color"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""
        # foreign-key-id: "label-id"

      - name: "idBoard"
        type: "string"
        description: ""
        foreign-key-id: "board-id"

      - name: "name"
        type: "string"
        description: ""

  - name: "manualCoverAttachment"
    type: "boolean"
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

  - name: "shortUrl"
    type: "string"
    description: ""

  - name: "subscribed"
    type: "boolean"
    description: ""

  - name: "url"
    type: "string"
    description: ""
---