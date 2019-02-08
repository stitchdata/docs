---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-form"
form-type: "source"
key: "source-form-properties-sendgrid-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "SendGrid Source Form Property"
api-type: "platform.sendgrid"
display-name: "SendGrid"

source-type: "saas"
docs-name: "sendgrid-core"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "api_key"
    type: "string"
    required: true
    description: "The SendGrid API key. Refer to [SendGrid's documentation](https://sendgrid.com/docs/Classroom/Basics/API/api_key_permissions.html) for info about permissions and creating keys."
    value: "<API_KEY>"
---
