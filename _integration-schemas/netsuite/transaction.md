---
tap: "netsuite"
# version: "10-15-2015"

name: "netsuite_transaction"
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/transaction.html
description: |
  The `{{ table.name }}` table contains info about transactions.

replication-method: "Key-based Incremental"
abstract: true

supported-types:
  - name: "AssemblyBuild"
  - name: "AssemblyUnBuild"
  - name: "BinTransfer"
  - name: "BinWorksheet"
  - name: "CashRefund"
  - name: "CashSale"
  - name: "Check"
  - name: "CreditMemo"
  - name: "Custom"
  - name: "CustomerDeposit"
  - name: "CustomerPayment"
  - name: "CustomerRefund"
  - name: "Deposit"
  - name: "DepositApplication"
  - name: "Estimate"
  - name: "ExpenseReport"
  - name: "InventoryAdjustment"
  - name: "InventoryCostRevaluation"
  - name: "InventoryTransfer"
  - name: "Invoice"
  - name: "ItemFulfillment"
  - name: "ItemReceipt"
  - name: "Journal"
  - name: "Opportunity"
  - name: "PaycheckJournal"
  - name: "PurchaseOrder"
  - name: "Requisition"
  - name: "ReturnAuthorization"
  - name: "SalesOrder"
  - name: "TransferOrder"
  - name: "VendorBill"
  - name: "VendorCredit"
  - name: "VendorPayment"
  - name: "VendorReturnAuthorization"
  - name: "WorkOrder"
  - name: "WorkOrderClose"
  - name: "WorkOrderCompletion"
  - name: "WorkOrderIssue"

permissions:
  - name: ""
    level: "View"
    location: "Transactions"

attributes:
  - name: "internalId"
    type: "integer"
    primary-key: true
    description: |
      The {{ table.name | remove: "netsuite_" | replace: "_"," " }} ID.

  - name: "_type"
    type: "string"
    description: |
      The transaction type. Possible values are:

      {% for transaction-type in table.supported-types %}
      - `{{ transaction-type.name }}`
      {% endfor %}

  - name: "lastModifiedDate"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.name | remove: "netsuite_" | replace: "_"," " }} was last updated.

  - name: "Your Selected Fields"
    description: |
      Other fields selected by you. For a list of available attributes, refer to [{{ integration.display_name }}'s documentation]({{ table.doc-link }}){:target="new"}. **Note**: You will need to log into your {{ integration.display_name }} account to view the documentation.
---