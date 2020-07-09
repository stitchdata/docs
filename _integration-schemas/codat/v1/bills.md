---
tap: "codat"
version: "1"
key: "bill"

name: "bills"
doc-link: "https://docs.codat.io/docs/bills-1"
singer-schema: "https://github.com/singer-io/tap-codat/blob/master/tap_codat/schemas/bills.json"
description: |
  The `{{ table.name }}` table contains info about the bills in your {{ integration.display_name }} account. A bill is an itemized record of goods or services purchased from a [supplier](#suppliers).

replication-method: "Key-based Incremental"

replication-key: "modifiedDate"

api-method:
    name: "Get bills for a company"
    doc-link: "https://docs.codat.io/reference/bills#bills_listpaged"

attributes:
  - name: "companyId"
    type: "string"
    primary-key: true
    description: "The ID of the company associated with the bill."
    #foreign-key-id: "bill-id"

  - name: "id"
    type: "string"
    primary-key: true
    description: "The bill ID."

  - name: "amountDue"
    type: "number"
    description: "The amount due for the bill."

  - name: "currency"
    type: "string"
    description: "The currency of the bill."

  - name: "dueDate"
    type: "date-time"
    description: "The date the bill is due to be paid by."

  - name: "issueDate"
    type: "date-time"
    description: "The date the bill was recorded in the accounting system."

  - name: "reference"
    type: "string"
    description: "A user-friendly identifier for the bill."

  - name: "status"
    type: "string"
    description: |
      The status of the bill. Possible values are:

      - `Draft` - Bill is yet to be authorised and sent by the Supplier and will not be used in any reports. It may contain incomplete line items.
      - `Open` - The Bill is no longer a draft. It has no payments made against it (`amountDue == totalAmount`).
      - `PartiallyPaid` - The balance paid against the Bill is positive, but less than the total Bill amount (`0 < amountDue < totalAmount`).
      - `Paid` - Bill is paid in full. This includes if the Bill has been credited or overpaid. (`amountDue == 0`)
      - `Void` - A Bill can become Void by being deleted, refunded, written off or cancelled. **Note:** A voided Bill may still be `partiallyPaid` and so all outstanding amounts on voided Bills are removed from the AP (Accounts Payable) account.
      - `Unknown`

  - name: "subTotal"
    type: "number"
    description: "The total amount of the bill, excluding any taxes."

  - name: "supplierRef"
    type: "string"
    description: "The supplier the bill has been received from."
    foreign-key-id: "supplier-id"

  - name: "taxAmount"
    type: "number"
    description: "The amount of tax on the bill."

  - name: "totalAmount"
    type: "number"
    description: "The total amount of the bill, including tax."

  - name: "lineItems"
    type: "array"
    description: ""
    subattributes:
      - name: "description"
        type: "string"
        description: "The name of the goods or services."
      - name: "unitAmount"
        type: "number"
        description: "The price of each unit of goods or services."
      - name: "quantity"
      - type: "number"
        description: "The number of units of goods or services."
      - name: "discountAmount"
        type: "number"
        description: "The value of the discounts applied."
      - name: "subTotal"
        type: "number"
        description: "The price of the goods or services, including the discounts."
      - name: "taxAmount"
        type: "number"
        description: "The amount of tax on the line items."
      - name: "totalAmount"
        type: "number"
        description: "The price of the good or services, including the discounts and tax."
      - name: "accountRef"
        type: "object"
        description: "The account the line items are linked to."
        subattributes:
          - name: "id"
            type: "string"
            description: ""
          - name: "name"
            type: "string"
            description: ""
      - name: "discountPercentage"
        type: "number"
        description: "The percentage rate of the discounts, from `0` to `100`."
      - name: "taxRateRef"
        type: "object"
        description: "The tax rate that the line items are linked to."
        subattributes:
          - name: "id"
            type: "string"
            description: "The tax rate ID."
          - name: "name"
            type: "string"
            description: "The tax rate name."
      - name: "itemRef"
        type: "object"
        description: "The product, service type, or inventory that is linked to the line item."
        subattributes:
          - name: "id"
            type: "string"
            description: "The item ID."
          - name: "name"
            type: "string"
            description: "The item name."     
---