---
tap: "xero"
version: "1"
key: "quote"

name: "quotes"
doc-link: &api-doc https://developer.xero.com/documentation/api/quotes
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/quotes.json
description: |
  The `{{ table.name }}` table contains info about the quotes in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get quotes"
  doc-link: *api-doc

attributes:
  - name: "QuoteID"
    type: "string"
    primary-key: true
    description: "The quote ID."
    foreign-key-id: "quote-id"

  - name: "UpdatedDateUTC"
    type: "date-time"
    replication-key: true
    description: "The time the quote was last updated."

  - name: "Contact"
    type: "array"
    description: ""

  - name: "Date"
    type: "date-time"
    description: ""

  - name: "ExpiryDate"
    type: "date-time"
    description: ""

  - name: "Status"
    type: "string"
    description: ""

  - name: "LineAmountTypes"
    type: "string"
    description: ""

  - name: "LineItems"
    type: "array"
    description: ""
    subattributes:
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
        type: "array"
        description: |
          Details about the tracking categories applied to the line item, if applicable.

  - name: "SubTotal"
    type: "number"
    description: ""

  - name: "TotalTax"
    type: "number"
    description: ""

  - name: "Total"
    type: "number"
    description: ""

  - name: "TotalDiscount"
    type: "number"
    description: ""

  - name: "CurrencyCode"
    type: "string"
    description: ""

  - name: "CurrencyRate"
    type: "number"
    description: ""

  - name: "QuoteNumber"
    type: "string"
    description: ""

  - name: "Reference"
    type: "string"
    description: ""

  - name: "BrandingThemeID"
    type: "string"
    description: ""
    foreign-key-id: "branding-theme-id"

  - name: "Title"
    type: "string"
    description: ""

  - name: "Summary"
    type: "string"
    description: ""

  - name: "Terms"
    type: "string"
    description: ""

  - name: "TrackingCategory"
    type: "array"
    description: ""
---