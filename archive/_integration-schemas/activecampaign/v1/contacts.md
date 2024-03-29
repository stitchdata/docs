---
tap: "activecampaign"
version: "1"
key: ""

name: "contacts"
doc-link: "https://developers.activecampaign.com/reference#contact"
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/contacts.json"
description: |
  The `{{ table.name }}` table contains information about the people that you market or sell to in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List, search, and filter contacts"
    doc-link: "https://developers.activecampaign.com/reference#list-all-contacts"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The contact ID."
    foreign-key-id: "contact-id"

  - name: "updated_timestamp"
    type: "date-time"
    description: "The time the contact was last updated."
    replication-key: true

  - name: "account_contacts"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "integer"
        description: ""
  - name: "adate"
    type: "date-time"
    description: ""
  - name: "anonymized"
    type: "integer"
    description: ""
  - name: "bounced_date"
    type: "string"
    description: ""
  - name: "bounced_hard"
    type: "integer"
    description: ""
  - name: "bounced_soft"
    type: "integer"
    description: ""
  - name: "cdate"
    type: "date-time"
    description: ""
  - name: "created_by"
    type: "integer"
    description: ""
  - name: "created_timestamp"
    type: "date-time"
    description: ""
  - name: "created_utc_timestamp"
    type: "date-time"
    description: ""
  - name: "deleted"
    type: "integer"
    description: ""
  - name: "deleted_at"
    type: "date-time"
    description: ""
  - name: "edate"
    type: "date-time"
    description: ""
  - name: "email"
    type: "string"
    description: ""
  - name: "email_domain"
    type: "string"
    description: ""
  - name: "email_empty"
    type: "boolean"
    description: ""
  - name: "email_local"
    type: "string"
    description: ""
  - name: "first_name"
    type: "string"
    description: ""
  - name: "gravatar"
    type: "integer"
    description: ""
  - name: "hash"
    type: "string"
    description: ""
  
  - name: "ip"
    type: "string"
    description: ""
  - name: "last_name"
    type: "string"
    description: ""
  - name: "organization"
    type: "integer"
    description: ""
  - name: "orgid"
    type: "integer"
    description: ""
  - name: "phone"
    type: "string"
    description: ""
  - name: "rating_tstamp"
    type: "string"
    description: ""
  - name: "score_values"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "integer"
        description: ""
  - name: "segmentio_id"
    type: "string"
    description: ""
  - name: "sentcnt"
    type: "integer"
    description: ""
  - name: "socialdata_lastcheck"
    type: "date-time"
    description: ""
  - name: "ua"
    type: "string"
    description: ""
  - name: "udate"
    type: "date-time"
    description: ""
  - name: "updated_by"
    type: "integer"
    description: ""
  
  - name: "updated_utc_timestamp"
    type: "date-time"
    description: ""
---
