---
tap: "shippo"

name: "shipments"
doc-link: https://goshippo.com/docs/reference#shipments
singer-schema: https://github.com/singer-io/tap-shippo/blob/master/tap_shippo/schemas/shipments.json
description: |
  The `shipments` table contains info about shipment objects. Shipment objects are made up of to and from addresses and the parcel to be shipped.

replication-method: "Key-based Incremental"
api-method:
  name: listAllShipments
  doc-link: https://goshippo.com/docs/reference?version=2016-10-25#shipments-list

attributes:
  - name: "object_id"
    type: "string"
    primary-key: true
    description: "The shipment ID."

  - name: "object_updated"
    type: "date-time"
    replication-key: true
    description: "The last time the shipment was updated."

  - name: "object_state"
    type: "string"
    description: "The state of the shipment. Possible values are `VALID`, `INCOMPLETE`, and `INVALID`."

  - name: "object_purpose"
    type: "string"
    description: "Indicates whether a shipment can be used to purchase labels or only obtain quote rates. Possible values are `QUOTE` and `PURCHASE`."

  - name: "object_created"
    type: "date-time"
    description: "The time the shipment was created."

  - name: "object_owner"
    type: "string"
    description: "The username of the user who created the shipment."

  - name: "object_from"
    type: "string"
    description: "The ID of the address that should be used as the sender address."

  - name: "object_to"
    type: "string"
    description: "The ID of the address that should be used as the recipient address."

  - name: "object_return"
    type: "string"
    description: "The ID of the address where the shipment will be sent back if it isn't delivered. If this field is not set, shipments will be returned to the address in the `object_from` field."

  - name: "object_parcel"
    type: "string"
    description: "The ID of the parcel to be shipped."

  - name: "submission-date"
    type: "date-time"
    description: "The date the shipment will be tendered to the carrier."

  - name: "insurance_amount"
    type: "string"
    description: "The total parcel value to be insured."

  - name: "insurance_currency"
    type: "string"
    description: "The currency used for `insurance_amount`."

  - name: "extra"
    type: "object"
    description: ""

  - name: "customs_declaration"
    type: "string"
    description: "The ID of the customs declarations object for an international shipment."

  - name: "reference1"
    type: "string"
    description: "Optional text to be printed on the shipping label."

  - name: "reference2"
    type: "string"
    description: "Optional text to be printed on the shipping label."

  - name: "rates_url"
    type: "string"
    description: "The URL of the rates list for the given shipment."

  - name: "rates_list"
    type: "array"
    description: "Values of available rates."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The available rate value."

  - name: "carrier_accounts"
    type: "array"
    description: "IDs of the carrier accounts to be used for getting shipping rates for the shipment."
    array-attributes:
      - name: "value"
        type: "string"
        primary-key: true
        description: "The carrier ID."

  - name: "metadata"
    type: "string"
    description: "Additional information about the shipment."

  - name: "test"
    type: "boolean"
    description: "Indicates if the shipment was created in test mode."

  - name: "messages"
    type: "array"
    description: "Details about messages associated with the shipment."
    array-attributes:
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