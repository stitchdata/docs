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

  - name: "company"
    type: "string"
    description: ""

  - name: "contactHistogram"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "array"
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

  - name: "custom100"
    type: "string"
    description: ""

  - name: "custom101"
    type: "string"
    description: ""

  - name: "custom102"
    type: "string"
    description: ""

  - name: "custom103"
    type: "string"
    description: ""

  - name: "custom104"
    type: "string"
    description: ""

  - name: "custom105"
    type: "string"
    description: ""

  - name: "custom106"
    type: "string"
    description: ""

  - name: "custom107"
    type: "string"
    description: ""

  - name: "custom108"
    type: "string"
    description: ""

  - name: "custom109"
    type: "string"
    description: ""

  - name: "custom11"
    type: "string"
    description: ""

  - name: "custom110"
    type: "string"
    description: ""

  - name: "custom111"
    type: "string"
    description: ""

  - name: "custom112"
    type: "string"
    description: ""

  - name: "custom113"
    type: "string"
    description: ""

  - name: "custom114"
    type: "string"
    description: ""

  - name: "custom115"
    type: "string"
    description: ""

  - name: "custom116"
    type: "string"
    description: ""

  - name: "custom117"
    type: "string"
    description: ""

  - name: "custom118"
    type: "string"
    description: ""

  - name: "custom119"
    type: "string"
    description: ""

  - name: "custom12"
    type: "string"
    description: ""

  - name: "custom120"
    type: "string"
    description: ""

  - name: "custom121"
    type: "string"
    description: ""

  - name: "custom122"
    type: "string"
    description: ""

  - name: "custom123"
    type: "string"
    description: ""

  - name: "custom124"
    type: "string"
    description: ""

  - name: "custom125"
    type: "string"
    description: ""

  - name: "custom126"
    type: "string"
    description: ""

  - name: "custom127"
    type: "string"
    description: ""

  - name: "custom128"
    type: "string"
    description: ""

  - name: "custom129"
    type: "string"
    description: ""

  - name: "custom13"
    type: "string"
    description: ""

  - name: "custom130"
    type: "string"
    description: ""

  - name: "custom131"
    type: "string"
    description: ""

  - name: "custom132"
    type: "string"
    description: ""

  - name: "custom133"
    type: "string"
    description: ""

  - name: "custom134"
    type: "string"
    description: ""

  - name: "custom135"
    type: "string"
    description: ""

  - name: "custom136"
    type: "string"
    description: ""

  - name: "custom137"
    type: "string"
    description: ""

  - name: "custom138"
    type: "string"
    description: ""

  - name: "custom139"
    type: "string"
    description: ""

  - name: "custom14"
    type: "string"
    description: ""

  - name: "custom140"
    type: "string"
    description: ""

  - name: "custom141"
    type: "string"
    description: ""

  - name: "custom142"
    type: "string"
    description: ""

  - name: "custom143"
    type: "string"
    description: ""

  - name: "custom144"
    type: "string"
    description: ""

  - name: "custom145"
    type: "string"
    description: ""

  - name: "custom146"
    type: "string"
    description: ""

  - name: "custom147"
    type: "string"
    description: ""

  - name: "custom148"
    type: "string"
    description: ""

  - name: "custom149"
    type: "string"
    description: ""

  - name: "custom15"
    type: "string"
    description: ""

  - name: "custom150"
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

  - name: "custom56"
    type: "string"
    description: ""

  - name: "custom57"
    type: "string"
    description: ""

  - name: "custom58"
    type: "string"
    description: ""

  - name: "custom59"
    type: "string"
    description: ""

  - name: "custom6"
    type: "string"
    description: ""

  - name: "custom60"
    type: "string"
    description: ""

  - name: "custom61"
    type: "string"
    description: ""

  - name: "custom62"
    type: "string"
    description: ""

  - name: "custom63"
    type: "string"
    description: ""

  - name: "custom64"
    type: "string"
    description: ""

  - name: "custom65"
    type: "string"
    description: ""

  - name: "custom66"
    type: "string"
    description: ""

  - name: "custom67"
    type: "string"
    description: ""

  - name: "custom68"
    type: "string"
    description: ""

  - name: "custom69"
    type: "string"
    description: ""

  - name: "custom7"
    type: "string"
    description: ""

  - name: "custom70"
    type: "string"
    description: ""

  - name: "custom71"
    type: "string"
    description: ""

  - name: "custom72"
    type: "string"
    description: ""

  - name: "custom73"
    type: "string"
    description: ""

  - name: "custom74"
    type: "string"
    description: ""

  - name: "custom75"
    type: "string"
    description: ""

  - name: "custom76"
    type: "string"
    description: ""

  - name: "custom77"
    type: "string"
    description: ""

  - name: "custom78"
    type: "string"
    description: ""

  - name: "custom79"
    type: "string"
    description: ""

  - name: "custom8"
    type: "string"
    description: ""

  - name: "custom80"
    type: "string"
    description: ""

  - name: "custom81"
    type: "string"
    description: ""

  - name: "custom82"
    type: "string"
    description: ""

  - name: "custom83"
    type: "string"
    description: ""

  - name: "custom84"
    type: "string"
    description: ""

  - name: "custom85"
    type: "string"
    description: ""

  - name: "custom86"
    type: "string"
    description: ""

  - name: "custom87"
    type: "string"
    description: ""

  - name: "custom88"
    type: "string"
    description: ""

  - name: "custom89"
    type: "string"
    description: ""

  - name: "custom9"
    type: "string"
    description: ""

  - name: "custom90"
    type: "string"
    description: ""

  - name: "custom91"
    type: "string"
    description: ""

  - name: "custom92"
    type: "string"
    description: ""

  - name: "custom93"
    type: "string"
    description: ""

  - name: "custom94"
    type: "string"
    description: ""

  - name: "custom95"
    type: "string"
    description: ""

  - name: "custom96"
    type: "string"
    description: ""

  - name: "custom97"
    type: "string"
    description: ""

  - name: "custom98"
    type: "string"
    description: ""

  - name: "custom99"
    type: "string"
    description: ""

  - name: "dateOfBirth"
    type: "date-time"
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
    - name: "items"
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
    type: "array"
    description: ""
    subattributes:
    - name: "items"
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
    - name: "items"
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
    - name: "items"
      type: "string"
      description: ""

  - name: "ownerId"
    type: "integer"
    description: ""

  - name: "personaId"
    type: "integer"
    description: ""

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
    type: "number"
    description: ""

  - name: "sharingTeamId"
    type: "string"
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
    - name: "items"
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

  - name: "trashedAt"
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
    - name: "items"
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
    - name: "items"
      type: "string"
      description: ""
---