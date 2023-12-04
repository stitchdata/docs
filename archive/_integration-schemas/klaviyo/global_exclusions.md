---
tap: "klaviyo"
version: "1"
key: "global-exclusion"

name: "global_exclusions"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-klaviyo/blob/master/tap_klaviyo/schemas/global_exclusions.json"
description: |
  The {{ table.name }} table contains info about the global exclusions in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "Get global exclusions"
  doc-link: "https://apidocs.klaviyo.com/reference/lists-segments#get-global-exclusions"

attributes:
  - name: "email"
    type: "string"
    primary-key: true
    description: ""
  
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