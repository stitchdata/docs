---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-marketo-bulk-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Marketo Bulk Source Form Property"
api-type: "platform.marketobulk"
display-name: "Marketo Bulk"

source-type: "saas"
docs-name: "marketo"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "client_id"
    type: "string"
    required: true
    description: "The user's Marketo client ID."
    value: "<MARKETO_CLIENT_ID>"

  - name: "client_secret"
    type: "string"
    required: true
    description: "The user's Marketo client secret."
    value: "<MARKETO_CLIENT_SECRET>"

  - name: "endpoint"
    type: "string"
    required: true
    description: "The user's Marketo REST endpoint URL. For example: `https://457-RFG-234.mktorest.com/rest`"
    value: "https://<some-id-here>.mktorest.com/rest"
---
