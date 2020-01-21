---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-harvest-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Harvest Source Form Property"
api-type: "platform.harvest"
display-name: "Harvest"

source-type: "saas"
docs-name: "harvest"

description: ""

# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "account_name"
    type: "string"
    required: true
    description: "Your {{ form-property.display-name }} account name. For example: if your {{ form-property.display-name }} account URL is `stitch.harvestapp.com`, this value would be `stitch`."
    value: "<ACCOUNT_NAME>"
---