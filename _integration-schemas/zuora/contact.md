---
tap: "zuora"
version: 1.0

name: "contact"
doc-link: https://live-www.zuora.com/developer/api-reference/#tag/Contacts
description: |
  The `contact` table contains info about an account's point-of-contact.

replication-method: "Incremental"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The contact ID."

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the contact was last updated."

  - name: "accountId"
    type: "string"
    description: "The ID of the account associated with the contact."
    ## foreign-keys:
    ##   - table-name: "account"
    ##     attribute: "id"

    ##   - table-name: "invoice"
    ##     attribute: "accountId"

    ##   - table-name: "payment"
    ##     attribute: "accountId"

    ##   - table-name: "refund"
    ##     attribute: "accountId"

    ##   - table-name: "subscription"
    ##     attribute: "accountId"

  - name: "address1"
    type: "string"
    description: "The first line of the contact's address."

  - name: "address2"
    type: "string"
    description: "The second line of the contact's address."

  - name: "city"
    type: "string"
    description: "The city of the contact's address."

  - name: "country"
    type: "string"
    description: "The country of the contact's address."

  - name: "createdById"
    type: "string"
    description: "The ID of the Zuora user who created the contact."

  - name: "createdDate"
    type: "date-time"
    description: "The date the contact was created."

  - name: "deleted"
    type: "boolean"
    description: |
      **Only supported for the AQuA API.** If `true`, this record was deleted in Zuora.

  - name: "description"
    type: "string"
    description: "The description of the contact."

  - name: "fax"
    type: "string"
    description: "The contact's fax number."

  - name: "firstName"
    type: "string"
    description: "The first name of the contact."

  - name: "homePhone"
    type: "string"
    description: "The contact's home phone number."

  - name: "lastName"
    type: "string"
    description: "The last name of the contact."

  - name: "mobilePhone"
    type: "string"
    description: "The contact's mobile phone number."

  - name: "nickName"
    type: "string"
    description: "The nickname for the contact."

  - name: "otherPhone"
    type: "string"
    description: "The additional phone number for the contact."

  - name: "otherPhoneType"
    type: "string"
    description: |
      The type of the `otherPhone`. Possible values are:

      - `Work`
      - `Mobile`
      - `Home`
      - `Other`

  - name: "personalEmail"
    type: "string"
    description: "The email address of the contact."

  - name: "postalCode"
    type: "string"
    description: "The zip code for the contact's address."

  - name: "state"
    type: "string"
    description: "The state or province of the contact's address."

  - name: "taxRegion"
    type: "string"
    description: "If using Zuora's tax rules."

  - name: "updatedById"
    type: "string"
    description: "The ID of the Zuora user who last updated the contact."

  - name: "workEmail"
    type: "string"
    description: "The work email address of the contact."

  - name: "workPhone"
    type: "string"
    description: "The contact's work phone number."

---