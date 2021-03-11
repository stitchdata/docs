---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-postgresql-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "PostgreSQL Source Form Property"
api-type: "platform.postgres"
display-name: "PostgreSQL"

source-type: "database"
docs-name: "postgres"
db-type: "postgres"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

## See these fields in _data/connect/common/database-sources.yml > all-databases
## This object will also list the fields in the `mysql` list ^

uses-common-fields: true
uses-feature-fields: true
uses-start-date: false

object-attributes:
  - name: "wal2json_message_format"
    required: false
    internal: true
    type: "string"
    description: |
      The message format version the [wal2json plugin](https://github.com/eulerto/wal2json){:target="new"} on Stitch's server should use when performing Log-based Incremental Replication.

      Accepted values are:

      - `1` - Use the v1 message format. This is the default.
      - `2` - Use the v2 message format
    value: "2"
---