---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-table-schema/
## FOR INSTRUCTIONS & REFERENCE INFO


tap: "salesforce-marketing-cloud"
version: "1.0"

name: "list_send"
doc-link: https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-apis.meta/mc-apis/listsend.htm
singer-schema: https://github.com/singer-io/tap-exacttarget/blob/master/tap_exacttarget/endpoints/list_sends.py
description: |
  The `{{ table.name }}` table contains info about the completed sends for lists in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Retrieve list sends"
  doc-link: "https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-apis.meta/mc-apis/listsend.htm"

attributes:
  - name: "ListID"
    type: "integer"
    primary-key: true
    description: "List associated with the send."
    foreign-key-id: "list-id"

  - name: "SendID"
    type: "integer"
    primary-key: true
    description: "The ID of the send associated with the list send."
    foreign-key-id: "send-id"

  - name: "ModifiedDate"
    type: "date-time"
    replication-key: true
    description: "The date and time the send was last modified."

  - name: "CreatedDate"
    type: "date-time"
    description: "The date and time the send was created."

  - name: "CustomerKey"
    type: "string"
    description: "User-supplied unique identifier for an object within an object type (corresponds to the external key assigned to an object in the user interface."

  - name: "ExistingUndeliverables"
    type: "integer"
    description: "Indicates whether bounces occurred on previous send."

  - name: "ExistingUnsubscribes"
    type: "integer"
    description: "Indicates whether unsubscriptions occurred on previous send."

  - name: "ForwardedEmails"
    type: "integer"
    description: "Number of emails forwarded for a send."

  - name: "HardBounces"
    type: "integer"
    description: "The number of hard bounces associated with a send."

  - name: "InvalidAddresses"
    type: "integer"
    description: "Specifies the number of invalid addresses associated with a send."

  - name: "ID"
    type: "integer"
    description: "The send ID."

  - name: "MissingAddresses"
    type: "integer"
    description: "The number of missing addresses encountered within a send."

  - name: "NumberDelivered"
    type: "integer"
    description: "The number of sent emails that did not bounce."

  - name: "NumberSent"
    type: "integer"
    description: "The number of emails actually sent as part of an email send. This number reflects all of the sent messages and may include bounced messages."

  - name: "ObjectID"
    type: "string"
    description: "The send's object ID."

  - name: "OtherBounces"
    type: "integer"
    description: "Specifies number of `Other`-type bounces in a send."

  # - name: "PartnerProperties"
  #   type: 
  #   description: ""

  - name: "SoftBounces"
    type: "integer"
    description: "The number of soft bounces associated with a specific send."

  - name: "UniqueClicks"
    type: "integer"
    description: "The number of unique clicks on message."

  - name: "UniqueOpens"
    type: "integer"
    description: "The number of unique opens resulting from a triggered send."

  - name: "Unsubscribes"
    type: "integer"
    description: "The number of unsubscribe events associated with a send."
---