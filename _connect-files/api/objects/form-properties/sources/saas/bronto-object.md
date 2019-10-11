---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-form"
form-type: "source"
key: "source-form-properties-bronto-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Bronto Source Form Property"
api-type: "platform.bronto"
display-name: "Bronto"

source-type: "saas"
docs-name: "bronto"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "token"
    type: "string"
    required: true
    description: "The API token for the Bronto account Stitch should replicate data from."
    value: "<API_TOKEN>"
---