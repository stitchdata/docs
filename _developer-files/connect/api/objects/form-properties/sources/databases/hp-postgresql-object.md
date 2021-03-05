---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-hp-postgresql-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "PostgreSQL (HP) Source Form Property"
api-type: "platform.hp-postgres"
display-name: "PostgreSQL (HP)"

source-type: "database"
docs-name: "postgres"
db-type: "postgres"

property-description: |
  PostgreSQL databases

description: |
  **Note**: This version of the PostgreSQL source differs from the version used by the `platform.postgres` form property. Refer to the [{{ form-property.display-name }} integration feature summary]({{ doc-link | append: "#feature-summary" }}) for more info.


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

## See these fields in _data/connect/common/database-sources.yml > all-databases
## This object will also list the fields in the `mysql` list ^

uses-common-fields: true
uses-feature-fields: true
uses-start-date: false
---