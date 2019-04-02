---
tap: "netsuite"
version: "1.0"

name: "Contact"
doc-link: "https://975200-sb2.app.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2018_1/schema/record/contact.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Contact.json"
description: |
  The `{{ table.name }}` table contains info about contacts.

replication-method: "Key-based Incremental"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: "The contact ID."
    # foreign-key-id: "contact-id"

  - name: "lastModifiedDate"
    type: "date-time"
    replication-key: true
    description: "The time the contact was last modified."

  - name: "addressbookList"
    type: "varies"
    description: ""

  - name: "altEmail"
    type: "string"
    description: "The alternate email address for the contact."

  - name: "assistant"
    type: "varies"
    description: "A reference to an existing contact."

  - name: "assistantPhone"
    type: "string"
    description: ""

  - name: "billPay"
    type: "boolean, string"
    description: "Indicates whether payments can be sent online to the contact."

  - name: "categoryList"
    type: "varies"
    description: ""

  - name: "comments"
    type: "string"
    description: "Additional comments about the contact."

  - name: "company"
    type: "varies"
    description: "The company the contact works for."

  - name: "contactSource"
    type: "varies"
    description: "Indicates how the contact came to do business with your company."

  - name: "customFieldList"
    type: "varies"
    description: "The custom fields associated with the contact."

  - name: "customForm"
    type: "varies"
    description: ""

  - name: "dateCreated"
    type: "date-time"
    description: "The date the contact was created."

  - name: "defaultAddress"
    type: "string"
    description: "The default billing address for the contact."

  - name: "email"
    type: "string"
    description: "The contact's email address."

  - name: "entityId"
    type: "string"
    description: "The name for the contact in lists."

  - name: "externalId"
    type: "string"
    description: ""

  - name: "fax"
    type: "string"
    description: "The contact's fax number."

  - name: "firstName"
    type: "string"
    description: "The contact's first name."

  - name: "globalSubscriptionStatus"
    type: "varies"
    description: |
      The contact's subscription status. Possible values are:

      - Confirmed Opt-In
      - Soft Opt-In
      - Soft Opt-Out
      - Confirmed Opt-Out

  - name: "homePhone"
    type: "string"
    description: "The customer's home phone number."

  - name: "image"
    type: "varies"
    description: "A reference to a file in the file cabinet for the contact."

  - name: "isInactive"
    type: "boolean, string"
    description: "Indicates if the contact is inactive."

  - name: "isPrivate"
    type: "boolean, string"
    description: "Indicates if the contact is private. When a contact is private, it can only be viewed by th e user that entered the contact record."

  - name: "lastName"
    type: "string"
    description: "The contact's last name."

  - name: "middleName"
    type: "string"
    description: "The contact's middle name."

  - name: "mobilePhone"
    type: "string"
    description: "The contact's mobile phone number."

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "officePhone"
    type: "string"
    description: "The contact's office phone number."

  - name: "phone"
    type: "string"
    description: "The contact's phone number."

  - name: "phoneticName"
    type: "string"
    description: "The furigana character used to sort the contact record in {{ integration.display_name }}."

  - name: "salutation"
    type: "string"
    description: "The contact's salutation."

  - name: "subscriptionsList"
    type: "varies"
    description: ""

  - name: "subsidiary"
    type: "varies"
    description: ""

  - name: "supervisor"
    type: "varies"
    description: "The contact's supervisor."

  - name: "supervisorPhone"
    type: "string"
    description: "The contact supervisor's phone number."

  - name: "title"
    type: "string"
    description: "The contact's title at their `company`."
---