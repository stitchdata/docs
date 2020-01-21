---
tap: "shippo"
version: "1"

name: "addresses"
doc-link: https://goshippo.com/docs/reference#addresses
singer-schema: https://github.com/singer-io/tap-shippo/blob/master/tap_shippo/schemas/addresses.json
description: |
  The `{{ table.name }}` table contains info about address objects. These are used to create shipments, obtain rates, and print labels.

replication-method: "Key-based Incremental"
api-method:
  name: listAllAddresses
  doc-link: https://goshippo.com/docs/reference?version=2016-10-25

attributes:
  - name: "object_id"
    type: "string"
    primary-key: true
    description: "The address object ID."
    foreign-key-id: "address-id"

  - name: "object_updated"
    type: "date-time"
    replication-key: true
    description: "The last time the address was updated."

  - name: "object_state"
    type: "string"
    description: "The state of the address. Possible values include `VALID`, `INVALID`, and `INCOMPLETE`."

  - name: "object_purpose"
    type: "string"
    description: "Indicates if the address can be used to purchase labels or only obtain rates. Possible values are `QUOTE` and `PURCHASE`."

  - name: "object_source"
    type: "string"
    description: "The source of the address. Possible values are `FULLY_ENTERED`, `PARTIALLY_ENTERED`, and `VALIDATOR`."

  - name: "object_created"
    type: "date-time"
    description: "The time the address was created."

  - name: "object_owner"
    type: "string"
    description: "The username of the user who created the address."

  - name: "name"
    type: "string"
    description: "The first and last name of the addressee."

  - name: "company"
    type: "string"
    description: "The company name associated with the address."

  - name: "street1"
    type: "string"
    description: "The first street line of the address."

  - name: "street2"
    type: "string"
    description: "The second street line of the address."

  - name: "city"
    type: "string"
    description: "The name of the city contained in the address."

  - name: "state"
    type: "string"
    description: "The state of the address. State values are only required for United States and Canada. Ex: `PA`"

  - name: "zip"
    type: "string"
    description: "The postal code of the address."

  - name: "country"
    type: "string"
    description: "The address's country code. Ex: `US`"

  - name: "phone"
    type: "string"
    description: "The phone number associated with the address."

  - name: "email"
    type: "string"
    description: "The email address of the contact person."

  - name: "is_residential"
    type: "boolean"
    description: "Indicates if the address is a residential address."

  - name: "metadata"
    type: "string"
    description: "Additional information about the address."

  - name: "test"
    type: "boolean"
    description: "Indicates if the address was created in test mode."

  - name: "messages"
    type: "array"
    description: "Details about messages associated with the address."
    subattributes:
      - name: "code"
        type: "string"
        description: "The ID of the message. This may not always be available."

      - name: "source"
        type: "string"
        description: "The source of the message. Ex: `USPS`"

      - name: "text"
        type: "string"
        description: "The text of the message."
---