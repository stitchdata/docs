---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-cloudsql-postgresql-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Google CloudSQL PostgreSQL Source Form Property"
api-type: "platform.cloudsql_pg"
display-name: "Google CloudSQL PostgreSQL"

source-type: "database"
docs-name: "cloudsql-postgres"
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
---