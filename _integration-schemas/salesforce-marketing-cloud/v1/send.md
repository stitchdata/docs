---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-table-schema/
## FOR INSTRUCTIONS & REFERENCE INFO


tap: "salesforce-marketing-cloud"
version: "1"

name: "send"
doc-link: https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-apis.meta/mc-apis/send.htm
singer-schema: https://github.com/singer-io/tap-exacttarget/blob/master/tap_exacttarget/endpoints/sends.py
description: |
  The `{{ table.name }}` table contains info about the email sends in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Retrieve sends"
  doc-link: "https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-apis.meta/mc-apis/send.htm"

attributes:
  - name: "ID"
    type: "integer"
    primary-key: true
    description: "The send ID."
    foreign-key-id: "send-id"

  - name: "ModifiedDate"
    type: "date-time"
    replication-key: true
    description: "The date and time the send was last modified."

  - name: "CreatedDate"
    type: "date-time"
    description: "The date and time the send was created."

  - name: "EmailID"
    type: "integer"
    description: "The ID of an email message associated with a send."
    foreign-key-id: "email-id"

  - name: "EmailName"
    type: "string"
    description: "The name of an email message associated with a send."

  - name: "FromAddress"
    type: "string"
    description: "The From address associated with the send. **This field has been deprecated by Salesforce.**"

  - name: "FromName"
    type: "string"
    description: "The From name associated with the send. **This field has been deprecated by Salesforce.**"

  - name: "IsAlwaysOn"
    type: "boolean"
    description: "If `true`, the request can be performed while the system is in maintenance mode."

  - name: "IsMultipart"
    type: "boolean"
    description: "Indicates whether the email is sent with Multipart/MIME enabled."

  # - name: "PartnerProperties"
  #   type: 
  #   description: ""

  - name: "SendDate"
    type: "date-time"
    description: "The date on which a send occurred."

  - name: "SentDate"
    type: "date-time"
    description: "The date on which a send took place."

  - name: "Status"
    type: "string"
    description: "Defines status of object. Status of an address."

  - name: "Subject"
    type: "string"
    description: "Contains subject area information for a message."
---