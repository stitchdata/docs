---
tap: "klaviyo"
version: "1.0"

name: "global_exclusions"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-klaviyo/blob/master/tap_klaviyo/schemas/global_exclusions.json"
description: |
  The {{ table.name }} table contains info about the global exclusions in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
    name: "Lists in Accounts"
    doc-link: "https://www.klaviyo.com/docs/api/lists#lists"

attributes:
  - name: "email"
    type: "string"
    primary-key: true
    description: "This is the of the globally excluded emails."
#    foreign-key-id: "exclusion-id"
  
  - name: "object"
    type: "string"
    description: ""
  
  - name: "reason"
    type: "string"
    description: ""
  
  - name: "timestamp"
    type: "string"
    description: ""
---
