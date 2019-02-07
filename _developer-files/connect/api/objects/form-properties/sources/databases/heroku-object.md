---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-heroku-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Heroku Source Form Property"
api-type: "heroku_pg"
display-name: "Heroku"

source-type: "database"
docs-name: "heroku"
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