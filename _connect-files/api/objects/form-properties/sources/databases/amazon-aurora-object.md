---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-form"
form-type: "source"
key: "source-form-properties-aurora-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Amazon Aurora Source Form Property"
api-type: "platform.aurora"
display-name: "Amazon Aurora"

source-type: "database"
docs-name: "aurora-rds"
db-type: "mysql"

description: ""

# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

## See these fields in _data/connect/common/database-sources.yml > all-databases
## This object will also list the fields in the `mysql` list ^

uses-common-fields: true
uses-feature-fields: true
---