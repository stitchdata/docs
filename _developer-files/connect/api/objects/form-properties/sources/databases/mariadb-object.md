---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-mariadb-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "MariaDB Source Form Property"
api-type: "platform.mariadb"
display-name: "MariaDB"

source-type: "database"
docs-name: "mariadb"
db-type: "mysql"

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
  - name: "allow_non_auto_increment_pks"
    type: "string"
    required: false
    description: |
      If `true`, an auto-incrementing Primary Key will not be required for tables using Full Table Replication. Auto-incrementing Primary Keys are used during full table replication to allow the replication of a table to span multiple replication jobs.

      Unless set, this property will default to `true`.
    value: "true"
---