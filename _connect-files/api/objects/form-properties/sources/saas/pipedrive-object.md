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

uses-start-date: true

object-attributes:
  - name: "api_token"
    type: "string"
    required: true
    description: |
      A {{ form-property.display-name }} API token, used to authenticate to {{ form-property.display-name }}'s API.

      **Note**: In {{ form-property.display-name }}, API tokens are unique to each {{ form-property.display-name }} user. The API token provided should be associated with a {{ form-property.display-name }} user with Admin permissions, which will ensure Stitch can successfully access and replicate all data from {{ form-property.display-name }}.
    value: "<API_TOKEN>"
---