---
tap: "netsuite"
version: "1.0"

name: "Transaction"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Transaction.json"
description: |
  The `{{ table.name }}` table contains info about transactions.

  #### Supported transaction types {#supported-transaction-types}

  Stitch's {{ integration.display_name }} integration supports replicating data for the the transaction types in the [Supported {{ integration.display_name }} transaction types](#supported-transaction-types) section.

  {{ integration.permission-for-table | flatify }}

permission:
  tab: "Transactions"
  name: "[Transaction Type]"
  description: ", where **[Transaction Type]** is a [supported transaction type](#supported-transaction-types),"

replication-method: "Key-based Incremental"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: "The transaction ID."
    foreign-key-id: "transaction-id"
    transaction-types:
      - name: "all"

  - name: "_type"
    type: "string"
    primary-key: true
    description: |
      The type of the transaction. This will be one of the [transaction types](#supported-transaction-types) supported by Stitch for replication.

      For example: If the transaction is an invoice, the value of this field will be `_Invoice`.
    transaction-types:
      - name: "all"

  - name: "lastModifiedDate"
    type: "date-time"
    replication-key: true
    description: "The time the transaction was last modified."
    transaction-types:
      - name: "all"

  - name: "_class"
    type: "varies"
    description: ""
    transaction-types:
      - name: "all"

  - name: "accessibilityTypeFedEx"
    type: "varies"
    description: |
      - `ItemFulfillment` - 
    transaction-types:
      - name: "ItemFulfillment"

  - name: "account"
    type: "varies"
    description: |
      - `CashRefund` - The cash or bank account to refund from.
      - `CashSale` - The account to be credited when payment is received via credit card.
      - `CreditMemo`, `CustomerRefund` - The Accounts Receivable account affected by the transaction.
      - `CustomerDeposit`, `Deposit` - The bank account that will receive the funds from the transaction.
      - `CustomerPayment` - The account for deposited payments.
      - `Invoice` - The AR account affected by the transaction.
      - `InventoryAdjustment` - The account to be used for inventory adjustments.
      - `InventoryCostRevaluation` - The adjustment account associated with the transaction.
    # foreign-key-id: "account-id"
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "Check"
      - name: "CreditMemo"
      - name: "CustomerRefund"
      - name: "CustomerDeposit"
      - name: "CustomerPayment"
      - name: "Deposit"
      - name: "ExpenseReport"
      - name: "InventoryAdjustment"
      - name: "InventoryCostRevaluation"
      - name: "Invoice"

  - name: "accountingApproval"
    type: "boolean, string"
    description: |
      - `ExpenseReport` - Indicates if the expense report is ready to be paid.
    transaction-types:
      - name: "ExpenseReport"

  - name: "accountingBook"
    type: "varies"
    description: |
      - `JournalEntry` - The accounting book associated with the journal entry.
    transaction-types:
      - name: "JournalEntry"
      - name: "InterCompanyJournalEntry"

  - name: "accountingBookDetailList"
    type: "varies"
    description: ""
    transaction-types:
      - name: "AssemblyBuild"
      - name: "AssemblyUnbuild"
      - name: "Check"
      - name: "CreditMemo"
      - name: "CustomerDeposit" 
      - name: "CustomerPayment" 
      - name: "CustomerRefund" 
      - name: "Deposit"
      - name: "DepositApplication" 
      - name: "Estimate"
      - name: "ExpenseReport"
      - name: "InterCompanyJournalEntry"
      - name: "InventoryAdjustment"
      - name: "InventoryCostRevaluation"
      - name: "ItemFulfillment"
      - name: "Invoice"
      - name: "JournalEntry"

  - name: "actualShipDate"
    type: "date-time"
    description: ""
    transaction-types:

  - name: "address"
    type: "string"
    description: |
      - `CustomerRefund` - The billing address for the customer.
    transaction-types:
      - name: "Check"
      - name: "CustomerRefund"

  - name: "adjLocation"
    type: "varies"
    description: |
      - `InventoryAdjustment` - The location to associate with the adjustment transaction.
    transaction-types:
      - name: "InventoryAdjustment"

  - name: "advance"
    type: "number, string"
    description: |
      - `ExpenseReport` - The amount advanced to the employee for the associated expenses.
    transaction-types:
      - name: "ExpenseReport"

  - name: "altHandlingCost"
    type: "number, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo` - The amount the customer was charged for handling.
      - `Estimate` - The amount the customer will be charged for handling.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "altSalesTotal"
    type: "number, string"
    description: |
      - `Estimate` - The Alternate Sales Amount for line items on the estimate. This is applicable to {{ integration.display_name }}'s Alternate Sales Amount feature.
    transaction-types:
      - name: "Estimate"

  - name: "altShippingCost"
    type: "number, string"
    description: |
      - `CashRefund`, `CashSale` - The amount the customer was charged for shipping.
      - `Estimate` - The amount the customer will be charged for shipping.
    transaction-types:
      - name: "CashRefund"
      - name: "Estimate"
      - name: "Invoice"

  - name: "amount"
    type: "number, string"
    description: |
      - `ExpenseReport` - The total of all expense line items minus the `advance` amount.
    transaction-types:
      - name: "ExpenseReport"

  - name: "amountPaid"
    type: "number, string"
    description: |
      - `CreditMemo` - The amount paid in the credit memo.
      - `Invoice` - The total amount paid for the invoice.
    transaction-types:
      - name: "CreditMemo"
      - name: "Invoice"

  - name: "amountRemaining"
    type: "number, string"
    description: |
      - `CreditMemo` - The amount remaining in the credit memo.
      - `Invoice` - The amount due for the invoice.
    transaction-types:
      - name: "CreditMemo"
      - name: "Invoice"

  - name: "ancillaryEndorsementFedEx"
    type: "varies"
    description: |
      - `ItemFulfillment` - The Address Correction or Return Service for SmartPost returns.
    transaction-types:
      - name: "ItemFulfillment"

  - name: "apAcct"
    type: "varies"
    description: ""
    transaction-types:

  - name: "applied"
    type: "number, string"
    description: |
      - `CreditMemo` - The amount of credit applied.
      - `CustomerPayment` - The amount of total payments applied.
      - `DepositApplication` - The amount of deposit applied.
    transaction-types:
      - name: "CreditMemo"
      - name: "CustomerPayment"
      - name: "DepositApplication"

  - name: "applyList"
    type: "varies"
    description: |
      - `CreditMemo`, `CustomerDeposit`, `CustomerPayment`, `CustomerRefund`, `DepositApplication`
    transaction-types:
      - name: "CreditMemo"
      - name: "CustomerDeposit"
      - name: "CustomerPayment"
      - name: "CustomerRefund"
      - name: "DepositApplication"

  - name: "approvalStatus"
    type: "varies"
    description: |
      - `ExpenseReport` - The status of the transaction in the approval process. Possible values include `Pending Approval`, `Approved`, `Rejected`
    transaction-types:
      - name: "ExpenseReport"
      - name: "Invoice"

  - name: "approved"
    type: "boolean, string"
    description: |
      - `JournalEntry` - Indicates whether the journal entry was approved. Journal entries are posted upon approval.
    transaction-types:
      - name: "InterCompanyJournalEntry"
      - name: "JournalEntry"

  - name: "arAcct"
    type: "varies"
    description: |
      - `CustomerPayment`, `DepositApplication` - The Accounts Receivable account that will be affected by the transaction.
    transaction-types:
      - name: "CustomerPayment"
      - name: "DepositApplication"

  - name: "assemblyItem"
    type: "varies"
    description: ""
    transaction-types:

  - name: "authCode"
    type: "string"
    description: "The authorization code for the transaction."
    transaction-types:

  - name: "autoApply"
    type: "boolean, string"
    description: |
      - `CreditMemo` - Indicates if credit will be automatically applied to the oldest open receivable.
      - `CustomerPayment` - Indicates if payments will be automatically applied to the oldest open receivable.
    transaction-types:
      - name: "CreditMemo"
      - name: "CustomerPayment"

  - name: "autoCalculateLag"
    type: "boolean, string"
    description: ""
    transaction-types:

  - name: "availableVendorCredit"
    type: "number, string"
    description: ""
    transaction-types:

  - name: "b13AFilingOptionFedEx"
    type: "varies"
    description: |
      - `ItemFulfillment` - 
    transaction-types:
      - name: "ItemFulfillment"

  - name: "b13AStatementDataFedEx"
    type: "string"
    description: |
      - `ItemFulfillment` - 
    transaction-types:
      - name: "ItemFulfillment"

  - name: "backupEmailAddressFedEx"
    type: "string"
    description: |
      - `ItemFulfillment` - 
    transaction-types:
      - name: "ItemFulfillment"

  - name: "backupEmailAddressUps"
    type: "string"
    description: |
      - `ItemFulfillment` - 
    transaction-types:
      - name: "ItemFulfillment"

  - name: "balance"
    type: "number, string"
    description: |
      - `CreditMemo` - The balance of the credit memo.
      - `CustomerPayment`, `CustomerRefund` - The balance in the customer's account.
    transaction-types:
      - name: "Check"
      - name: "CreditMemo"
      - name: "CustomerPayment"
      - name: "CustomerRefund"
      - name: "Invoice"

  - name: "billAddressList"
    type: "varies"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - The billing address for the transaction, which is the billing address for the customer associated with the transaction.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "billOfMaterials"
    type: "varies"
    description: |
      - `AssemblyBuild` - The bill of materials to associate with the assembly.
      - `AssemblyUnbuild` - The bill of materials associated with the unassembly.
    transaction-types:
      - name: "AssemblyBuild"
      - name: "AssemblyUnbuild"

  - name: "billOfMaterialsRevision"
    type: "varies"
    description: |
      - `AssemblyBuild` - The bill of materials revision associated with the assembly.
      - `AssemblyUnbuild` - The bill of materials revision associated with the unassembly.
    transaction-types:
      - name: "AssemblyBuild"
      - name: "AssemblyUnbuild"

  - name: "billPay"
    type: "boolean, string"
    description: |
      Indicates if the check for the transaction can be sent online.
    transaction-types:
      - name: "Check"
      

  - name: "billingAccount"
    type: "varies"
    description: |
      - `CashSale` - 
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "billingAddress"
    type: "varies"
    description: |
      - `CashSale`, `CreditMemo`, `Estimate` - The billing address for the transaction.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "billingSchedule"
    type: "varies"
    description: |
      - `CashSale` - 
      - `Estimate` - The billing schedule associated with the transaction.
    transaction-types:
      - name: "CashSale"
      - name: "Estimate"
      - name: "Invoice"

  - name: "binNumbers"
    type: "string"
    description: |
      - `AssemblyBuild` - The bin numbers associated with the transaction.
      - `AssemblyUnbuild` - The bin numbers associated with the transaction.
    transaction-types:
      - name: "AssemblyBuild"
      - name: "AssemblyUnbuild"

  - name: "blanketEndDateUps"
    type: "date-time"
    description: |
      - `ItemFulfillment` - The expiration date for the NAFTA certificate of origin.
    transaction-types:
      - name: "ItemFulfillment"

  - name: "blanketStartDateUps"
    type: "date-time"
    description: |
      - `ItemFulfillment` - The start date for the blanket period that the NAFTA certificate of origin is in effect.
    transaction-types:
      - name: "ItemFulfillment"

  - name: "bookingConfirmationNumFedEx"
    type: "string"
    description: ""
    transaction-types:

  - name: "buildable"
    type: "number, string"
    description: |
      - `AssemblyBuild` - Indicates the number of assembly items possible, determined by the amount of member items in stock.
    transaction-types:
      - name: "AssemblyBuild"

  - name: "built"
    type: "number, string"
    description: |
      - `AssemblyUnbuild` - Indicates the number of built assembly items.
    transaction-types:
      - name: "AssemblyUnbuild"

  - name: "canHaveStackable"
    type: "boolean, string"
    description: |
      - `CashSale` - 
      - `Estimate` - 
    transaction-types:
      - name: "CashSale"
      - name: "Estimate"
      - name: "Invoice"

  - name: "carrierIdUps"
    type: "string"
    description: |
      - `ItemFulfillment` - The four-digit Standard Carrier Alpha Code (SCAC) of the carrier for vessel, rail, and truck shipments, or the two to three character International Air Transport Association (IATA) code of carrier for air shipments. Refer to the [United States Census Bureau](www.census.gov/foreign-trade){:target="new"} for info on codes.
    transaction-types:
      - name: "ItemFulfillment"

  - name: "cashBackList"
    type: "varies"
    description: ""
    transaction-types:
      - name: "Deposit"

  - name: "ccApproved"
    type: "boolean, string"
    description: |
      - `CashRefund`, `CashSale`, `CustomerDeposit`, `CustomerPayment`, `CustomerRefund` - Indicates if the credit card associated with the transaction is approved.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CustomerDeposit"
      - name: "CustomerPayment"
      - name: "CustomerRefund"

  - name: "ccAvsStreetMatch"
    type: "varies"
    description: |
      - `CashSale`, `CustomerDeposit`, `CustomerPayment` - The Address Verification Services (AVS) result code returned to Verisign if paid via credit card. Possible values include `_Y` (Address matches), `_N,` (Address doesn't match) `_X` (AVS is unsupported or no info was returned to Versign).
    transaction-types:
      - name: "CashSale"
      - name: "CustomerDeposit"
      - name: "CustomerPayment"

  - name: "ccAvsZipMatch"
    type: "varies"
    description: |
      - `CashSale`, `CustomerDeposit`, `CustomerPayment` - The Address Verification Services (AVS) result code returned to Verisign if paid via credit card. Possible values include `_Y` (Zip code matches), `_N,` (Zip code doesn't match) `_X` (AVS is unsupported or no info was returned to Versign).
    transaction-types:
      - name: "CashSale"
      - name: "CustomerDeposit"
      - name: "CustomerPayment"

  - name: "ccExpireDate"
    type: "date-time"
    description: |
      - `CashRefund`, `CashSale`, `CustomerDeposit`, `CustomerPayment`, `CustomerRefund` - The expiration date of the credit card associated with the transaction.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CustomerDeposit"
      - name: "CustomerPayment"
      - name: "CustomerRefund"

  - name: "ccIsPurchaseCardBin"
    type: "boolean, string"
    description: |
      - `CashRefund`, `CashSale`, `CustomerDeposit`, `CustomerPayment`, `CustomerRefund` - Indicates whether the credit card is a purchase card. This is associated with {{ integration.display_name }}'s Send Purchase Card Data feature.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CustomerDeposit"
      - name: "CustomerPayment"
      - name: "CustomerRefund"

  - name: "ccName"
    type: "string"
    description: |
      - `CashRefund`, `CashSale`, `CustomerDeposit`, `CustomerPayment` - The cardholder name from the default credit card on the customer's record.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CustomerDeposit"
      - name: "CustomerPayment"

  - name: "ccNumber"
    type: "string"
    description: |
      - `CashRefund`, `CashSale`, `CustomerDeposit`, `CustomerPayment` - The credit card number. **Note**: This value will be masked when replicated from {{ integration.display_name }}.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CustomerDeposit"
      - name: "CustomerPayment"

  - name: "ccProcessAsPurchaseCard"
    type: "boolean, string"
    description: |
      - `CashRefund`, `CashSale`, `CustomerDeposit`, `CustomerPayment` - Indicates if {{ integration.display_name }} has determined the credit card to be a purchase card and it should be processed as such.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CustomerDeposit"
      - name: "CustomerPayment"

  - name: "ccSecurityCode"
    type: "string"
    description: |
      - `CashSale`, `CustomerDeposit`, `CustomerPayment` - The three-digit security code from the back of the customer's credit card.
    transaction-types:
      - name: "CashSale"
      - name: "CustomerDeposit"
      - name: "CustomerPayment"

  - name: "ccSecurityCodeMatch"
    type: "varies"
    description: |
      - `CashSale`, `CustomerDeposit`, `CustomerPayment` - The Card Security Code (CSC) result code returned from Verisign when paid via credit ccard. Possible values include `Y` (Code matches), `N` (Code doesn't match)`, `X` (CSC is unuspported or no info was returned to Verisign).
    transaction-types:
      - name: "CashSale"
      - name: "CustomerDeposit"
      - name: "CustomerPayment"

  - name: "ccStreet"
    type: "string"
    description: |
      - `CashRefund`, `CashSale`, `CustomerDeposit`, `CustomerPayment`, `CustomerRefund` - The street address from the customer's billing address.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CustomerDeposit"
      - name: "CustomerPayment"
      - name: "CustomerRefund"

  - name: "ccZipCode"
    type: "string"
    description: |
      - `CashRefund`, `CashSale`, `CustomerDeposit`, `CustomerPayment`, `CustomerRefund` - The zip code from the customer's billing address.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CustomerDeposit"
      - name: "CustomerPayment"
      - name: "CustomerRefund"

  - name: "chargeIt"
    type: "boolean, string"
    description: |
      - `CashRefund`, `CashSale`, `CustomerDeposit`, `CustomerPayment` - If the refund is by credit card, this indicates whether the credit can be processed over the internet.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CustomerDeposit"
      - name: "CustomerPayment"
      - name: "CustomerRefund"

  - name: "checkNum"
    type: "string"
    description: |
      - `CustomerDeposit`, `CustomerPayment` - If the customer paid by check, this will be the check number.
    transaction-types:
      - name: "CustomerDeposit"
      - name: "CustomerPayment"

  - name: "companyContributionList"
    type: "varies"
    description: ""
    transaction-types:

  - name: "companyTaxList"
    type: "varies"
    description: ""
    transaction-types:

  - name: "complete"
    type: "boolean, string"
    description: |
      - `ExpenseReport` - Indicates if the expense report is complete.
    transaction-types:
      - name: "ExpenseReport"

  - name: "completedQuantity"
    type: "number, string"
    description: ""
    transaction-types:

  - name: "componentList"
    type: "varies"
    description: |
      - `AssemblyUnbuild` - 
    transaction-types:
      - name: "AssemblyBuild"
      - name: "AssemblyUnbuild"

  - name: "contribPct"
    type: "string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - 
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "costComponentList"
    type: "varies"
    description: |
      - `InventoryCostRevaluation` - 
    transaction-types:
      - name: "InventoryCostRevaluation"

  - name: "createdDate"
    type: "date-time"
    description: |
      - `AssemblyUnbuild` - 
      - `Deposit` - The date the deposit was created.
    transaction-types:
      - name: "AssemblyUnbuild"
      - name: "Deposit"
      - name: "Estimate"
      - name: "ExpenseReport"
      - name: "InterCompanyJournalEntry"
      - name: "InventoryAdjustment"
      - name: "InventoryTransfer"
      - name: "Invoice"
      - item: "ItemFulfillment"

  - name: "createdFrom"
    type: "varies"
    description: |
      - `CashRefund` - The return authorization the refund is created from.
      - `CashSale` - The sales order the sale is associated with.
      - `CreditMemo` - 
      - `ItemFulfillment` - The sales order the fulfillment is created from.
      - `JournalEntry` - The original transaction being voided.
    transaction-types:
      - name: "AssemblyBuild"
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "InterCompanyJournalEntry"
      - name: "Invoice"
      - item: "ItemFulfillment"
      - name: "JournalEntry"

  - name: "createdFromShipGroup"
    type: "integer, string"
    description: ""
    transaction-types:
      - item: "ItemFulfillment"

  - name: "creditCard"
    type: "varies"
    description: |
      - `CashRefund`, `CashSale`, `CustomerDeposit`, `CustomerPayment`, `CustomerRefund` - A reference to the credit card records associated with the customer.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CustomerDeposit"
      - name: "CustomerPayment"
      - name: "CustomerRefund"

  - name: "creditCardProcessor"
    type: "varies"
    description: |
      - `CashRefund`, `CashSale`, `CustomerDeposit`, `CustomerPayment`, `CustomerRefund` - References the credit card processor used to process the payment.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CustomerDeposit"
      - name: "CustomerPayment"
      - name: "CustomerRefund"

  - name: "creditLimit"
    type: "number, string"
    description: ""
    transaction-types:

  - name: "creditList"
    type: "varies"
    description: |
      - `CustomerPayment` -
    transaction-types:
      - name: "CustomerPayment"

  - name: "currency"
    type: "varies"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `CustomerDeposit` - The currency of the customer associated with the transaction.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CustomerDeposit"
      - name: "CustomerPayment"
      - name: "CustomerRefund"
      - name: "DepositApplication"
      - name: "Estimate"
      - name: "InterCompanyJournalEntry"
      - name: "Invoice"

  - name: "currencyName"
    type: "string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `CustomerDeposit` - The name of the currency associated with the customer.
      - `Deposit` - The currency of the bank account associated with the transaction.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "CustomerDeposit"
      - name: "Deposit"
      - name: "Estimate"
      - name: "Invoice"

  - name: "customFieldList"
    type: "varies"
    description: ""
    transaction-types:
      - name: "all"

  - name: "customForm"
    type: "varies"
    description: "The custom form associated with the transaction."
    transaction-types:
      - name: "all"

  - name: "customer"
    type: "varies"
    description: |
      - `CustomerPayment`, `DepositApplication` - A reference to a customer or job.
      - `CustomerRefund` - A reference to the customer associated with the transaction.
    transaction-types:
      - name: "CustomerPayment"
      - name: "CustomerRefund"
      - name: "DepositApplication"
      - name: "InventoryAdjustment"

  - name: "debitCardIssueNo"
    type: "string"
    description: |
      - `CashRefund`, `CashSale`, `CustomerPayment` - **For UK accounts only.** The debit card authorization number.
      - `CustomerDeposit`, `CustomerRefund` - If the customer paid by debit card, this will be the card's issue number.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CustomerDeposit"
      - name: "CustomerPayment"
      - name: "CustomerRefund"

  - name: "deductionList"
    type: "varies"
    description: ""
    transaction-types:

  - name: "deferredRevenue"
    type: "number, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo` - The amount of revenue deferred on the transaction.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Invoice"
      - name: ""

  - name: "depDate"
    type: "date-time"
    description: |
      - `DepositApplication` - The date the pre-payment was originally deposited.
    transaction-types:
      - name: "DepositApplication"
      - name: ""
      - name: ""
      - name: ""
      - name: ""

  - name: "department"
    type: "varies"
    description: "The department associated with the transaction."
    transaction-types:
      - name: "all"

  - name: "deposit"
    type: "varies"
    description: |
      - `DepositApplication` - A reference to the customer deposit being applied.
    transaction-types:
      - name: "DepositApplication"
      - name: ""
      - name: ""
      - name: ""
      - name: ""

  - name: "depositList"
    type: "varies"
    description: |
      - `CustomerPayment` - 
      - `CustomerRefund` -
    transaction-types:
      - name: "CustomerPayment"
      - name: "CustomerRefund"

  - name: "discountAmount"
    type: "number, string"
    description: |
      - `Invoice` - The discount the customer will recieve if the invoice is paid according to the set terms.
    transaction-types:
      - name: "Invoice"

  - name: "discountDate"
    type: "date-time"
    description: |
       - `Invoice` - The date the customer must pay the invoice by to receive the discount.
    transaction-types:
      - name: "Invoice"

  - name: "discountItem"
    type: "varies"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - The discount item associated with the transaction.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "discountRate"
    type: "string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - The discount rate for `discountItem`. If the value includes a percent sign (`%`), this is calculated as percent. Otherwise, this is calculated as an absolute discount value.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "discountTotal"
    type: "number, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - The total of the amount discounted.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "drAccount"
    type: "varies"
    description: ""
    transaction-types:

  - name: "dueDate"
    type: "date-time"
    description: |
      - `Estimate` - The due date for the estimate.
      - `ExpenseReport` - The due date for the expense report.
    transaction-types:
      - name: "Estimate"
      - name: "ExpenseReport"
      - name: "Invoice"

  - name: "earningList"
    type: "varies"
    description: ""
    transaction-types:

  - name: "eccNumberUps"
    type: "string"
    description: |
      - `ItemFulfillment` - The Export Control Classification Number for the fulfillment.
    transaction-types:
      - item: "ItemFulfillment"

  - name: "email"
    type: "string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo` - The email address(es) that should receive notification about the transaction.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "employee"
    type: "varies"
    description: ""
    transaction-types:

  - name: "employeeTaxList"
    type: "varies"
    description: ""
    transaction-types:

  - name: "endDate"
    type: "date-time"
    description: |
      - `CashSale` - The date for the last cash sale.
      - `Estimate` - The end date for the estimate.
    transaction-types:
      - name: "CashSale"
      - name: "Estimate"
      - name: "Invoice"
      - name: ""

  - name: "endOperation"
    type: "varies"
    description: ""
    transaction-types:

  - name: "entity"
    type: "varies"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate`, `Invoice` - The customer associated with the transaction.
      - `ExpenseReport` - The employee associated with the expense report.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "Check"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "ExpenseReport"
      - name: "Invoice"
      - item: "ItemFulfillment"

  - name: "entityStatus"
    type: "varies"
    description: |
      - `Estimate` - The entity status.
    transaction-types:
      - name: "Estimate"

  - name: "entityTaxRegNum"
    type: "varies"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - 
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "entryNumberUps"
    type: "string"
    description: |
      - `ItemFulfillment` - The Import Entry Number for the fulfillment, used when the export transaction is used as proof of export for import transactions.
    transaction-types:
      - item: "ItemFulfillment"

  - name: "estGrossProfit"
    type: "number, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - The estimated gross profit associated with the refund. This is calculated as the revenue amount minus the estimated cost.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "estGrossProfitPercent"
    type: "number, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - The estimated gross profit margin, as a percentage. This is calculated as the estimated gross profit divided by revenue, expressed as a percentage.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "estimatedTotalValue"
    type: "number, string"
    description: |
      - `InventoryAdjustment` - The total value of the change in inventory.
    transaction-types:
      - name: "InventoryAdjustment"

  - name: "exchangeRate"
    type: "number, string"
    description: "The exchange rate associated with the `currency`."
    transaction-types:
      - name: "Check"
      - name: "DepositApplication"
      - name: "Estimate"
      - name: "InterCompanyJournalEntry"
      - name: "Invoice"

  - name: "excludeCommission"
    type: "boolean, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo` - Indicates if the transaction and its subordinate transactions should be excluded from all commission calculations.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Invoice"
      - name: ""

  - name: "expCostDiscAmount"
    type: "number, string"
    description: |
      - `CashSale` - The discount amount associated with expenses for the transaction.
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"
      - name: ""
      - name: ""

  - name: "expCostDiscPrint"
    type: "boolean, string"
    description: |
      - `CashSale` - Indicates if discounts or markups made to expenses should be printed on the invoice for the transaction.
    transaction-types:
      - name: "CashSale"
      - name: ""
      - name: ""
      - name: ""

  - name: "expCostDiscRate"
    type: "string"
    description: |
      - `CashSale` - The rate of the discount or markup item. This rate is applied to selected billable expenses and calculated in the total for the cash sale.
      - `Invoice` - The rate for the discount or markup item.
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "expCostDiscTax1Amt"
    type: "number, string"
    description: |
      - `CashSale` - 
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "expCostDiscTaxable"
    type: "boolean, string"
    description: |
      - `CashSale` - Indicates if expenses associated with the transaction are taxable.
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "expCostDiscount"
    type: "varies"
    description: |
      - `Invoice` - The markup or discount to be applied to expenses billed in the invoice.
    transaction-types:
      - name: "Invoice"

  - name: "expCostDiscprint"
    type: "boolean, string"
    description: |
      - `Invoice` - Indicates if the discount or markup added should be printed on the invoice.
    transaction-types:
      - name: "Invoice"

  - name: "expCostList"
    type: "varies"
    description: |
      - `Invoice` - 
    transaction-types:
      - name: "Invoice"

  - name: "expCostTaxCode"
    type: "varies"
    description: |
      - `CashSale` - The default tax code for expenses associated with the transaction.
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "expCostTaxRate1"
    type: "number, string"
    description: |
      - `CashSale` - The tax rate for `expCostTaxCode`.
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "expCostTaxRate2"
    type: "number, string"
    description: |
      - `CashSale` - The tax rate for `expCostTaxCode`.
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "expandAssembly"
    type: "boolean, string"
    description: ""
    transaction-types:

  - name: "expectedCloseDate"
    type: "date-time"
    description: |
      - `Estimate` - The expected close date of the estimate.
    transaction-types:
      - name: "Estimate"

  - name: "expenseList"
    type: "varies"
    description: ""
    transaction-types:
      - name: "Check"
      - name: "ExpenseReport"

  - name: "expirationDate"
    type: "date-time"
    description: |
      - `AssemblyBuild` - The lot expiration date for lot numbered assembly items.
    transaction-types:
      - name: "AssemblyBuild"

  - name: "exportTypeUps"
    type: "varies"
    description: |
      - `ItemFulfillment` - Possible values include: `Domestic Exports`, `Foreign Exports`, `Foreign Military Sales`
    transaction-types:
      - item: "ItemFulfillment"

  - name: "externalId"
    type: "string"
    description: ""
    transaction-types:

  - name: "fax"
    type: "string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo` -
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "firmed"
    type: "boolean, string"
    description: ""
    transaction-types:

  - name: "fob"
    type: "string"
    description: |
      - `CashSale`, `Estimate` - The location where customers tecnhnically acquire ownership.
    transaction-types:
      - name: "CashSale"
      - name: "Estimate"
      - name: "Invoice"

  - name: "forecastType"
    type: "varies"
    description: |
      - `Estimate` - The forecast type associated with the estimate.
    transaction-types:
      - name: "Estimate"
      - name: ""

  - name: "fxAccount"
    type: "varies"
    description: ""
    transaction-types:

  - name: "generateIntegratedShipperLabel"
    type: "boolean, string"
    description: |
      - `ItemFulfillment` - Indicates if the fulfillment uses a UPS or FedEx-integrated shipping item.
    transaction-types:
      - item: "ItemFulfillment"

  - name: "getAuth"
    type: "boolean, string"
    description: ""
    transaction-types:

  - name: "giftCert"
    type: "varies"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo` - 
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"

  - name: "giftCertApplied"
    type: "number, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo` - 
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Invoice"

  - name: "giftCertAvailable"
    type: "number, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo` - 
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"

  - name: "giftCertRedemptionList"
    type: "varies"
    description: ""
    transaction-types:
      - name: "Invoice"

  - name: "giftCertTotal"
    type: "number, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo` - 
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"

  - name: "halAddr1FedEx"
    type: "string"
    description: ""
    transaction-types:
      - item: "ItemFulfillment"

  - name: "halAddr2FedEx"
    type: "string"
    description: ""
    transaction-types:
      - item: "ItemFulfillment"

  - name: "halAddr3FedEx"
    type: "string"
    description: ""
    transaction-types:
      - item: "ItemFulfillment"

  - name: "halCityFedEx"
    type: "string"
    description: ""
    transaction-types:
      - item: "ItemFulfillment"

  - name: "halCountryFedEx"
    type: "string"
    description: ""
    transaction-types:
      - item: "ItemFulfillment"

  - name: "halPhoneFedEx"
    type: "string"
    description: ""
    transaction-types:
      - item: "ItemFulfillment"

  - name: "halStateFedEx"
    type: "string"
    description: ""
    transaction-types:
      - item: "ItemFulfillment"

  - name: "halZipFedEx"
    type: "string"
    description: ""
    transaction-types:
      - item: "ItemFulfillment"

  - name: "handlingCost"
    type: "number, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo` -  The amount the customer was charged for handling.
      - `Estimate` - The amount the customer will be charged for handling.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"
      - item: "ItemFulfillment"

  - name: "handlingTax1Rate"
    type: "number, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` -  The tax rate for the associated `handlingTaxCode`.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "handlingTax2Rate"
    type: "number, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` -  The tax rate for the associated `handlingTaxCode`.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "handlingTaxCode"
    type: "varies"
    description: |
      - `CashRefund`, `CreditMemo`, `Estimate` - The tax code associated with handling charges.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "hazmatTypeFedEx"
    type: "varies"
    description: ""
    transaction-types:
      - item: "ItemFulfillment"

  - name: "holdAtLocationFedEx"
    type: "boolean, string"
    description: ""
    transaction-types:
      - item: "ItemFulfillment"

  - name: "homeDeliveryDateFedEx"
    type: "date-time"
    description: ""
    transaction-types:
      - item: "ItemFulfillment"

  - name: "homeDeliveryTypeFedEx"
    type: "varies"
    description: ""
    transaction-types:
      - item: "ItemFulfillment"

  - name: "ignoreAvs"
    type: "boolean, string"
    description: |
      - `CashSale`, `CustomerDeposit`, `CustomerPayment` - Indicates if the results of the Address Verification System (AVS) pre-authoriziation check should be ignored.
    transaction-types:
      - name: "CashSale"
      - name: "CustomerDeposit"
      - name: "CustomerPayment"
      - name: ""

  - name: "inbondCodeUps"
    type: "string"
    description: |
      - `ItemFulfillment` - The two-character Foreign Trade Statistics Regulation (FTSR) code used to indicate whether the shipment is being transported under bond. Refer to the [United States Census Bureau](www.census.gov/foreign-trade){:target="new"} for more info.
    transaction-types:
      - item: "ItemFulfillment"

  - name: "inboundShipment"
    type: "varies"
    description: ""
    transaction-types:

  - name: "includeInForecast"
    type: "boolean, string"
    description: |
      - `Estimate` - Indicates if the estimate is to be included in sales forecast reports, key performance indicators, and snapshots.
    transaction-types:
      - name: "Estimate"
      - name: ""

  - name: "incoterm"
    type: "varies"
    description: ""
    transaction-types:

  - name: "insideDeliveryFedEx"
    type: "boolean, string"
    description: |
      - `ItemFulfillment` - Indicates if the shipment can be delivered to a location other than the loading error.
    transaction-types:
      - item: "ItemFulfillment"

  - name: "insidePickupFedEx"
    type: "boolean, string"
    description: |
      - `ItemFulfillment` - Indicates if the shipment can be picked up from a location other than the loading error.
    transaction-types:
      - item: "ItemFulfillment"

  - name: "intercoStatus"
    type: "varies"
    description: ""
    transaction-types:

  - name: "intercoTransaction"
    type: "varies"
    description: ""
    transaction-types:

  - name: "intlExemptionNumFedEx"
    type: "string"
    description: |
      - `ItemFulfillment` -  
    transaction-types:
      - item: "ItemFulfillment"

  - name: "inventoryDetail"
    type: "varies"
    description: |
      - `AssemblyBuild` - Indicates the bin and quantity detail associated with the assembly.
      - `AssemblyUnbuild` - Indicates the bin and quantity detail associated with the unassembly.
    transaction-types:
      - name: "AssemblyBuild"
      - name: "AssemblyUnbuild"

  - name: "inventoryList"
    type: "varies"
    description: |
      - `InventoryTransfer` - 
    ransaction-types:
      - name: "BinTransfer"
      - name: "InventoryTransfer"

  - name: "inventoryValue"
    type: "number, string"
    description: |
      - `InventoryCostRevaluation` - The new inventory value.
    transaction-types:
      - name: "InventoryCostRevaluation"

  - name: "isBackflush"
    type: "boolean, string"
    description: ""
    transaction-types:

  - name: "isBookSpecific"
    type: "boolean, string"
    description: |
      - `JournalEntry` -
    transaction-types:
      - name: "InterCompanyJournalEntry"
      - name: "JournalEntry" 

  - name: "isCargoAircraftOnlyFedEx"
    type: "boolean, string"
    description: ""
    transaction-types:
      - item: "ItemFulfillment"

  - name: "isMultiShipTo"
    type: "boolean, string"
    description: |
      - `CreditMemo` - Indicates that shipping is allowed for more than one address for this transaction.
    transaction-types:
      - name: "CreditMemo"
      - name: ""
      - name: ""

  - name: "isRecurringPayment"
    type: "boolean, string"
    description: |
      - `CashSale`, `CustomerDeposit`, `CustomerPayment` - Indicates if the sale was generated from a sales order for a recurring payment.
    transaction-types:
      - name: "CashSale"
      - name: "CustomerDeposit"
      - name: "CustomerPayment"
      - name: ""

  - name: "isRoutedExportTransactionUps"
    type: "boolean, string"
    description: |
      - `ItemFulfillment` - Indicates if the foreign principal party in interest authorizes a US forwarding agent or other agent to export the merchandise out of the US.
    transaction-types:
      - item: "ItemFulfillment"

  - name: "isTaxable"
    type: "boolean, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - Indicates if the order is taxable.
    ransaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"
  
  - name: "isWip"
    type: "boolean, string"
    description: ""
    transaction-types:

  - name: "item"
    type: "varies"
    description: |
      - `AssemblyBuild` - The assembly item to build.
      - `AssemblyUnbuild` - The assembly item to unbuild.
    # foreign-key-id: "item-id"
    transaction-types:
      - name: "AssemblyBuild"
      - name: "AssemblyUnbuild"
      - name: "InventoryCostRevaluation"

  - name: "itemCostDiscAmount"
    type: "number, string"
    description: |
      - `CashSale` - The discount or markup amount to be applied to the total.
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "itemCostDiscPrint"
    type: "boolean, string"
    description: |
      - `CashSale` - Indicates if a discount or markup was added and should be printed on the invoice.
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "itemCostDiscRate"
    type: "string"
    description: |
      - `CashSale` - The rate of the discount or markup item.
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "itemCostDiscTax1Amt"
    type: "number, string"
    description: |
      - `CashSale` - 
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "itemCostDiscTaxable"
    type: "boolean, string"
    description: |
      - `CashSale` - Indicates if markups should be applied to prices before taxes.
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "itemCostDiscount"
    type: "varies"
    description: |
      - `CashSale` - The discount or markup item to apply to billable items applied to the sale.
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "itemCostList"
    type: "varies"
    description: |
      - `CashSale` - 
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "itemCostTaxCode"
    type: "varies"
    description: |
      - `CashSale` - The default tax code for all items in the sale.
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "itemCostTaxRate1"
    type: "number, string"
    description: |
      - `CashSale` - The tax rate for `itemCostTaxCode`.
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "itemCostTaxRate2"
    type: "number, string"
    description: |
      - `CashSale` - The tax rate for `itemCostTaxCode`.
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "itemFulfillment"
    type: "varies"
    description: ""
    transaction-types:

  - name: "itemList"
    type: "varies"
    description: |
      - `CreditMemo` - 
      - `Estimate` - 
    transaction-types:
      - name: "BinWorksheet"
      - name: "Check"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"
      - item: "ItemFulfillment"

  - name: "job"
    type: "varies"
    description: |
      - `CashRefund` - The job associated with the transaction being refunded.
      - `CashSale` - The job associated with the transaction.
      - `CreditMemo`, `Estimate`, `Invoice` - The project associated with the transaction.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "landedCostMethod"
    type: "varies"
    description: |
      Possible values are: `_quantity`, `_value`, `_weight`
    transaction-types:
      - name: "Check"

  - name: "landedCostPerLine"
    type: "boolean, string"
    description: |
      Indicates if the landed cost per line is to be specified for the transaction.
    transaction-types:
      - name: "Check"
      

  - name: "landedCostsList"
    type: "varies"
    description: ""
    transaction-types:
      - name: "Check"

  - name: "leadSource"
    type: "varies"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - The lead source the transaction is associated with.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "licenseDateUps"
    type: "date-time"
    description: |
      - `ItemFulfillment` - The date of the license number.
    transaction-types:
      - item: "ItemFulfillment"

  - name: "licenseExceptionUps"
    type: "varies"
    description: |
      - `ItemFulfillment` - The license exception symbol for the shipment type.
    transaction-types:
      - item: "ItemFulfillment"

  - name: "licenseNumberUps"
    type: "string"
    description: |
      - `ItemFulfillment` - The license number required when operating under the authority of the Department of the Treasury, Office of Foreign Assets Control license, Department of Justice DEA permit, or any other export license issued by a federal goverment agency.
    transaction-types:
      - item: "ItemFulfillment"

  - name: "lineList"
    type: "varies"
    description: |
      - `JournalEntry` - 
    transaction-types:
      - name: "InterCompanyJournalEntry"
      - name: "JournalEntry"

  - name: "linkedTrackingNumbers"
    type: "string"
    description: |
      - `CashSale` - 
      - `Estimate` - 
    transaction-types:
      - name: "CashSale"
      - name: "Estimate"
      - name: "Invoice"

  - name: "location"
    type: "varies"
    description: "The location for the transaction."
    # foreign-key-id: "location-id"
    transaction-types:
      - name: "all"

  - name: "manufacturingRouting"
    type: "varies"
    description: ""
    transaction-types:

  - name: "memo"
    type: "string"
    description: "An optional memo for the transaction."
    transaction-types:
      - name: "all"

  - name: "message"
    type: "string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - Defaults to the `messageSel` value.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "messageSel"
    type: "varies"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - The message associated with the refund.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "methodOfTransportUps"
    type: "varies"
    description: |
      - `ItemFulfillment` - The method by which the merchandise is exported.
    transaction-types:
      - item: "ItemFulfillment"

  - name: "nextApprover"
    type: "varies"
    description: |
      - `ExpenseReport` - The next approver for the expense report.
    transaction-types:
      - name: "ExpenseReport"
      - name: "Invoice"

  - name: "nextBill"
    type: "date-time"
    description: ""
    transaction-types:

  - name: "nexus"
    type: "varies"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - The nexus of the transaction.
      - `JournalEntry` - The nexus associated with the journal entry, if any.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"
      - name: "JournalEntry"

  - name: "nullFieldList"
    type: "varies"
    description: ""
    transaction-types:

  - name: "onCreditHold"
    type: "string"
    description: |
      - `CreditMemo` - 
    transaction-types:
      - name: "CreditMemo"
      - name: "Invoice"

  - name: "oneTime"
    type: "number, string"
    description: |
      - `Estimate` - 
    transaction-types:
      - name: "Estimate"

  - name: "operationList"
    type: "varies"
    description: ""
    transaction-types:

  - name: "opportunity"
    type: "varies"
    description: |
      - `CashSale` - A reference to opportunities associated with the customer (`entity`).
      - `Estimate` - A reference to the opportunity associated with the estimate.
    transaction-types:
      - name: "CashSale"
      - name: "Estimate"
      - name: "Invoice"

  - name: "options"
    type: "varies"
    description: ""
    transaction-types:

  - name: "orderQuantity"
    type: "number, string"
    description: ""
    transaction-types:

  - name: "orderStatus"
    type: "varies"
    description: ""
    transaction-types:

  - name: "otherList"
    type: "varies"
    description: ""
    transaction-types:
      - name: "Deposit"

  - name: "otherRefNum"
    type: "string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - The customer PO number associated with the refund.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "packageFedExList"
    type: "varies"
    description: |
      - `ItemFulfillment` - 
    transaction-types:
      - item: "ItemFulfillment"

  - name: "packageList"
    type: "varies"
    description: |
      - `ItemFulfillment` - 
    transaction-types:
      - item: "ItemFulfillment"

  - name: "packageUpsList"
    type: "varies"
    description: |
      - `ItemFulfillment` - 
    transaction-types:
      - item: "ItemFulfillment"

  - name: "packageUspsList"
    type: "varies"
    description: |
      - `ItemFulfillment` - 
    transaction-types:
      - item: "ItemFulfillment"

  - name: "packedDate"
    type: "date-time"
    description: |
      - `ItemFulfillment` - 
    transaction-types:
      - item: "ItemFulfillment"

  - name: "parentExpenseAlloc"
    type: "varies"
    description: |
      - `JournalEntry` - The parent expense allocation associated with the journal entry.
    transaction-types:
      - name: "InterCompanyJournalEntry"
      - name: "JournalEntry"

  - name: "partiesToTransactionUps"
    type: "boolean, string"
    description: |
      - `ItemFulfillment` - Indicates if this is a related party transaction.
    transaction-types:
      - item: "ItemFulfillment"

  - name: "partner"
    type: "varies"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - A reference to a partner record. By default, this is the partner set on the `entity` record.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"
      - name: "ItemFulfillment"

  - name: "partnersList"
    type: "varies"
    description: |
      - `CashSale`, `CreditMemo`, `Estimate` - 
    transaction-types:
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "payment"
    type: "number, string"
    description: |
      - `CustomerDeposit` - The currency amount of the deposit.
      - `CustomerPayment` - The total amount of the payment for the customer.
    transaction-types:
      - name: "CustomerDeposit"
      - name: "CustomerPayment"

  - name: "paymentEventDate"
    type: "date-time"
    description: ""
    transaction-types:

  - name: "paymentEventHoldReason"
    type: "varies"
    description: ""
    transaction-types:

  - name: "paymentEventResult"
    type: "varies"
    description: ""
    transaction-types:

  - name: "paymentEventType"
    type: "varies"
    description: ""
    transaction-types:

  - name: "paymentEventUpdatedBy"
    type: "string"
    description: ""
    transaction-types:

  - name: "paymentHold"
    type: "boolean, string"
    description: ""
    transaction-types:

  - name: "paymentList"
    type: "varies"
    description: ""
    transaction-types:
      - name: "Deposit"

  - name: "paymentMethod"
    type: "varies"
    description: |
      - `CashRefund`, `CashSale`, `CustomerPayment`, `CustomerRefund` - The type of card used in the transaction.
      - `CustomerDeposit` - The payment method for the deposit.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CustomerDeposit"
      - name: "CustomerPayment"
      - name: "CustomerRefund"

  - name: "payPalStatus"
    type: "string"
    description: |
      - `CashRefund`, `CashSale` - 
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"

  - name: "payPalTranId"
    type: "string"
    description: |
      - `CashRefund`, `CashSale` - 
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"

  - name: "paypalAuthId"
    type: "string"
    description: |
      - `CashRefund`, `CashSale` - 
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"

  - name: "paypalProcess"
    type: "boolean, string"
    description: |
      - `CashRefund`, `CashSale` - 
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"

  - name: "pending"
    type: "number, string"
    description: |
      - `CustomerPayment` - The sum of unapproved credit card payments for the customer.
    transaction-types:
      - name: "CustomerPayment"

  - name: "pickedDate"
    type: "date-time"
    description: |
      - `ItemFulfillment` - The date the fulfillment was picked.
    transaction-types:
      - name: "ItemFulfillment"

  - name: "pnRefNum"
    type: "string"
    description: |
      - `CashRefund`, `CashSale`, `CustomerDeposit`, `CustomerPayment`, `CustomerRefund` - If you accept credit card payments, this will be the Verisign authentication code when the payment is approved.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CustomerDeposit"
      - name: "CustomerPayment"
      - name: "CustomerRefund"

  - name: "postingPeriod"
    type: "varies"
    description: "The posting period for the transaction."
    transaction-types:
      - name: "all"

  - name: "printVoucher"
    type: "boolean, string"
    description: ""
    transaction-types:

  - name: "probability"
    type: "number, string"
    description: |
      - `Estimate` - The probability of the estimate.
    transaction-types:
      - name: "Estimate"

  - name: "promoCode"
    type: "varies"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - The promotion code applied to the transaction.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "promotionsList"
    type: "varies"
    description: |
      - `CashRefund`, `CashSale`, `Estimate` - 
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "Estimate"
      - name: "Invoice"

  - name: "purchaseContract"
    type: "varies"
    description: ""
    transaction-types:

  - name: "purchaseOrderList"
    type: "varies"
    description: ""
    transaction-types:

  - name: "quantity"
    type: "number, string"
    description: |
      - `AssemblyBuild` - The number of assembly items to build.
      - `AssemblyUnbuild` - The number of assembly items to unbuild.
    transaction-types:
      - name: "AssemblyBuild"
      - name: "AssemblyUnbuild"

  - name: "recipientTaxIdUps"
    type: "string"
    description: |
      - `ItemFulfillment` - The tax ID number of the business receiving the shipment.
    transaction-types:
      - name: "ItemFulfillment"

  - name: "recognizedRevenue"
    type: "number, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo` - The cumulative amount of revenue recognized for the transaction.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Invoice"

  - name: "recurAnnually"
    type: "number, string"
    description: |
      - `Estimate` - 
    transaction-types:
      - name: "Estimate"

  - name: "recurMonthly"
    type: "number, string"
    description: |
      - `Estimate` - 
    transaction-types:
      - name: "Estimate"

  - name: "recurQuarterly"
    type: "number, string"
    description: |
      - `Estimate` - 
    transaction-types:
      - name: "Estimate"

  - name: "recurWeekly"
    type: "number, string"
    description: |
      - `Estimate` - 
    transaction-types:
      - name: "Estimate"

  - name: "recurringBill"
    type: "boolean, string"
    description: |
      - `CashSale` - Indicates if the sale is a recurring bill.
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "refundCheck"
    type: "boolean, string"
    description: |
      - `CashRefund` - Indicates if the refund will be made by check (`TRUE`) or cash or credit card (`FALSE`).
    transaction-types:
      - name: "CashRefund"

  - name: "requestedBy"
    type: "varies"
    description: |
      - `ItemFulfillment` - The fulfillment request that the item fulfillment originated from.
    transaction-types:
      - name: "ItemFulfillment"

  - name: "revCommitStatus"
    type: "varies"
    description: ""
    transaction-types:

  - name: "revRecEndDate"
    type: "date-time"
    description: |
      - `Invoice` - The revenue recognition end date for the line.
    transaction-types:
      - name: "Invoice"

  - name: "revRecOnRevCommitment"
    type: "boolean, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo` - Indicates if a Revenue Commitment or Revenue Commitment reversal should be creaed for the transaction.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Invoice"

  - name: "revRecSchedule"
    type: "varies"
    description: |
      - `CashSale` - The revenue recognition schedule for the transaction.
    transaction-types:
      - name: "CashSale"

  - name: "revRecStartDate"
    type: "date-time"
    description: |
      `CashSale`- The start date for the revenue rec schedule for the transaction.
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "revenueStatus"
    type: "varies"
    description: |
      - `CashRefund`, `CreditMemo` - The status of revenue for the transaction. Possible values are `Pending`, `In Progress`, `Completed`
    transaction-types:
      - name: "CashRefund"
      - name: "CreditMemo"
      - name: "Invoice"

  - name: "reversalDate"
    type: "date-time"
    description: |
      - `JournalEntry` - The date for the reversing entry to be posted.
    transaction-types:
      - name: "InterCompanyJournalEntry"
      - name: "JournalEntry"

  - name: "reversalDefer"
    type: "boolean, string"
    description: |
      - `JournalEntry` - Indicates that the reversal should be made into a memorized transaction that automatically occurrs on the `reversalDate`.
    transaction-types:
      - name: "InterCompanyJournalEntry"
      - name: "JournalEntry"

  - name: "reversalEntry"
    type: "string"
    description: |
      - `JournalEntry` - If the journal entry is a reversal entry, this will reference the reversing entry.
    transaction-types:
      - name: "InterCompanyJournalEntry"
      - name: "JournalEntry"

  - name: "revision"
    type: "varies"
    description: |
      - `AssemblyBuild` - The revision of the assembly build to use.
    transaction-types:
      - name: "AssemblyBuild"

  - name: "salesEffectiveDate"
    type: "date-time"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`  - The sales effective date for the transaction.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Invoice"

  - name: "salesGroup"
    type: "varies"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - The sales team associated with the transaction. Associated with {{ integration.display_name }}'s Team Selling Feature.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "salesOrder"
    type: "varies"
    description: |
      - `CustomerDeposit` - The sales order that the deposit is reserved for. The deposit may only be applied to the order listed here.
    transaction-types:
      - name: "CustomerDeposit"

  - name: "salesRep"
    type: "varies"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - The sales representative associated with the customer in the `entity` field.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "salesTeamList"
    type: "varies"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - 
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "saturdayDeliveryFedEx"
    type: "boolean, string"
    description: |
      - `ItemFulfillment` - Indicates whether FedEx is required to deliver the shipment on a Saturday.
    transaction-types:
      - name: "ItemFulfillment"

  - name: "saturdayDeliveryUps"
    type: "boolean, string"
    description: |
      - `ItemFulfillment` - Indicates whether UPS is required to deliver the shipment on a Saturday.
    transaction-types:
      - name: "ItemFulfillment"

  - name: "saturdayPickupFedex"
    type: "boolean, string"
    description: |
      - `ItemFulfillment` - Indicates whether FedEx is required to pick up the shipment on a Saturday.
    transaction-types:
      - name: "ItemFulfillment"

  - name: "saveOnAuthDecline"
    type: "boolean, string"
    description: ""
    transaction-types:

  - name: "schedulingMethod"
    type: "varies"
    description: ""
    transaction-types:

  - name: "scrapQuantity"
    type: "number, string"
    description: ""
    transaction-types:

  - name: "sendBackupEmailFedEx"
    type: "boolean, string"
    description: |
      - `ItemFulfillment` - Indicates if proof of delivery should be automatically sent when the package is delivered.
    transaction-types:
      - name: "ItemFulfillment"

  - name: "sendBackupEmailUps"
    type: "boolean, string"
    description: |
      - `ItemFulfillment` - Indicates if shipment notifications should be sent to the `backupEmailUps` email.
    transaction-types:
      - name: "ItemFulfillment"

  - name: "sendShipNotifyEmailFedEx"
    type: "boolean, string"
    description: |
      - `ItemFulfillment` - Indicates if the recipient of the shipment should be alerted of the expected delivery date.
    transaction-types:
      - name: "ItemFulfillment"

  - name: "sendShipNotifyEmailUps"
    type: "boolean, string"
    description: |
      - `ItemFulfillment` - Indicates if the recipient of the shipment should be alerted of the package being shipped.
    transaction-types:
      - name: "ItemFulfillment"

  - name: "serialNumbers"
    type: "string"
    description: |
      - `AssemblyBuild` - The serial numbers for the assemblies to build.
      - `AssemblyUnbuild` - The serial numbers for the assemblies to unbuild.
    transaction-types:
      - name: "AssemblyBuild"
      - name: "AssemblyUnbuild"

  - name: "shipAddress"
    type: "string"
    description: ""
    transaction-types:

  - name: "shipAddressList"
    type: "varies"
    description: |
      - `CashSale`, `Estimate` - The shipping address for the transaction.
    transaction-types:
      - name: "CashSale"
      - name: "Estimate"
      - name: "Invoice"
      - name: "ItemFulfillment"

  - name: "shipComplete"
    type: "boolean, string"
    description: ""
    transaction-types:

  - name: "shipDate"
    type: "date-time"
    description: |
      - `CashSale`, `Estimate` - The ship date for the transaction.
    transaction-types:
      - name: "CashSale"
      - name: "Estimate"
      - name: "Invoice"

  - name: "shipDateFedEx"
    type: "date-time"
    description: |
      - `ItemFulfillment` - 
    transaction-types:
      - name: "ItemFulfillment"

  - name: "shipGroupList"
    type: "varies"
    description: |
      - `CashSale`, `Estimate` -
    transaction-types:
      - name: "CashSale"
      - name: "Estimate"
      - name: "Invoice"

  - name: "shipIsResidential"
    type: "boolean, string"
    description: |
      - `CashSale`, `Estimate` - Indicates whether the `shipAddressList` is a residential address.
    transaction-types:
      - name: "CashSale"
      - name: "Estimate"
      - name: "Invoice"
      - name: "ItemFulfillment"

  - name: "shipMethod"
    type: "varies"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - The shipping method for the transaction.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "shipNotifyEmailAddress2Ups"
    type: "string"
    description: ""
    transaction-types:

  - name: "shipNotifyEmailAddressFedEx"
    type: "string"
    description: ""
    transaction-types:

  - name: "shipNotifyEmailAddressUps"
    type: "string"
    description: ""
    transaction-types:

  - name: "shipNotifyEmailMessageUps"
    type: "string"
    description: ""
    transaction-types:

  - name: "shipStatus"
    type: "varies"
    description: ""
    transaction-types:

  - name: "shipTo"
    type: "varies"
    description: ""
    transaction-types:

  - name: "shipmentWeightFedEx"
    type: "number, string"
    description: |
      - `ItemFulfillment` - The total weight of all packages in the order.
    transaction-types:
      - name: "ItemFulfillment"

  - name: "shipmentWeightUps"
    type: "number, string"
    description: |
      - `ItemFulfillment` - The total weight of all packages in the order.
    transaction-types:
      - name: "ItemFulfillment"

  - name: "shippedDate"
    type: "date-time"
    description: ""
    transaction-types:
      - name: "ItemFulfillment"

  - name: "shippingAddress"
    type: "varies"
    description: |
      - `CashSale`, `Estimate` - 
    transaction-types:
      - name: "CashSale"
      - name: "Estimate"
      - name: "Invoice"
      - name: "ItemFulfillment"

  - name: "shippingCost"
    type: "number, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - The shipping cost for the transaction.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"
      - name: "ItemFulfillment"

  - name: "shippingTax1Rate"
    type: "number, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - The tax rate associated with the `shippingTaxCode`.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "shippingTax2Rate"
    type: "number, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - The tax rate associated with the `shippingTaxCode`.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "shippingTaxCode"
    type: "varies"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - The tax code used for shipping costs.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "shopperIpAddress"
    type: "string"
    description: ""
    transaction-types:

  - name: "signatureHomeDeliveryFedEx"
    type: "boolean, string"
    description: ""
    transaction-types:

  - name: "softDescriptor"
    type: "string"
    description: |
      - `CustomerDeposit` - 

  - name: "source"
    type: "string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - The source of the transaction.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "sourceTransactionId"
    type: "string"
    description: ""
    transaction-types:

  - name: "sourceTransactionLine"
    type: "integer, string"
    description: ""
    transaction-types:

  - name: "specialOrder"
    type: "boolean, string"
    description: ""
    transaction-types:

  - name: "startDate"
    type: "date-time"
    description: |
      - `CashSale` - The date for creating the first bill.
      - `Estimate` - The expected closing date for the estimate.
    transaction-types:
      - name: "CashSale"
      - name: "Estimate"
      - name: "Invoice"

  - name: "startOperation"
    type: "varies"
    description: ""
    transaction-types:

  - name: "status"
    type: "string"
    description: "The status of the transaction."
    transaction-types:
      - name: "Check"
      - name: "DepositApplication"
      - name: "ExpenseReport"
      - name: "Invoice"

  - name: "subTotal"
    type: "number, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - The transaction subtotal before any discounts, shipping, handling, or tax costs are added to the order.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "subsidiary"
    type: "varies"
    description: |
      - `Check` - The primary subsidiary associated with the payee.
      - `CashSale`, `CreditMemo`, `CustomerPayment`, `CustomerRefund`, `DepositApplication`, `Estimate`, `JournalEntry` - The subsidiary associated with the transaction.
      - `Deposit` - The subsidiary associated with the bank account for the transaction.
    transaction-types:
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "CustomerPayment"
      - name: "CustomerRefund"
      - name: "Deposit"
      - name: "DepositApplication"
      - name: "Estimate"
      - name: "ExpenseReport"
      - name: "InterCompanyJournalEntry"
      - name: "InventoryAdjustment"
      - name: "Invoice"
      - name: "JournalEntry"
      - name: ""

  - name: "subsidiaryTaxRegNum"
    type: "varies"
    description: |
      - `CashRefund`, `CashSale`, `Estimate` - The tax registration number of the transaction `nexus`.
      - `JournalEntry` - The tax registration number associated with the journal entry, if any.
    transaction-types:
      - name: "CashRefund"
      - name: "Invoice"
      - name: "JournalEntry"

  - name: "supervisorApproval"
    type: "boolean, string"
    description: |
      - `ExpenseReport` - Indicates if supervisor approval is required for the expense report.
    transaction-types:
      - name: "ExpenseReport"

  - name: "syncPartnerTeams"
    type: "boolean, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - Indicates if the sales team on the customer's record should be updated based on modifications to the transaction.
    transaction-types:
      - name: "AssemblyBuild"
      - name: "AssemblyUnbuild"
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CustomerDeposit"
      - name: "CustomerPayment"
      - name: "CustomerRefund"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"
      - name: "JournalEntry"

  - name: "syncSalesTeams"
    type: "boolean, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - Indicates if the sales team on the customer's record should be updated based on modifications to the transaction.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "tax1Amt"
    type: "number, string"
    description: |
      todo
    transaction-types:
      - name: "ExpenseReport"

  - name: "tax2Amt"
    type: "number, string"
    description: |
      todo
    transaction-types:
      - name: "ExpenseReport"

  - name: "tax2Total"
    type: "number, string"
    description: |
      - `Check` - The total amount of PST based on the associated line items.
      - `CashRefund`, `CashSale`, `CreditMemo` - The PST tax total for Canadian accounts.
      - `Estimate` - The tax rate multiplied by the taxable total number of line items.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "Check"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "taxDetailsList"
    type: "varies"
    description: |
      - `CashSale`, `CreditMemo`, `Estimate` -
    transaction-types:
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "taxDetailsOverride"
    type: "boolean, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - Indicates if tax info from the Tax Details subtab of the transaction should be overridden.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "taxItem"
    type: "varies"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - The tax item for the customer associated with the transaction.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "taxRate"
    type: "number, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - The percentage rate of the `taxItem`.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "taxRegOverride"
    type: "boolean, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - Indicates if the values in `nexus` and `subsidiaryTaxRegNum` should be overridden.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "taxTotal"
    type: "number, string"
    description: |
      - `Check` - The total amount of GST based on the associated line items.
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - The total tax applied to the transaction.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "Check"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "ExpenseReport"
      - name: "Invoice"

  - name: "terms"
    type: "varies"
    description: |
      - `Estimate` - The discount term to apply to the estimate.
    transaction-types:
      - name: "Estimate"
      - name: "Invoice"

  - name: "termsFreightChargeFedEx"
    type: "number, string"
    description: ""
    transaction-types:

  - name: "termsInsuranceChargeFedEx"
    type: "number, string"
    description: ""
    transaction-types:

  - name: "termsOfSaleFedEx"
    type: "varies"
    description: ""
    transaction-types:

  - name: "thirdPartyAcctFedEx"
    type: "string"
    description: ""
    transaction-types:

  - name: "thirdPartyAcctUps"
    type: "string"
    description: ""
    transaction-types:

  - name: "thirdPartyCountryFedEx"
    type: "varies"
    description: ""
    transaction-types:

  - name: "thirdPartyCountryUps"
    type: "varies"
    description: ""
    transaction-types:

  - name: "thirdPartyTypeFedEx"
    type: "varies"
    description: ""
    transaction-types:

  - name: "thirdPartyTypeUps"
    type: "varies"
    description: ""
    transaction-types:

  - name: "thirdPartyZipcodeUps"
    type: "string"
    description: ""
    transaction-types:

  - name: "threeDStatusCode"
    type: "string"
    description: |
      - `CashSale`, `CustomerDeposit`, `CustomerPayment` - The payer authentication status.
    transaction-types:
      - name: "CashSale"
      - name: "CustomerDeposit"
      - name: "CustomerPayment"

  - name: "timeDiscAmount"
    type: "number, string"
    description: |
      - `CashSale` - The discount or markup amount applied to billable time for the transaction.
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "timeDiscPrint"
    type: "boolean, string"
    description: |
      - `CashSale` - Indicates if discounts or markups applied to billable time should be printed on the invoice for the transaction.
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "timeDiscRate"
    type: "string"
    description: |
      - `CashSale` - The rate of the discount or markup item applied to billable time for the transaction.
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "timeDiscTax1Amt"
    type: "number, string"
    description: |
      - `CashSale` - 
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "timeDiscTaxable"
    type: "boolean, string"
    description: |
      - `CashSale` - Indicates if the discount or markup item shouled be applied to billable time before taxes are calculated for the transaction.
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "timeDiscount"
    type: "varies"
    description: |
      - `CashSale` - The discount or markup item to apply to billable time for the transaction.
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "timeList"
    type: "varies"
    description: |
      - `CashSale` - 
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "timeTaxCode"
    type: "varies"
    description: |
      - `CashSale` - The default tax code for all time entries in the transaction.
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "timeTaxRate1"
    type: "number, string"
    description: |
      - `CashSale` - The tax rate for `timeTaxCode`.
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "timeTaxRate2"
    type: "number, string"
    description: |
      - `CashSale` - The tax rate for `timeTaxCode`.
    transaction-types:
      - name: "CashSale"
      - name: "Invoice"

  - name: "title"
    type: "string"
    description: |
      - `Estimate` - The title for the estimate.
    transaction-types:
      - name: "Estimate"

  - name: "toAch"
    type: "boolean, string"
    description: ""
    transaction-types:

  - name: "toBeEmailed"
    type: "boolean, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - Indicates if the cash refund should be sent to all emails in the `email` field.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "toBeFaxed"
    type: "boolean, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - Indicates if the cash refund should be sent to all fax numbers in the `fax` field.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "toBePrinted"
    type: "boolean, string"
    description: "Indicates if the transaction should be saved in a queue of checks to print."
    transaction-types:
      - name: "all"
      - name: "Check"
      - name: "Deposit"
      - name: "Estimate"
      - name: "Invoice"

  - name: "toPrint2"
    type: "boolean, string"
    description: |
      - `CashRefund`, `CashSale` - Indicates if the refund check should be added to the check printing queue.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"

  - name: "toSubsidiary"
    type: "varies"
    description: "The second subsidiary for the ledger transaction."
    transaction-types:
      - name: "InterCompanyJournalEntry"

  - name: "total"
    type: "number, string"
    description: |
      - `AssemblyBuild`, `AssemblyUnbuild` - The projected value of the assembly.
      - `CashRefund`, `CashSale`, `CreditMemo`, `CustomerRefund`, `Estimate` - The total of line items, tax, and shipping costs.
      - `CustomerPayment` - The sum of the `payment` amount and any applied credits.
      - `Deposit` - The total amount being deposited.
      - `DepositApplication` - The total amount to apply.
      - `InventoryCostRevaluation` - The total of the adjustment.
    transaction-types:
      - name: "AssemblyBuild"
      - name: "AssemblyUnbuild"
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CustomerDeposit"
      - name: "CustomerPayment"
      - name: "CustomerRefund"
      - name: "CreditMemo"
      - name: "Deposit"
      - name: "DepositApplication"
      - name: "Estimate"
      - name: "InventoryCostRevaluation"
      - name: "Invoice"

  - name: "totalCostEstimate"
    type: "number, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - The estimated cost of the specific number of items. This is calculated as: `estimated rate x quantity = estimated cost`
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "trackingNumbers"
    type: "string"
    description: |
      - `CashSale`, `Estimate` - The shipping tracking number from the shipping company.
    transaction-types:
      - name: "CashSale"
      - name: "Estimate"
      - name: "Invoice"

  - name: "tranDate"
    type: "date-time"
    description: |
      - `AssemblyBuild`, `AssemblyUnbuild` - The date of the transaction.
      - `BinTransfer` - The date of the transfer.
      - `BinWorksheet` - The date of the transaction.
       - The posting date of the check, by default.
      - `CashRefund`, `CashSale`, `CreditMemo`, `CustomerDeposit`, `CustomerPayment`, `CustomerRefund`, `DepositApplication`, `Estimate` - The date of the transaction.
      - `Deposit` - The posting date of the deposit, by default.
    transaction-types:
      - name: "all"

  - name: "tranId"
    type: "string"
    description: "The {{ integration.display_name }}-generated number associated with the transaction."
    transaction-types:
      - name: "all"

  - name: "tranIsVsoeBundle"
    type: "boolean, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo` - Indicates if all items in the transaction shouldb e included as a VSOE bundle.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Invoice"

  - name: "transactionNumber"
    type: "string"
    description: "The {{ integration.display_name }}-generated number for the transaction."
    transaction-types:
      - name: "CashRefund"
      - name: "Check"

  - name: "transferLocation"
    type: "varies"
    description: |
      - `InventoryTransfer` - The location the item will be transferred to.
    transaction-types:
      - name: "InventoryTransfer"

  - name: "unapplied"
    type: "number, string"
    description: |
      - `CreditMemo` - The remaining amount of credit to be applied.
      - `CustomerPayment` - The difference between available and applied payment amounts.
      - `DepositApplication` - The remaining amount of deposit to be applied.
    transaction-types:
      - name: "CustomerPayment"
      - name: "CreditMemo"
      - name: "DepositApplication"

  - name: "undepFunds"
    type: "boolean, string"
    description: |
      - `CashSale` - Indicates if payment is received by cash or check (`TRUE`) or by account (`FALSE`).
      - `CustomerPayment` - Indicates if the payment will be deposited to a bank account later.
    transaction-types:
      - name: "CashSale"
      - name: "CustomerPayment"

  - name: "unitCost"
    type: "number, string"
    description: |
      - `InventoryCostRevaluation` - The new unit cost.
    transaction-types:
      - name: "InventoryCostRevaluation"

  - name: "units"
    type: "varies"
    description: |
      - `AssemblyBuild`, `AssemblyUnbuild` - If the assembly uses Units of Measure, this is the value of the base units.
    transaction-types:
      - name: "AssemblyBuild"
      - name: "AssemblyUnbuild"

  - name: "unitsType"
    type: "varies"
    description: ""
    transaction-types:

  - name: "useItemCostAsTransferCost"
    type: "boolean, string"
    description: ""
    transaction-types:

  - name: "useMultiCurrency"
    type: "boolean, string"
    description: |
      - `ExpenseReport` - Indicates if expenses are allowed to be entered in foreign currencies on the report.
    transaction-types:
      - name: "ExpenseReport"

  - name: "userTaxTotal"
    type: "number, string"
    description: ""
    transaction-types:

  - name: "userTotal"
    type: "number, string"
    description: |
       The dollar amount of the check.
    transaction-types:
      - name: "Check"
      
  - name: "validFrom"
    type: "date-time"
    description: |
      - `CashRefund`, `CashSale`, `CustomerDeposit`, `CustomerPayment`, `CustomerRefund` - The date when the card first became valid.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CustomerDeposit"
      - name: "CustomerPayment"
      - name: "CustomerRefund"

  - name: "vatRegNum"
    type: "string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo`, `Estimate` - The tax ID for UK accounts.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Estimate"
      - name: "Invoice"

  - name: "visibleToCustomer"
    type: "boolean, string"
    description: |
      - `Estimate` - Indicates that the estimate is available to customers in the Customer Center.
    transaction-types:
      - name: "Estimate"

  - name: "voidJournal"
    type: "varies"
    description: |
      - `CustomerRefund` - If the refund was voided, this will be a reference to the journal entry voiding the transaction.
    transaction-types:
      - name: "Check"
      - name: "CustomerRefund"

  - name: "vsoeAutoCalc"
    type: "boolean, string"
    description: |
      - `CashRefund`, `CashSale`, `CreditMemo` - The VSOE allocation amount for the transaction.
    transaction-types:
      - name: "CashRefund"
      - name: "CashSale"
      - name: "CreditMemo"
      - name: "Invoice"
---