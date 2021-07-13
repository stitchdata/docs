---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-hp-heroku-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Heroku (HP) Source Form Property"
api-type: "platform.hp-heroku-pg"
display-name: "Heroku (HP)"

source-type: "database"
docs-name: "heroku"
db-type: "postgres"

property-description: |
  {{ form-property.display-name }} PostgreSQL databases

description: |
  **Note**: This version of the {{ form-property.display-name }} source differs from the version used by the `platform.heroku_pg` form property. Refer to the [{{ form-property.display-name }} integration feature summary]({{ doc-link | append: "#feature-summary" }}) for more info.


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

## See these fields in _data/connect/common/database-sources.yml > all-databases

uses-common-fields: true
uses-feature-fields: true
uses-start-date: false
---