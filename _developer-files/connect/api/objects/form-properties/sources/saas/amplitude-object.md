---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-amplitude-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Amplitude Source Form Property"
api-type: "amplitude"
display-name: "Amplitude"

source-type: "saas"
docs-name: "amplitude"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "account"
    type: "string"
    required: true
    description: "The account ID for the Amplitude Snowflake warehouse."
    value: "<AMPLITUDE_SNOWFLAKE_ACCOUNT>"

  - name: "username"
    required: true
    type: "string"
    description: "The username of the {{ integration }} database user."
    value: "<username>"

  - name: "warehouse"
    type: "string"
    required: true
    description: "The name of the Amplitude Snowflake warehouse."
    value: "<AMPLITUDE_WAREHOUSE>"
---