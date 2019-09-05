---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-form"
form-type: "source"
key: "source-form-properties-salesforce-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Salesforce Source Form Property"
api-type: "platform.salesforce"
display-name: "Salesforce"

source-type: "saas"
docs-name: "salesforce"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "api_type"
    type: "string"
    required: true
    description: "The Salesforce API Stitch should use to extract data. Possible values are `REST` or `BULK`. [Read about the pros and cons of each API here]({{ site.baseurl }}/integrations/saas/salesforce#bulk-vs-rest-api)."
    value: "BULK"

  - name: "is_sandbox"
    type: "string"
    required: false
    description: "If `true`, the Salesforce account being connected is a sandbox."
    value: "false"

  - name: "quota_percent_per_run"
    type: "string"
    required: false
    description: "The maximum percentage of Salesforce API quota allowed per replication job."
    value: "20"

  - name: "quota_percent_total"
    type: "string"
    required: false
    description: "The maximum percentage of Salesforce API quota allowed per day."
    value: "80"

  - name: "select_fields_by_default"
    type: "string"
    required: true
    description: "If `true`, Stitch will automatically set new fields added in Salesforce to replicate."
    value: "false"
---