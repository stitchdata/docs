---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-postgresql-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "PostgreSQL Source Form Property"
api-type: "postgres"
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
---