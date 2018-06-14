---
tap: "hubspot"
version: "1.0"

name: "keywords"
doc-link: https://developers.hubspot.com/docs/methods/keywords/get_keyword
singer-schema: https://github.com/singer-io/tap-hubspot/blob/master/tap_hubspot/schemas/keywords.json
description: |
  The `keywords` table contains info about your HubSpot portal keywords.

notes: 

replication-method: "Key-based Incremental"
api-method:
  name: getAKeyword
  doc-link: https://developers.hubspot.com/docs/methods/keywords/get_keywords

attributes:
## Primary Key
  - name: "keyword_guid"
    type: "string"
    primary-key: true ## remove if this column isn't part of the table's PK
    description: "The GUID of the keyword."

  ## Replication Key
  - name: "created_at"
    type: "date-time"
    replication-key: true
    description: "The time the keyword was created."

  - name: "keyword"
    type: "string"
    description: "The text value of the keyword."

  - name: "country"
    type: "string"
    description: "If the keyword is localized, this column will contain the selected country's ID."
    doc-link: https://knowledge.hubspot.com/keyword-user-guide-v2/localizing-the-keywords-tool

  - name: "visits"
    type: "integer"
    description: "The number of visits attributed to the keyword."

  - name: "contacts"
    type: "integer"
    description: "The number of contacts attributed to the keyword."

  - name: "leads"
    type: "integer"
    description: "The number of leads attributed to the keyword."
---