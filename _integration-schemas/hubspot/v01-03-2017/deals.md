---
tap: "hubspot"
version: "01-03-2017"

name: "deals"
doc-link: https://developers.hubspot.com/docs/methods/deals/deals_overview
singer-schema: https://github.com/singer-io/tap-hubspot/blob/v0.11.0/tap_hubspot/schemas/deals.json
description: |
  The `deals` table contains info about the deals in a HubSpot portal.

replication-method: "Full Table"
api-method:
  name: getRecentlyModifiedDeals
  doc-link: https://developers.hubspot.com/docs/methods/deals/get_deals_modified

attributes:
## Primary Key
  - name: "dealId"
    type: "integer"
    primary-key: true
    description: "The ID of the deal."

## Primary Key
  - name: "portalId"
    type: "integer"
    primary-key: true
    description: "The ID of the portal the deal is associated with."

  - name: "isDeleted"
    type: "boolean"
    description: "Indicates if the deal has been deleted in {{ integration.display_name }}."

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

      - name: "associatedDealIds"
        type: "array"
        description: "IDs of the deals associated with the deal."
        array-attributes:
          - name: "value"
            type: "integer"
            description: "The ID of the deal associated with the deal. (How meta!)"
---
