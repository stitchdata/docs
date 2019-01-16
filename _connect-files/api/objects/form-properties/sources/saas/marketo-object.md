---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-form"
form-type: "source"
key: "source-form-properties-marketo-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Marketo Source Form Property"
api-type: "marketo"
display-name: "Marketo"

source-type: "saas"
docs-name: "marketo"

description: ""

deprecated:
  as-of: "June 26, 2018"
  use-instead: "[Marketo Bulk]({{ api.form-properties.source-forms.marketo-bulk.section }})"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

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

  - name: "identity"
    type: "string"
    required: true
    description: "The user's Marketo REST identity URL. For example: `https://457-RFG-234.mktorest.com/identity`"
    value: "https://<some-id-here>.mktorest.com/identity"

  - name: "max_daily_calls"
    type: "string"
    required: false
    description: "The maximum number of daily API calls that Stitch may make to the Marketo API."
---
