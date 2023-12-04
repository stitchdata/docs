---
tap: "activecampaign"
version: "1"
key: ""

name: "contact_tags"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/contact_tags.json"
description: ""

replication-method: "Key-based Incremental"

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The contact tag ID."
    #foreign-key-id: "contact-tag-id"

  - name: "updated_timestamp"
    type: "date-time"
    description: "The time the contact tag was last updated."
    replication-key: true

  - name: "cdate"
    type: "date-time"
    description: ""
  - name: "contact"
    type: "integer"
    description: "The contact ID."
    foreign-key-id: "contact-id"
  - name: "created_by"
    type: "integer"
    description: ""
  - name: "created_timestamp"
    type: "date-time"
    description: ""
  
  - name: "tag"
    type: "integer"
    description: "The tag ID."
    foreign-key-id: "tag-id"
  - name: "updated_by"
    type: "integer"
    description: ""

---
