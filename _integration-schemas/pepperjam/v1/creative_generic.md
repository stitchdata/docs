---
tap: "pepperjam"
version: "1"
key: "creative_generic"

name: "creative_generic"
doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#Generic"
singer-schema: "https://github.com/singer-io/tap-pepperjam/blob/master/tap_pepperjam/schemas/creative_generic.json"
description: |
  The {{ table.name }} table contains information about generic link creatives in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "getGenericLinkCreative"
    doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#Generic"

attributes:
  - name: "type"
    type: "string"
    primary-key: true
    description: "The type of generic link."
    #foreign-key-id: "type-id"
    
  - name: "modified"
    type: "date-time"
    description: "The last time the generic link was modified."
    replication-key: true
      
  - name: "allow_deep_link"
    type: "integer"
    description: ""
  - name: "url"
    type: "string"
    description: ""
---
