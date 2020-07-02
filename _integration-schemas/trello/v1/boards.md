---
tap: "trello"
version: "1"
key: "board"

name: "boards"
doc-link: "https://developer.atlassian.com/cloud/trello/rest/#api-boards-id-get"
singer-schema: "https://github.com/singer-io/tap-trello/blob/master/tap_trello/schemas/boards.json"
description: |
  The {{ table.name }} table contains info about the boards that the [authorizing user](#data-replication-board-membership) is a member of.

  #### Custom field support

  Custom fields are supported for this table.

replication-method: "Full Table"

supports-custom-fields: true

api-method:
    name: "Get boards that a member belongs to"
    doc-link: "https://developer.atlassian.com/cloud/trello/rest/#api-members-id-boards-get"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The board ID."
    foreign-key-id: "board-id"

  - name: "closed"
    type: "boolean"
    description: ""

  - name: "creationMethod"
    type: "string"
    description: ""

  - name: "dateLastActivity"
    type: "date-time"
    description: "The date the board last had activity on it."
  
  - name: "dateLastView"
    type: "date-time"
    description: ""

  - name: "datePluginDisable"
    type: "date-time"
    description: ""

  - name: "desc"
    type: "string"
    description: ""

  - name: "descData"
    type: "string"
    description: ""

  - name: "enterpriseOwned"
    type: "boolean"
    description: ""
  
  - name: "idBoardSource"
    type: "string"
    description: ""

  - name: "idEnterprise"
    type: "string"
    description: ""

  - name: "idOrganization"
    type: "string"
    description: ""
    # foreign-key-id: "organization-id"

  - name: "idTags"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""
        foreign-key-id: "tag-id"

  - name: "ixUpdate"
    type: "integer"
    description: ""

  - name: "labelNames"
    type: "object"
    description: ""
    subattributes:
      - name: "black"
        type: "string"
        description: ""

      - name: "blue"
        type: "string"
        description: ""

      - name: "green"
        type: "string"
        description: ""

      - name: "lime"
        type: "string"
        description: ""

      - name: "orange"
        type: "string"
        description: ""

      - name: "pink"
        type: "string"
        description: ""

      - name: "purple"
        type: "string"
        description: ""

      - name: "red"
        type: "string"
        description: ""

      - name: "sky"
        type: "string"
        description: ""

      - name: "yellow"
        type: "string"
        description: ""

  - name: "limits"
    type: "object"
    description: ""
    subattributes:
      - name: "attachments"
        type: "object"
        description: ""
        subattributes:
          - name: "perBoard"
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

  - name: "memberships"
    type: "array"
    description: ""
    subattributes:
      - name: "deactivated"
        type: "boolean"
        description: ""

      - name: "id"
        type: "string"
        description: ""

      - name: "idMember"
        type: "string"
        description: ""
        foreign-key-id: "user-id"

      - name: "memberType"
        type: "string"
        description: ""

      - name: "unconfirmed"
        type: "boolean"
        description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "pinned"
    type: "boolean"
    description: ""

  - name: "powerUps"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "prefs"
    type: "object"
    description: ""
    subattributes:
      - name: "background"
        type: "string"
        description: ""
      - name: "backgroundBottomColor"
        type: "string"
        description: ""
      - name: "backgroundBrightness"
        type: "string"
        description: ""
      - name: "backgroundImage"
        type: "string"
        description: ""
      - name: "backgroundImageScaled"
        type: "array"
        description: ""
        subattributes:
          - name: "height"
            type: "integer"
            description: ""
          - name: "url"
            type: "string"
            description: ""
          - name: "width"
            type: "integer"
            description: ""
      - name: "backgroundTile"
        type: "boolean"
        description: ""
      - name: "backgroundTopColor"
        type: "string"
        description: ""
      - name: "calendarFeedEnabled"
        type: "boolean"
        description: ""
      - name: "canBeEnterprise"
        type: "boolean"
        description: ""
      - name: "canBeOrg"
        type: "boolean"
        description: ""
      - name: "canBePrivate"
        type: "boolean"
        description: ""
      - name: "canBePublic"
        type: "boolean"
        description: ""
      - name: "canInvite"
        type: "boolean"
        description: ""
      - name: "cardAging"
        type: "string"
        description: ""
      - name: "cardCovers"
        type: "boolean"
        description: ""
      - name: "comments"
        type: "string"
        description: ""
      - name: "hideVotes"
        type: "boolean"
        description: ""
      - name: "invitations"
        type: "string"
        description: ""
      - name: "isTemplate"
        type: "boolean"
        description: ""
      - name: "permissionLevel"
        type: "string"
        description: ""
      - name: "selfJoin"
        type: "boolean"
        description: ""
      - name: "voting"
        type: "string"
        description: ""

  - name: "premiumFeatures"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "shortLink"
    type: "string"
    description: ""

  - name: "shortUrl"
    type: "string"
    description: ""

  - name: "starred"
    type: "boolean"
    description: ""

  - name: "subscribed"
    type: "boolean"
    description: ""

  - name: "templateGallery"
    type: "string"
    description: ""

  - name: "url"
    type: "string"
    description: ""
---