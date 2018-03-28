---
tap: "zuora"
version: 1.0 

name: "invoiceItem"
doc-link: https://live-www.zuora.com/developer/api-reference/#tag/Invoice-Items
description: |
  The `invoiceItem` table contains info about the line items in invoices.

replication-method: "Incremental"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The ID of the invoice item."

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the invoice item was last updated."

  - name: "accountingCode"
    type: "string"
    description: "The accounting code for the item's charged."

  - name: "appliedToChargeNumber"
    type: "string"
    description: "The charge number that the discount charge is applied to. This is only applicable to invoice items that are discount charges."

  - name: "appliedToInvoiceItemId"
    type: "string"
    description: "Associates a discount invoice item to a specific invoice item."

  - name: "chargeAmount"
    type: "decimal"
    description: "The amount being charged for the invoice item, without taxes."

  - name: "chargeDate"
    type: "date-time"
    description: "The date when the invoice item was created."

  - name: "chargeDescription"
    type: "string"
    description: "A description of the invoice item's charge."

  - name: "chargeId"
    type: "string"
    description: "The original ID of the rate plan charge that is associated with the invoice item upon creation."

  - name: "chargeName"
    type: "string"
    description: "The name of the invoice item's charge."

  - name: "chargeNumber"
    type: "string"
    description: "The unique identifer of the invoice item's charge."

  - name: "chargeType"
    type: "string"
    description: |
      The type of charge. Possible values are:

      - `OneTime`
      - `Recurring`
      - `Usage`

  - name: "createdById"
    type: "string"
    description: "The ID of the Zuora user who created the invoice item."

  - name: "createdDate"
    type: "date-time"
    description: "The date the invoice item was created."

  - name: "deleted"
    type: "boolean"
    description: |
      **Only supported for the AQuA API.** If `true`, this record was deleted in Zuora.

  - name: "invoiceId"
    type: "string"
    description: "The ID of the invoice associated with the invoice item."
    ## foreign-keys:
    ##   - table-name: "invoice"
    ##     attribute: "id"

  - name: "processingType"
    type: "decimal"
    description: |
      The processing type of the invoice item. Possible values are:

      - `0` - charge
      - `1` - discount
      - `2` - prepayment
      - `3` tax

  - name: "productDescription"
    type: "string"
    description: "The description of the product associated with the invoice item."

  - name: "productId"
    type: "string"
    description: "The ID of the product associated with the invoice item."
    ## foreign-keys:
    ##   - table-name: "product"
    ##     attribute: "id"

  - name: "productName"
    type: "string"
    description: "The name of the product associated with the invoice item."

  - name: "productRatePlanChargeId"
    type: "string"
    description: "The ID of the rate plan charge associated with the invoice item."
    ## foreign-keys:
    ##   - table-name: "product_rate_plan_charge"
    ##     attribute: "id"

  - name: "quantity"
    type: "decimal"
    description: "The number of units for the invoice item."

  - name: "ratePlanChargeId"
    type: "string"
    description: "The ID of the rage plan charge that's associated with the invoice item."
    ## foreign-keys:
    ##   - table-name: "rate_plan_charge"
    ##     attribute: "id"

  - name: "revRecCode"
    type: "string"
    description: "Associates the invoice item with a specific revenue recognition code."

  - name: "revRecStartDate"
    type: "date-time"
    description: "The date when revenue recognition is triggered."

  - name: "revRecTriggerCondition"
    type: "string"
    description: "Specifies when revenue recognition begins based on a triggering event."

  - name: "serviceEndDate"
    type: "date-time"
    description: "The end date of the service period associated with the invoice item. Service will end one second before the date in this value."

  - name: "serviceStartDate"
    type: "date-time"
    description: "The start date of the service period associated with the invoice item."

  - name: "sku"
    type: "string"
    description: "The unique SKU for the product associated with the invoice item."

  - name: "subscriptionId"
    type: "string"
    description: "The ID of the subscription associated with the invoice item."
    ## foreign-keys:
    ##   - table-name: "subscription"
    ##     attribute: "id"

  - name: "subscriptionNumber"
    type: "string"
    description: "The number or name of the subscription associated with the invoice item."

  - name: "taxAmaount"
    type: "decimal"
    description: "The amount of tax applied to the invoice item's charge."

  - name: "taxCode"
    type: "string"
    description: "The tax code for taxation rules."

  - name: "taxExemptAmount"
    type: "decimal"
    description: "The amount of the invoice item's charge that is tax exempt."

  - name: "taxMode"
    type: "string"
    description: "The tax mode of the invoice item."

  - name: "unitPrice"
    type: "decimal"
    description: "The per-unit price of the invoice item."

  - name: "uom"
    type: "string"
    description: "The units to measure usage."

  - name: "updatedById"
    type: "string"
    description: "The ID of the Zuora user who last updated the invoice item."
---