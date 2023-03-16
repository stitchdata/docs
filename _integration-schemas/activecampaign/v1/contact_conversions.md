---
tap: "activecampaign"
version: "0.3"
key: ""

name: "contact_conversions"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/contact_conversions.json"
description: ""

replication-method: "Key-based Incremental"

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The contact conversion ID."
    #foreign-key-id: "contact-conversion-id"

  - name: "cdate"
    type: "date-time"
    description: "The date the contact conversion was created."
    replication-key: true

  - name: "contact"
    type: "integer"
    description: "The contact ID."
    foreign-key-id: "contact-id"
  - name: "conversion"
    type: "integer"
    description: "The conversion ID."
    foreign-key-id: "conversion-id"
  - name: "conversion_trigger"
    type: "integer"
    description: ""
  - name: "conversiontrigger"
    type: "integer"
    description: "The conversion trigger ID."
    foreign-key-id: "conversion-trigger-id"
  - name: "converted_by"
    type: "integer"
    description: ""
  - name: "converted_by_id"
    type: "integer"
    description: ""
  - name: "converted_by_type"
    type: "string"
    description: ""
  - name: "currency"
    type: "string"
    description: ""
  - name: "dynamic"
    type: "integer"
    description: ""
  
  - name: "modifier"
    type: "string"
    description: ""
  - name: "trigger_type"
    type: "string"
    description: ""
  - name: "value"
    type: "integer"
    description: ""
---
