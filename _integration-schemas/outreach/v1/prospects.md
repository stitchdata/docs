---
tap: "outreach"
version: "1"

name: "prospects"
doc-link: "https://api.outreach.io/api/v2/docs#prospect"
singer-schema: "https://github.com/singer-io/tap-outreach/blob/master/tap_outreach/schemas/prospects.json"
description: |
  The `{{ table.name}}` table contains information about your prospects.

replication-method: "Key-based Incremental"

api-method:
    name: "Prospect"
    doc-link: "https://api.outreach.io/api/v2/docs#prospect"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The prospect ID."
    foreign-key-id: "prospect-id"

  - name: "updatedAt"
    type: "date-time"
    replication-key: true
    description: "The time the prospect was last updated."

  - name: "accountId"
    type: "integer"
    description: ""
    foreign-key-id: "account-id"

  - name: "addedAt"
    type: "date-time"
    description: ""

  - name: "addressCity"
    type: "string"
    description: ""

  - name: "addressCountry"
    type: "string"
    description: ""

  - name: "addressState"
    type: "string"
    description: ""

  - name: "addressStreet"
    type: "string"
    description: ""

  - name: "addressStreet2"
    type: "string"
    description: ""

  - name: "addressZip"
    type: "string"
    description: ""

  - name: "angelListUrl"
    type: "string"
    description: ""

  - name: "availableAt"
    type: "date-time"
    description: ""

  - name: "callOptedOut"
    type: "boolean"
    description: ""

  - name: "callsOptStatus"
    type: "string"
    description: ""

  - name: "callsOptedAt"
    type: "date-time"
    description: ""

  - name: "campaignName"
    type: "string"
    description: ""

  - name: "clickCount"
    type: "integer"
    description: ""

  - name: "contactHistogram"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "integer"
            description: ""

  - name: "createdAt"
    type: "date-time"
    description: ""

  - name: "creatorId"
    type: "integer"
    description: ""
    foreign-key-id: "user-id"

  - name: "custom1"
    type: "string"
    description: ""

  - name: "custom10"
    type: "string"
    description: ""

  - name: "custom11"
    type: "string"
    description: ""

  - name: "custom12"
    type: "string"
    description: ""

  - name: "custom13"
    type: "string"
    description: ""

  - name: "custom14"
    type: "string"
    description: ""

  - name: "custom15"
    type: "string"
    description: ""

  - name: "custom16"
    type: "string"
    description: ""

  - name: "custom17"
    type: "string"
    description: ""

  - name: "custom18"
    type: "string"
    description: ""

  - name: "custom19"
    type: "string"
    description: ""

  - name: "custom2"
    type: "string"
    description: ""

  - name: "custom20"
    type: "string"
    description: ""

  - name: "custom21"
    type: "string"
    description: ""

  - name: "custom22"
    type: "string"
    description: ""

  - name: "custom23"
    type: "string"
    description: ""

  - name: "custom24"
    type: "string"
    description: ""

  - name: "custom25"
    type: "string"
    description: ""

  - name: "custom26"
    type: "string"
    description: ""

  - name: "custom27"
    type: "string"
    description: ""

  - name: "custom28"
    type: "string"
    description: ""

  - name: "custom29"
    type: "string"
    description: ""

  - name: "custom3"
    type: "string"
    description: ""

  - name: "custom30"
    type: "string"
    description: ""

  - name: "custom31"
    type: "string"
    description: ""

  - name: "custom32"
    type: "string"
    description: ""

  - name: "custom33"
    type: "string"
    description: ""

  - name: "custom34"
    type: "string"
    description: ""

  - name: "custom35"
    type: "string"
    description: ""

  - name: "custom36"
    type: "string"
    description: ""

  - name: "custom37"
    type: "string"
    description: ""

  - name: "custom38"
    type: "string"
    description: ""

  - name: "custom39"
    type: "string"
    description: ""

  - name: "custom4"
    type: "string"
    description: ""

  - name: "custom40"
    type: "string"
    description: ""

  - name: "custom41"
    type: "string"
    description: ""

  - name: "custom42"
    type: "string"
    description: ""

  - name: "custom43"
    type: "string"
    description: ""

  - name: "custom44"
    type: "string"
    description: ""

  - name: "custom45"
    type: "string"
    description: ""

  - name: "custom46"
    type: "string"
    description: ""

  - name: "custom47"
    type: "string"
    description: ""

  - name: "custom48"
    type: "string"
    description: ""

  - name: "custom49"
    type: "string"
    description: ""

  - name: "custom5"
    type: "string"
    description: ""

  - name: "custom50"
    type: "string"
    description: ""

  - name: "custom51"
    type: "string"
    description: ""

  - name: "custom52"
    type: "string"
    description: ""

  - name: "custom53"
    type: "string"
    description: ""

  - name: "custom54"
    type: "string"
    description: ""

  - name: "custom55"
    type: "string"
    description: ""

  - name: "custom6"
    type: "string"
    description: ""

  - name: "custom7"
    type: "string"
    description: ""

  - name: "custom8"
    type: "string"
    description: ""

  - name: "custom9"
    type: "string"
    description: ""

  - name: "dateOfBirth"
    type: "date-time"
    description: ""

  - name: "defaultPluginMappingId"
    type: "integer"
    description: ""

  - name: "degree"
    type: "string"
    description: ""

  - name: "emailOptedOut"
    type: "boolean"
    description: ""

  - name: "emails"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "emailsOptStatus"
    type: "string"
    description: ""

  - name: "emailsOptedAt"
    type: "date-time"
    description: ""

  - name: "engagedAt"
    type: "date-time"
    description: ""

  - name: "engagedScore"
    type: "number"
    description: ""

  - name: "eventName"
    type: "string"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "externalOwner"
    type: "string"
    description: ""

  - name: "externalSource"
    type: "string"
    description: ""

  - name: "facebookUrl"
    type: "string"
    description: ""

  - name: "firstName"
    type: "string"
    description: ""

  - name: "gender"
    type: "string"
    description: ""

  - name: "githubUrl"
    type: "string"
    description: ""

  - name: "githubUsername"
    type: "string"
    description: ""

  - name: "googlePlusUrl"
    type: "string"
    description: ""

  - name: "graduationDate"
    type: "date-time"
    description: ""

  - name: "homePhones"
    type: "string"
    description: ""

  - name: "jobStartDate"
    type: "date-time"
    description: ""

  - name: "lastName"
    type: "string"
    description: ""

  - name: "linkedInConnections"
    type: "integer"
    description: ""

  - name: "linkedInId"
    type: "string"
    description: ""

  - name: "linkedInSlug"
    type: "string"
    description: ""

  - name: "linkedInUrl"
    type: "string"
    description: ""

  - name: "middleName"
    type: "string"
    description: ""

  - name: "mobilePhones"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nickname"
    type: "string"
    description: ""

  - name: "occupation"
    type: "string"
    description: ""

  - name: "openCount"
    type: "integer"
    description: ""

  - name: "optedOut"
    type: "boolean"
    description: ""

  - name: "optedOutAt"
    type: "date-time"
    description: ""

  - name: "otherPhones"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "ownerId"
    type: "integer"
    description: ""
    foreign-key-id: "user-id"

  - name: "personaId"
    type: "integer"
    description: ""
    foreign-key-id: "persona-id"

  - name: "personalNote1"
    type: "string"
    description: ""

  - name: "personalNote2"
    type: "string"
    description: ""

  - name: "preferredContact"
    type: "string"
    description: ""

  - name: "quoraUrl"
    type: "string"
    description: ""

  - name: "region"
    type: "string"
    description: ""

  - name: "replyCount"
    type: "integer"
    description: ""

  - name: "school"
    type: "string"
    description: ""

  - name: "score"
    type: "integer"
    description: ""

  - name: "smsOptStatus"
    type: "string"
    description: ""

  - name: "smsOptedAt"
    type: "date-time"
    description: ""

  - name: "smsOptedOut"
    type: "boolean"
    description: ""

  - name: "source"
    type: "string"
    description: ""

  - name: "specialties"
    type: "string"
    description: ""

  - name: "stackOverflowId"
    type: "string"
    description: ""

  - name: "stackOverflowUrl"
    type: "string"
    description: ""

  - name: "stageId"
    type: "integer"
    description: ""
    foreign-key-id: "stage-id"

  - name: "tags"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "timeZone"
    type: "string"
    description: ""

  - name: "timeZoneIana"
    type: "string"
    description: ""

  - name: "timeZoneInferred"
    type: "string"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "touchedAt"
    type: "date-time"
    description: ""

  - name: "twitterUrl"
    type: "string"
    description: ""

  - name: "twitterUsername"
    type: "string"
    description: ""

  - name: "updaterId"
    type: "integer"
    description: ""
    foreign-key-id: "user-id"

  - name: "voipPhones"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "websiteUrl1"
    type: "string"
    description: ""

  - name: "websiteUrl2"
    type: "string"
    description: ""

  - name: "websiteUrl3"
    type: "string"
    description: ""

  - name: "workPhones"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""
---