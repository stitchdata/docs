---
tap: "hubspot"
version: "2.0"

name: "deals"
doc-link: https://developers.hubspot.com/docs/methods/deals/deals_overview
singer-schema: https://github.com/singer-io/tap-hubspot/blob/master/tap_hubspot/schemas/deals.json
description: |
  The `{{ table.name }}` table contains info about the deals in a HubSpot portal.

replication-method: "Full Table"
api-method:
  name: getAllDeals
  doc-link: https://developers.hubspot.com/docs/methods/deals/get-all-deals

attributes:
  - name: "dealId"
    type: "integer"
    primary-key: true
    description: "The ID of the deal."
    foreign-key-id: "deal-id"

  - name: "portalId"
    type: "integer"
    primary-key: true
    description: "The ID of the portal the deal is associated with."
    foreign-key-id: "portal-id"

  - name: "associations"
    type: "object"
    description: "IDs of the Vids, Companies, and Deals associated with the deal."
    object-attributes:
      - name: "associatedVids"
        type: "array"
        description: "IDs of the Vids associated with the deal."
        array-attributes:
          - name: "value"
            type: "integer"
            description: "The ID of the Vid associated with the deal."

      - name: "associatedCompanyIds"
        type: "array"
        description: "IDs of the companies associated with the deal."
        array-attributes:
          - name: "value"
            type: "integer"
            description: "The ID of the company associated with the deal."
            foreign-key-id: "company-id"

      - name: "associatedDealIds"
        type: "array"
        description: "IDs of the deals associated with the deal."
        array-attributes:
          - name: "value"
            type: "integer"
            description: "The ID of the deal associated with the deal. (How meta!)"
            foreign-key-id: "deal-id"

  - name: "properties"
    type: "object"
    description: "Details about the properties set for the deal."
    object-attributes:
      - name: "amount"
        type: "object"
        description: "Details about amounts set for the deal."
        object-attributes:
          - name: "value"
            type: "integer"
            description: "The amount of the deal."

          - name: "timestamp"
            type: "date-time"
            description: "The time the amount was set."

          - name: "source"
            type: "string"
            description: "The method used to set the amount."

      - name: "dealname"
        type: "object"
        description: "Details about the name of the property."
        object-attributes:
          - name: "value"
            type: "string"
            description: "The current value of the property."

          - name: "timestamp"
            type: "date-time"
            description: "The time the current value was set."

          - name: "source"
            type: "string"
            description: "The method used to set the value."

          - name: "sourceId"
            type: "string"
            description: "Additional details about the source."
---