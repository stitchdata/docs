---
tap: "trello"
version: "1"
key: "checklist"

name: "checklists"
doc-link: "https://developer.atlassian.com/cloud/trello/rest/#api-checklists-id-get"
singer-schema: "https://github.com/singer-io/tap-trello/blob/master/tap_trello/schemas/checklists.json"
description: |
  The {{ table.name }} table contains info about checklists on boards that the user who authorized the connection is a member of.

  **Note**: To replicate this table, the [boards](#boards) table must be set to replicate.

replication-method: "Full Table"

api-method:
    name: "Get a Checklist"
    doc-link: "https://developer.atlassian.com/cloud/trello/rest/#api-checklists-id-get"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The checklist ID." 
    foreign-key-id: "checklist-id"

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
        type: "string"
        description: ""

      - name: "comments"
        type: "integer"
        description: ""

      - name: "description"
        type: "boolean"
        description: ""

      - name: "due"
        type: "string"
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
    type: "string"
    description: ""

  - name: "checkItems"
    type: "array"
    description: ""
    subattributes:
      - name: "creationMethod"
        type: "string"
        description: ""

      - name: "due"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""

      - name: "idChecklist"
        type: "string"
        description: ""
        foreign-key-id: "checklist-id"

      - name: "idMember"
        type: "string"
        description: ""
        foreign-key-id: "user-id"

      - name: "name"
        type: "string"
        description: ""

      - name: "nameData"
        type: "string"
        description: ""

      - name: "pos"
        type: "number"
        description: ""

      - name: "state"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
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
        type: "string"
        description: ""

      - name: "size"
        type: "string"
        description: ""

  - name: "creationMethod"
    type: "string"
    description: ""

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
              - name: "permissionLevel"
                type: "string"
                description: ""

              - name: "selfJoin"
                type: "boolean"
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

          - name: "due"
            type: "string"
            description: ""

          - name: "dueComplete"
            type: "boolean"
            description: ""

          - name: "id"
            type: "string"
            description: "The card ID."
            foreign-key-id: "card-id"

          - name: "idShort"
            type: "integer"
            description: ""

          - name: "name"
            type: "string"
            description: ""

          - name: "shortLink"
            type: "string"
            description: ""

      - name: "checklist"
        type: "object"
        description: ""
        subattributes:
          - name: "id"
            type: "string"
            description: ""
            foreign-key-id: "checklist-id"

          - name: "name"
            type: "string"
            description: ""

      - name: "creationMethod"
        type: "string"
        description: ""

      - name: "list"
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

      - name: "old"
        type: "object"
        description: ""
        subattributes:
          - name: "closed"
            type: "boolean"
            description: ""

          - name: "due"
            type: "string"
            description: ""

          - name: "dueComplete"
            type: "boolean"
            description: ""

          - name: "name"
            type: "string"
            description: ""

          - name: "prefs"
            type: "object"
            description: ""
            subattributes:
              - name: "permissionLevel"
                type: "string"
                description: ""

              - name: "selfJoin"
                type: "boolean"
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

  - name: "date"
    type: "string"
    description: ""

  - name: "dateLastActivity"
    type: "string"
    description: "The date the checklist last had activity on it."
  
  - name: "dateLastView"
    type: "string"
    description: ""

  - name: "datePluginDisable"
    type: "string"
    description: ""

  - name: "desc"
    type: "string"
    description: ""

  - name: "descData"
    type: "string"
    description: ""

  - name: "due"
    type: "string"
    description: ""

  - name: "dueComplete"
    type: "boolean"
    description: ""

  - name: "dueReminder"
    type: "string"
    description: ""

  - name: "enterpriseOwned"
    type: "boolean"
    description: ""

  - name: "fullName"
    type: "string"
    description: ""
  
  - name: "idAttachmentCover"
    type: "string"
    description: ""

  - name: "idBoard"
    type: "string"
    description: ""
    foreign-key-id: "board-id"

  - name: "idBoardSource"
    type: "string"
    description: ""

  - name: "idCard"
    type: "string"
    description: ""
    foreign-key-id: "card-id"

  - name: "idChecklists"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "idEnterprise"
    type: "string"
    description: ""

  - name: "idList"
    type: "string"
    description: ""
    foreign-key-id: "list-id"

  - name: "idMemberCreator"
    type: "string"
    description: ""
    foreign-key-id: "user-id"

  - name: "idOrganization"
    type: "string"
    description: ""
    foreign-key-id: "organization-id"

  - name: "idShort"
    type: "integer"
    description: ""

  - name: "isTemplate"
    type: "boolean"
    description: ""

  - name: "ixUpdate"
    type: "string"
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
      - name: "checkItems"
        type: "object"
        description: ""
        subattributes:
          - name: "perChecklist"
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

  - name: "manualCoverAttachment"
    type: "boolean"
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

      - name: "initials"
        type: "string"
        description: ""

      - name: "nonPublicAvailable"
        type: "boolean"
        description: ""

      - name: "username"
        type: "string"
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

      - name: "backgroundBottomColor"
        type: "string"
        description: ""

      - name: "backgroundBrightness"
        type: "string"
        description: ""

      - name: "backgroundColor"
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

  - name: "shortLink"
    type: "string"
    description: ""

  - name: "shortUrl"
    type: "string"
    description: ""

  - name: "softLimit"
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

  - name: "type"
    type: "string"
    description: ""

  - name: "url"
    type: "string"
    description: ""

  - name: "username"
    type: "string"
    description: ""
---