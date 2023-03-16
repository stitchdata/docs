---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "mambu"
version: "1"
key: "index-rate-source"

name: "index_rate_sources"
doc-link: "https://api.mambu.com/#mambu-api-v2-index-rate-sources"
singer-schema: "https://github.com/singer-io/tap-mambu/tree/v1.3.3/tap_mambu/schemas/index_rate_sources.json"
description: |
  This table contains information about index rate sources.


# -------------------------- #
#    Replication Details     #
# -------------------------- #
api-method:
  name: "Get all index rate sources (v2.0)"
  doc-link: "https://api.mambu.com/#mambu-api-v2-index-rate-sources"

replication-method: "Full Table"


# -------------------------- #
#       Table Attributes     #
# -------------------------- #

attributes:
  - name: "encoded_key"
    type: "string"
    primary-key: true
    description: "The unique index rate encoded key."
    #foreign-key-id: "index-rate-key"

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