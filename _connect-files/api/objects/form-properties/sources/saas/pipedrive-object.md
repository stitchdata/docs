---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-form"
form-type: "source"
key: "source-form-properties-pipedrive-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Pipedrive Source Form Property"
api-type: "platform.pipedrive"
display-name: "Pipedrive"

source-type: "saas"
docs-name: "pipedrive"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "api_token"
    type: "string"
    required: true
    description: |
      A Pipedrive API token, used to authenticate to Pipedrive's API.
    value: "<API_TOKEN>"
---