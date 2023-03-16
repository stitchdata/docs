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

  - name: "custom4"
    type: "string"
    description: ""

  - name: "custom5"
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

  - name: "tags"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "updaterId"
    type: "integer"
    description: ""
    foreign-key-id: "user-id"

  - name: "websiteUrl"
    type: "string"
    description: ""
---