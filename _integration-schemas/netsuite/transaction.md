---
tap: "netsuite"
# version: "10-15-2015"

name: "netsuite_transaction"
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/transaction.html
description: |
  The `{{ table.name }}` table contains info about [PLACEHOLDER].

  {% include integrations/saas/netsuite-permission-list.html %}

replication-method: "Incremental"
primary-key: "internalId:_type"
replication-key: "lastModifiedDate"

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
  - name: "PLACEHOLDER"
    level: "View"
    location: "Transactions"
---