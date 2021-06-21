---
tap: "mambu"
version: "1"
key: ""

name: "index_rate_sources"
doc-link: "https://api.mambu.com/#mambu-api-v2-index-rate-sources"
singer-schema: "https://github.com/singer-io/tap-mambu/blob/master/tap_mambu/schemas/index_rate_sources.json"
description: "This table contains information about index rate sources."

replication-method: "Full Table"

api-method:
    name: "getAllIndexRateSources"
    doc-link: "https://api.mambu.com/#mambu-api-v2-index-rate-sources"
    
attributes:
  - name: "encoded_key"
    type: "string"
    replication-key: true
    description: "The unique intex rate encoded key."
    #foreign-key-id: "index-rate-encoded-key"
  - name: "name"
    type: "string"
    description: ""
  - name: "notes"
    type: "string"
    description: ""
  - name: "type"
    type: "string"
    description: ""
---
