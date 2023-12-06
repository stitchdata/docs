---
tap-reference: "xero"
version: "1"

name: "line_items"
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/line_items.json

attributes:
  - name: "LineItemID"
    type: "string"
    description: "The ID of the line item."

  - name: "Description"
    type: "string"
    description: "The description of the line item."

  - name: "Quantity"
    type: "number"
    description: "The quantity of the line item."

  - name: "UnitAmount"
    type: "number"
    description: "The amount of the line item."

  - name: "AccountCode"
    type: "string"
    description: "The account code associated with the line item."

  - name: "ItemCode"
    type: "string"
    description: "The code associated with the line item."

  - name: "TaxType"
    type: "string"
    description: "The tax type associated with the line item."

  - name: "LineAmount"
    type: "number"
    description: "The total of the line item, calculated as `UnitAmount x Quantity`."

  - name: "TaxAmount"
    type: "number"
    description: "The total tax of the line item."

  - name: "DiscountRate"
    type: "number"
    description: "The discount rate of the line item, if applicable."

  - name: "Tracking"
    type: ""
    description: |
      Details about the tracking categories applied to the line item, if applicable.

      {{ integration.subsubtable-note | flatify | replace:"table_name","tracking_categories" }}
---