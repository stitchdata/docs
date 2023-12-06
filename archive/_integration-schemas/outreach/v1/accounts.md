---
tap: "outreach"
version: "1"
key: "account"

name: "accounts"
doc-link: "https://api.outreach.io/api/v2/docs#account"
singer-schema: "https://github.com/singer-io/tap-outreach/blob/master/tap_outreach/schemas/accounts.json"
description: |
  The `{{ table.name }}` table contains information about prospective clients in {{ integration.display_name }}.

replication-method: "Key-based Incremental"

api-method:
  name: "Get accounts"
  doc-link: "https://api.outreach.io/api/v2/docs#account"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The account ID"
    foreign-key-id: "account-id"

  - name: "updatedAt"
    type: "date-time"
    description: "The time the account was last updated."
    replication-key: true

  - name: "buyerIntentScore"
    type: "number"
    description: ""

  - name: "companyType"
    type: "string"
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

  - name: "customId"
    type: "string"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "domain"
    type: "string"
    description: ""

  - name: "externalSource"
    type: "string"
    description: ""

  - name: "followers"
    type: "integer"
    description: ""

  - name: "foundedAt"
    type: "date-time"
    description: ""

  - name: "industry"
    type: "string"
    description: ""

  - name: "linkedInEmployees"
    type: "integer"
    description: ""

  - name: "linkedInUrl"
    type: "string"
    description: ""

  - name: "locality"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "named"
    type: "boolean"
    description: ""

  - name: "naturalName"
    type: "string"
    description: ""

  - name: "numberOfEmployees"
    type: "integer"
    description: ""

  - name: "ownerId"
    type: "integer"
    description: ""
    foreign-key-id: "user-id"

  - name: "sharingTeamId"
    type: "string"
    description: ""

  - name: "tags"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "touchedAt"
    type: "date-time"
    description: ""

  - name: "updaterId"
    type: "integer"
    description: ""
    foreign-key-id: "user-id"

  - name: "websiteUrl"
    type: "string"
    description: ""
---