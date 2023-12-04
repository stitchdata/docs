---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-table-schema/
## FOR INSTRUCTIONS & REFERENCE INFO


tap: "salesforce-marketing-cloud"
version: "1"

name: "list_subscriber"
doc-link: https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-apis.meta/mc-apis/listsubscriber.htm
singer-schema: https://github.com/singer-io/tap-exacttarget/blob/master/tap_exacttarget/endpoints/list_subscribers.py
description: |
  The `{{ table.name }}` table contains info about the lists associated with a specific subscriber in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Retrieve list subscribers"
  doc-link: "https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-apis.meta/mc-apis/listsubscriber.htm"

attributes:
  - name: "ListID"
    type: "integer"
    primary-key: true
    description: "Defines identification for a list the subscriber resides on."
    foreign-key-id: "list-id"

  - name: "SubscriberKey"
    type: "string"
    primary-key: true
    description: "The ID of the subscriber associated with the list subscriber."
    foreign-key-id: "subscriber-key"

  - name: "ModifiedDate"
    type: "date-time"
    replication-key: true
    description: "The date and time the list subscriber was last modified."

  - name: "CreatedDate"
    type: "date-time"
    description: "The date and time the list subscriber was created."

  - name: "ID"
    type: "integer"
    description: "The list subscriber ID."

  - name: "ObjectID"
    type: "string"
    description: "The list subscriber's object ID."

  # - name: "PartnerProperties"
  #   type: 
  #   description: ""

  - name: "Status"
    type: "string"
    description: |
      Defines the status of a subscriber's address. Possible values are:

      - `Active`
      - `Bounced`
      - `Held`
      - `Unsubscribed`
      - `Deleted`
---