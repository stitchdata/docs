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

title: "Google CloudSQL PostgreSQL (HP) Source Form Property"
api-type: "platform.hp-cloudsql-pg"
display-name: "Google CloudSQL PostgreSQL (HP)"

source-type: "database"
docs-name: "cloudsql-postgres"
db-type: "postgres"

property-description: |
  {{ form-property.display-name | remove: "(HP)" }} databases

description: |
  **Note**: This version of the {{ form-property.display-name | remove: "(HP)" }} source differs from the version used by the `platform.cloudsql_pg` form property. Refer to the [{{ form-property.display-name }} integration feature summary]({{ doc-link | append: "#feature-summary" }}) for more info.


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

## See these fields in _data/connect/common/database-sources.yml > all-databases
## This object will also list the fields in the `mysql` list ^

uses-common-fields: true
uses-feature-fields: true
uses-start-date: false
---