---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-table-schema/
## FOR INSTRUCTIONS & REFERENCE INFO


tap: "salesforce-marketing-cloud"
version: "1.0"

name: "subscriber"
doc-link: https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-apis.meta/mc-apis/subscriber.htm
singer-schema: https://github.com/singer-io/tap-exacttarget/blob/master/tap_exacttarget/endpoints/subscribers.py
description: |
  The `{{ table.name }}` table contains info about the subscribers (people subscribed to receive email and/or SMS communication) in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Retrieve subscribers"
  doc-link: "https://developer.salesforce.com/docs/atlas.en-us.noversion.mc-apis.meta/mc-apis/subscriber.htm"

attributes:
  - name: "ID"
    type: "integer"
    primary-key: true
    description: "The subscriber ID."
    foreign-key-id: "subscriber-id"

  - name: "ModifiedDate"
    type: "date-time"
    replication-key: true
    description: "The date and time the subscriber was last modified."

  - name: "Addresses"
    type: "array"
    description: "Indicates addresses belonging to a subscriber, used to create, retrieve, update or delete an email or SMS Address for a given subscriber."
    subattributes:
      - name: "Address"
        type: "string"
        description: ""

      - name: "AddressType"
        type: "string"
        description: ""

      - name: "AddressStatus"
        type: "string"
        description: ""

  # - name: "Attributes"
  #   type: 
  #   description: ""

  - name: "CreatedDate"
    type: "date-time"
    description: "The date and time the subscriber was created."

  - name: "CustomerKey"
    type: "string"
    description: "User-supplied unique identifier for an object within an object type (corresponds to the external key assigned to an object in the user interface."

  - name: "EmailAddress"
    type: "string"
    description: "Contains the email address for a subscriber. Indicates the data extension field contains email address data."

  - name: "EmailTypePreference"
    type: "string"
    description: "The format in which email should be sent."

  - name: "ListIDs"
    type: "array"
    description: "The IDs of the lists the subscriber is a part of."
    subattributes:
      - name: "value"
        type: "string"
        description: "The list ID."
        foreign-key-id: "list-id"

  - name: "Locale"
    type: "string"
    description: "Contains the locale information for an Account. If no location is set, Locale defaults to en-US (English in United States)."

  - name: "ObjectID"
    type: "string"
    description: "The subscriber's object ID."

  - name: "PartnerKey"
    type: "string"
    description: "Unique identifier provided by partner for an object, accessible only via API."

  # - name: "PartnerProperties"
  #   type: 
  #   description: ""

  - name: "PartnerType"
    type: "string"
    description: "The partner associated with a subscriber."

  - name: "PrimaryEmailAddress"
    type: "string"
    description: "The primary email address for a subscriber."

  - name: "PrimarySMSAddress"
    type: "string"
    description: "The primary SMS address for a subscriber. Used to create and update SMS Address for a given subscriber."

  - name: "PrimarySMSPublicationStatus"
    type: "string"
    description: "Indicates the subscriber's modality status."

  - name: "Status"
    type: "string"
    description: "Defines status of object. Status of an address."

  - name: "SubscriberKey"
    type: "string"
    description: "The ID of the subscriber."

  - name: "SubscriberTypeDefinition"
    type: "string"
    description: "Specifies if a subscriber resides in an integration, such as Salesforce or Microsoft Dynamics CRM."

  - name: "UnsubscribedDate"
    type: "date-time"
    description: "Represents the date subscriber unsubscribed from a list."
---