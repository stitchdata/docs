---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-form"
form-type: "source"
key: "source-form-properties-oracle-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Oracle Source Form Property"
api-type: "oracle"
display-name: "Oracle"

source-type: "database"
docs-name: "oracle"
db-type: "oracle"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-common-fields: true
## See these fields in _data/connect/common/database-sources.yml > all-databases

object-attributes:
  - name: "default_replication_method"
    type: "string"
    required: false
    description: "**This field is not currently in use, but will be part of a future release.**"
    value: ""

  - name: "filter_schemas"
    type: "string"
    required: false
    description: "**This is an internal field and is for Stitch use only.**"
    value: ""

  - name: "sid"
    type: "string"
    required: false
    description: "The site identifier associated with the Oracle instance."
    value: "<ORACLE_SID>"
---