---
title: QuickBooks
permalink: /integrations/saas/quickbooks
redirect_from: /saas-integrations/quickbooks/quickbooks-latest.html

keywords: quickbooks, integration, schema, etl quickbooks, quickbooks etl, quickbooks schema, intuit
summary: "Connection instructions and schema details for Stitch's QuickBooks integration."
format: ## controls formatting options in template
  schema-list: true
  table-desc: true
  list: expand

# -------------------------- #
#     Integration Details    #
# -------------------------- #

name: "quickbooks"
display_name: "QuickBooks"

singer: false
status-url: "http://status.developer.intuit.com/"

api: |
  [{{ integration.display_name }} Online API](https://developer.intuit.com/app/developer/qbo/docs/api/accounting/most-commonly-used/account){:target="new"}

# -------------------------- #
#       Stitch Details       #
# -------------------------- #

status: "Released"
certified: true

historical: "1 year"
frequency: "30 minutes"
tier: "Paid"

anchor-scheduling: true
cron-scheduling: false

table-selection: false
column-selection: false

extraction-logs: false
loading-reports: true

## Row usage details

row-usage-hog: true
row-usage-hog-reasons:
  data-structure: false
  data-volume: false
  lots-of-full-table: false

# -------------------------- #
#      Feature Summary       #
# -------------------------- #

feature-summary: |
  Stitch's {{ integration.display_name }} integration replicates data from a {{ integration.display_name }} Online instance using the {{ integration.api | flatify | strip }}. Refer to the [Schema](#schema) section for a list of objects available for replication.

  **Note**: Currently, replicating data from {{ integration.display_name }} Desktop apps isn't supported.

# -------------------------- #
#     Integration Tables     #
# -------------------------- #

tables:
## Accounts
  - name: "quickbooks_accounts"
    doc-link: https://developer.intuit.com/docs/api/accounting/account
    description: "info about the various account types in your QuickBooks account. An account can be one of five types: asset, liability, revenue (income), expenses, or equity."
    notes: |
      ### Deleted Accounts 
      To account for deleted accounts, look for `false` values in the `active` column. `False` indicates that an account has been archived/soft-deleted but its attributes and references are intact.
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Account ID (<code>id</code>)
      - name: accountssubtype
      - name: accounttype
      - name: active
      - name: classification
      - name: currencyref__name
      - name: currencyref__value
      - name: currentbalance
      - name: currentbalancewithsubaccounts
      - name: domain
      - name: fullyqualifiedname
      - name: subaccount
      - name: domain
      - name: sparse
      - name: synctoken
      - name: metadata__createtime
      - name: metadata__lastupdatedtime

## Bills
  - name: "quickbooks_bills"
    doc-link: https://developer.intuit.com/docs/api/accounting/Bill
    description: "info about AP transactions, or a request-for-payment from a third-party."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Bill ID (<code>id</code>)
      - name: salestermref
      - name: duedate
      - name: balance
      - name: domain
      - name: sparse
      - name: synctoken
      - name: metadata__createtime
      - name: metadata__lastupdatedtime
      - name: txndate
      - name: currencyref__value
      - name: currencyref__name
      - name: linkedtxn<code>*</code>
      - name: line<code>*</code>
      - name: vendorref__value
      - name: vendorref__name
      - name: apaccountref__value
      - name: apaccountref__name
      - name: totalamt

## Bill Payments
  - name: "quickbooks_billpayments"
    doc-link: https://developer.intuit.com/docs/api/accounting/BillPayment
    description: "info about the final transaction in the payment of bills received from a vendor."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Bill Payment ID (<code>id</code>)
      - name: billpayment__vendorref__value
      - name: billpayment__vendorrref__name
      - name: paytime
      - name: checkpayment__bankaccountref__value
      - name: checkpayment__bankaccountref__name
      - name: printstatus
      - name: totalamt
      - name: domain
      - name: sparse
      - name: synctoken
      - name: metadata__createtime
      - name: metadata__lastupdatedtime
      - name: txndate
      - name: privatenote
      - name: line<code>*</code>

## Budgets
  - name: "quickbooks_budgets"
    doc-link: https://developer.intuit.com/docs/api/accounting/Budget
    description: "info about company budgets."
    notes: |
      ### Budget & Budget Details
      If the above is true and you see a `quickbooks_budgets__budgetdetail` subtable in your data warehouse, you can tie the budget details to the top level table using a composite key. This composite key is made up of the budget ID and the row ID: `_sdc_source_key_id` (budget ID) : `_sdc_level_0_id` (row ID)
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Budget ID (<code>id</code>)
      - name: name
      - name: startdate
      - name: enddate
      - name: budgettype
      - name: budgetentrytype
      - name: active
      - name: "budgetdetail<code>*</code>: This array contains <code>budgetdate, amount, accountref__value, accountref__name</code>."
      - name: domain
      - name: sparse
      - name: synctoken
      - name: metadata__createtime
      - name: metadata__lastupdatedtime

## Classes
  - name: "quickbooks_classes"
    doc-link: https://developer.intuit.com/docs/api/accounting/Class
    description: "info about the classes that are applied to the detail lines of transactions. Classes allow you to track segments that aren't tied to a client or project."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Class ID (<code>id</code>)
      - name: name
      - name: subclass
      - name: fullyqualifiedname
      - name: active
      - name: domain
      - name: sparse
      - name: synctoken
      - name: metadata__createtime
      - name: metadata__lastupdatedtime

## Credit Memos
  - name: "quickbooks_creditmemos"
    doc-link: https://developer.intuit.com/docs/api/accounting/CreditMemo
    description: "info about transactions that are refunds or credits of both full and partial payments."
    notes: &custom |
      Also: in addition to the attributes listed below, our QuickBooks integration will replicate any custom fields.
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Credit Memo ID (<code>id</code>)
      - name: remainingcredit
      - name: domain
      - name: sparse
      - name: synctoken
      - name: metadata__createtime
      - name: metadata__lastupdatedtime
      - name: docnumber
      - name: txndate
      - name: line<code>*</code>
      - name: txntaxdetail__totaltax
      - name: customerref__value
      - name: customerref__name
      - name: customermemo__value
      - name: billaddr__id
      - name: billaddr__line1
      - name: billaddr__line2
      - name: billaddr__line3
      - name: billaddr__line4
      - name: shipaddr__id
      - name: shipaddr__line1
      - name: shipaddr__line2
      - name: shipaddr__line3
      - name: shipaddr__line4
      - name: totalamt
      - name: applytaxafterdiscount
      - name: printstatus
      - name: emailstatus
      - name: billemail__address
      - name: balance

## Customers
  - name: "quickbooks_customers"
    doc-link: https://developer.intuit.com/docs/api/accounting/Customer
    description: "info about the people that consume the products or services offered by your business."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Customer ID (<code>id</code>)
      - name: billaddr__id
      - name: billaddr__line1
      - name: billaddr__line2
      - name: billaddr__line3
      - name: billaddr__line4
      - name: taxable
      - name: job
      - name: domain
      - name: sparse
      - name: synctoken
      - name: metadata__createtime
      - name: metadata__lastupdatedtime
      - name: billwithparent
      - name: balance
      - name: balancewithjobs
      - name: preferreddeliverymethod
      - name: givenname
      - name: familyname
      - name: fullyqualifiedname
      - name: companyname
      - name: displayname
      - name: printoncheckname
      - name: active
      - name: primaryphone__freeformnumber
      - name: primaryemailaddr__address

## Departments
  - name: "quickbooks_departments"
    doc-link: https://developer.intuit.com/docs/api/accounting/Department
    description: "info about the departments - stores, sales regions, countries, and so on - in your company."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Department ID (<code>id</code>)
      - name: name
      - name: subdepartment
      - name: fullyqualifiedname
      - name: active
      - name: domain
      - name: sparse
      - name: synctoken
      - name: metadata__createtime
      - name: metadata__lastupdatedtime

## Deposits
  - name: "quickbooks_deposits"
    doc-link: https://developer.intuit.com/docs/api/accounting/Deposit
    description: "info about direct deposits and customer payments moved into the Asset Account after being held in the Undeposited Funds account."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Deposit ID (<code>id</code>)
      - name: deposittoaccountref__value
      - name: deposittoaccountref__name
      - name: totalamt
      - name: txndate
      - name: line<code>*</code>
      - name: domain
      - name: sparse
      - name: synctoken
      - name: metadata__createtime
      - name: metadata__lastupdatedtime

## Employees
  - name: "quickbooks_employees"
    doc-link: https://developer.intuit.com/docs/api/accounting/Employee
    description: "info about the people who work for your company."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Employee ID (<code>id</code>)
      - name: "ssn: Note that when this attribute is retrieved via the QuickBooks API, it will <strong>always</strong> appear as masked."
      - name: primaryaddr__id
      - name: primaryaddr__line1
      - name: primaryaddr__city
      - name: primaryaddr__countrysubdivisioncode
      - name: primaryaddr__postalcode
      - name: billabletime
      - name: domain
      - name: sparse
      - name: synctoken
      - name: metadata__createtime
      - name: metadata__lastupdatedtime
      - name: primaryphone__freeformnumber
      - name: primaryemailaddr__address
      - name: givenname
      - name: familyname
      - name: displayname
      - name: printoncheckname

## Estimates
  - name: "quickbooks_estimates"
    doc-link: https://developer.intuit.com/docs/api/accounting/Estimate
    description: "info about proposals given to customers about pricing for a good or service."
    notes: *custom
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Estimate ID (<code>id</code>)
      - name: docnumber
      - name: txndate
      - name: txnstatus
      - name: line<code>*</code>
      - name: txntaxdetail__totaltax
      - name: customerref__value
      - name: customerref__name
      - name: customermemo__value
      - name: billaddr__id
      - name: billaddr__line1
      - name: billaddr__line2
      - name: billaddr__line3
      - name: billaddr__line4
      - name: shipaddr__id
      - name: shipaddr__line1
      - name: shipaddr__line2
      - name: shipaddr__line3
      - name: shipaddr__line4
      - name: totalamt
      - name: applytaxafterdiscount
      - name: printstatus
      - name: emailstatus
      - name: billemail__address
      - name: domain
      - name: sparse
      - name: synctoken
      - name: metadata__createtime
      - name: metadata__lastupdatedtime

## Invoices
  - name: "quickbooks_invoices"
    doc-link: https://developer.intuit.com/docs/api/accounting/Invoice
    description: "info about invoices, or sales forms that customers pay later."
    notes: *custom
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Invoice ID (<code>id</code>)
      - name: docnumber
      - name: txndate
      - name: customfield<code>*</code>
      - name: linkedtxn<code>*</code>
      - name: line<code>*</code>
      - name: txntaxdetail__txntaxcoderef__value
      - name: txntaxdetail__totaltax
      - name: txntaxdetail__taxline<code>*</code>
      - name: customerref__value
      - name: customerref__name
      - name: customermemo__value
      - name: billaddr__id
      - name: billaddr__line1
      - name: billaddr__line2
      - name: billaddr__line3
      - name: billaddr__line4
      - name: shipaddr__id
      - name: shipaddr__line1
      - name: shipaddr__line2
      - name: shipaddr__line3
      - name: shipaddr__line4
      - name: salestermref__value
      - name: duedate
      - name: totalamt
      - name: applytaxafterdiscount
      - name: printstatus
      - name: emailstatus
      - name: billemail__address
      - name: balance
      - name: domain
      - name: sparse
      - name: synctoken
      - name: metadata__createtime
      - name: metadata__lastupdatedtime

## Items
  - name: "quickbooks_items"
    doc-link: https://developer.intuit.com/docs/api/accounting/Item
    description: "info about the goods and/or services your company sells."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Item ID (<code>id</code>)
      - name: name
      - name: description
      - name: active
      - name: fullyqualifiedname
      - name: taxable
      - name: unitprice
      - name: type
      - name: incomeaccountref__value
      - name: incomeaccountref__name
      - name: purchasedesc
      - name: purchasecost
      - name: expenseaccountref__value
      - name: expenseaccountref__name
      - name: assetaccountref__value
      - name: assetaccountref__name
      - name: trackqtyonhand
      - name: qtyonhand
      - name: invstartdate
      - name: domain
      - name: sparse
      - name: synctoken
      - name: metadata__createtime
      - name: metadata__lastupdatedtime

## Journal Entries
  - name: "quickbooks_journalentries"
    doc-link: https://developer.intuit.com/docs/api/accounting/JournalEntry
    description: "info about Accounts Receivable and Accounts Payable accounts."
    notes: |
      #### Journal Entries & Line Item Details
      If the above is true and you see a `quickbooks_journalentries__line` subtable in your data warehouse, you can tie the line item details to the top level table using a composite key. This composite key is made up of the journal entry ID and the row ID: `_sdc_source_key_id` (journal entry ID) : `_sdc_level_0_id` (row ID).
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Journal Entry ID (<code>id</code>)
      - name: adjustment
      - name: txndate
      - name: txntaxdetail
      - name: line<code>*</code>
      - name: domain
      - name: sparse
      - name: synctoken
      - name: metadata__createtime
      - name: metadata__lastupdatedtime

## Payment Methods
  - name: "quickbooks_paymentmethods"
    doc-link: https://developer.intuit.com/docs/api/accounting/PaymentMethod
    description: "info about the methods used to pay for goods and services."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Payment Method ID (<code>id</code>)
      - name: name
      - name: active
      - name: type
      - name: domain
      - name: sparse
      - name: synctoken
      - name: metadata__createtime
      - name: metadata__lastupdatedtime

## Payments
  - name: "quickbooks_payments"
    doc-link: https://developer.intuit.com/docs/api/accounting/Payment
    description: "info about the payments received for goods and services."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Payment ID (<code>id</code>)
      - name: deposittoaccountref__value
      - name: totalamt
      - name: unappliedamt
      - name: processpayment
      - name: txndate
      - name: line<code>*</code>
      - name: customerref__value
      - name: customerref__name
      - name: customermemo__value
      - name: domain
      - name: sparse
      - name: synctoken
      - name: metadata__createtime
      - name: metadata__lastupdatedtime

## Purchase Orders
  - name: "quickbooks_purchaseorders"
    doc-link: https://developer.intuit.com/docs/api/accounting/PurchaseOrder
    description: "info about purchase orders, or the requests for goods that are sent to vendors."
    notes: *custom
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Purchase Order ID (<code>id</code>)
      - name: docnumber
      - name: txndate
      - name: line<code>*</code>
      - name: currencyref__value
      - name: currencyref__name
      - name: vendoraddr__id
      - name: vendoraddr__line1
      - name: vendoraddr__line2
      - name: vendoraddr__line3
      - name: vendoraddr__line4
      - name: shipaddr__id
      - name: shipaddr__line1
      - name: shipaddr__line2
      - name: shipaddr__line3
      - name: shipaddr__line4
      - name: vendorref__value
      - name: vendorref__name
      - name: apaccountref__value
      - name: apaccountref__name
      - name: totalamt
      - name: postatus
      - name: domain
      - name: sparse
      - name: synctoken
      - name: metadata__createtime
      - name: metadata__lastupdatedtime

## Purchases
  - name: "quickbooks_purchases"
    doc-link: https://developer.intuit.com/docs/api/accounting/Purchase
    description: "info about your company's expenses, such as a purchase made from a vendor. There are three types of purchases: cash, check, and credit card."
    notes: *custom
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Purchase ID (<code>id</code>)
      - name: paymenttype
      - name: purchaseex<code>*</code>
      - name: txndate
      - name: line<code>*</code>
      - name: accountref__value
      - name: accountref__name
      - name: totalamt
      - name: domain
      - name: sparse
      - name: synctoken
      - name: metadata__createtime
      - name: metadata__lastupdatedtime

## Refund Receipts
  - name: "quickbooks_refundreceipts"
    doc-link: https://developer.intuit.com/docs/api/accounting/RefundReceipt
    description: "info about refunds given to customers."
    notes: *custom
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Refund Recept ID (<code>id</code>)
      - name: docname
      - name: txndate
      - name: txntaxdetail__totaltax
      - name: customerref__value
      - name: customerref__name
      - name: customermemo__value
      - name: line<code>*</code>
      - name: billaddr__id
      - name: billaddr__line1
      - name: billaddr__line2
      - name: billaddr__line3
      - name: billaddr__line4
      - name: billaddr__lat
      - name: billaddr__long
      - name: shipaddr__id
      - name: shipaddr__line1
      - name: shipaddr__line2
      - name: shipaddr__line3
      - name: shipaddr__line4
      - name: shipaddr__lat
      - name: shipaddr__long
      - name: totalamt
      - name: applytaxafterdiscount
      - name: printstatus
      - name: billemail__address
      - name: balance
      - name: paymentmethodref__value
      - name: paymentmethodref__name
      - name: deposittoaccountref__value
      - name: deposittoaccountref__name
      - name: domain
      - name: sparse
      - name: synctoken
      - name: metadata__createtime
      - name: metadata__lastupdatedtime

## Sales Receipts
  - name: "quickbooks_salesreceipts"
    doc-link: https://developer.intuit.com/docs/api/accounting/SalesReceipt
    description: "info about the sales receipts given to customers."
    notes: *custom
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Sales Receipt ID (<code>id</code>)
      - name: docname
      - name: txndate
      - name: txntaxdetail__totaltax
      - name: customerref__value
      - name: customerref__name
      - name: customermemo__value
      - name: line<code>*</code>
      - name: billaddr__id
      - name: billaddr__line1
      - name: billaddr__line2
      - name: billaddr__lat
      - name: billaddr__long
      - name: totalamt
      - name: applytaxafterdiscount
      - name: printstatus
      - name: emailstatus
      - name: balance
      - name: paymentrefnum
      - name: deposittoaccountref__value
      - name: deposittoaccountref__name
      - name: domain
      - name: sparse
      - name: synctoken
      - name: metadata__createtime
      - name: metadata__lastupdatedtime

## Tax Agencies
  - name: "quickbooks_taxagencies"
    doc-link: https://developer.intuit.com/docs/api/accounting/TaxAgency
    description: "info about tax agencies, which are associated withy a tax rate. This object identifies the entity that collects those taxes."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Tax Agency ID (<code>id</code>)
      - name: taxtrackedonpremises
      - name: taxtrackedonsales
      - name: displayname
      - name: domain
      - name: sparse
      - name: synctoken
      - name: metadata__createtime
      - name: metadata__lastupdatedtime

## Tax Codes
  - name: "quickbooks_taxcodes"
    doc-link: https://developer.intuit.com/docs/api/accounting/TaxCode
    description: "info about tax codes."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Tax Code ID (<code>id</code>)
      - name: name
      - name: description
      - name: active
      - name: taxable
      - name: taxgroup
      - name: salestaxratelist<code>*</code>
      - name: purchasetaxratelist<code>*</code>
      - name: domain
      - name: sparse
      - name: synctoken
      - name: metadata__createtime
      - name: metadata__lastupdatedtime

## Tax Rates
  - name: "quickbooks_taxrates"
    doc-link: https://developer.intuit.com/docs/api/accounting/TaxRate
    description: "info about tax rates, which are used to calculate tax liability."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Tax Rate ID (<code>id</code>)
      - name: name
      - name: description
      - name: active
      - name: ratevalue
      - name: agencyref
      - name: specialtaxtype
      - name: displaytype
      - name: domain
      - name: sparse
      - name: synctoken
      - name: metadata__createtime
      - name: metadata__lastupdatedtime

## Terms
  - name: "quickbooks_terms"
    doc-link: https://developer.intuit.com/docs/api/accounting/Term
    description: "info about the terms applied to sales."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Term ID (<code>id</code>)
      - name: name
      - name: active
      - name: type
      - name: discountpercent
      - name: duedays
      - name: discountdays
      - name: domain
      - name: sparse
      - name: synctoken
      - name: metadata__createtime
      - name: metadata__lastupdatedtime

## Time Activities
  - name: "quickbooks_timeactivites"
    doc-link: https://developer.intuit.com/docs/api/accounting/TimeActivity
    description: "info about employee time records."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Time Activity ID (<code>id</code>)
      - name: txndate
      - name: nameof
      - name: billablestatus
      - name: taxable
      - name: hourlyrate
      - name: hours
      - name: minutes
      - name: description
      - name: customerref__value
      - name: customerref__name
      - name: itemref__value
      - name: itemref__name
      - name: employeeref__value
      - name: employeeref__name
      - name: domain
      - name: sparse
      - name: synctoken
      - name: metadata__createtime
      - name: metadata__lastupdatedtime

## Transfers
  - name: "quickbooks_tranfsers"
    doc-link: https://developer.intuit.com/docs/api/accounting/Transfer
    description: "info about transfers, or transactions where funds are moved between two accounts from the company's chart of accounts."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Transfer ID (<code>id</code>)
      - name: amount
      - name: txndate
      - name: fromaccountref__value
      - name: fromaccountref__name
      - name: toaccountref__value
      - name: toaccountref__name
      - name: domain
      - name: sparse
      - name: synctoken
      - name: metadata__createtime
      - name: metadata__lastupdatedtime

## Vendor Credits
  - name: "quickbooks_vendorcredits"
    doc-link: https://developer.intuit.com/docs/api/accounting/VendorCredit
    description: "info about AP transactions that are refunds or credits given to vendors."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: true
    attributes:
      - name: Vendor Credit ID (<code>id</code>)
      - name: txndate
      - name: line<code>*</code>
      - name: totalamt
      - name: vendorref__value
      - name: vendorref__name
      - name: apaccountref__value
      - name: apaccountref__name
      - name: domain
      - name: sparse
      - name: synctoken
      - name: metadata__createtime
      - name: metadata__lastupdatedtime

## Vendors
  - name: "quickbooks_vendors"
    doc-link: https://developer.intuit.com/docs/api/accounting/Vendor
    description: "info about the vendors you purchase goods and/or services from."
    notes: 
    replication-method: "Key-based Incremental"
    primary-key: "id"
    nested-structures: false
    attributes:
      - name: Vendor ID (<code>id</code>)
      - name: balance
      - name: acctnum
      - name: vendor1099
      - name: givenname
      - name: famiilyname
      - name: displayname
      - name: printoncheckname
      - name: active
      - name: primaryphone__freeformnumber
      - name: primaryemailaddr__address
      - name: webaddr__uri
      - name: billaddr__id
      - name: billaddr__line1
      - name: billaddr__line2
      - name: billaddr__lat
      - name: billaddr__long
      - name: domain
      - name: sparse
      - name: synctoken
      - name: metadata__createtime
      - name: metadata__lastupdatedtime
---
{% assign integration = page %}
{% include misc/data-files.html %}



{% contentfor setup %}
Connecting your [QuickBooks data](https://quickbooks.intuit.com/cloud-accounting-software/){:target="new"}* to Stitch is a four-step process:

**Note**: Stitch only integrates with online {{ integration.display_name }}. {{ integration.display_name }} for Desktop is not currently supported.

1. [Add QuickBooks as a Stitch data source](#add-stitch-data-source)
2. [Define the Historical Sync](#define-historical-sync)
3. [Define the Replication Frequency](#define-rep-frequency)
4. [Authorize Stitch to access QuickBooks](#authorize-stitch)

{% include integrations/shared-setup/connection-setup.html %}

{% include integrations/saas/setup/historical-sync.html %}

{% include integrations/shared-setup/replication-frequency.html %}

### Authorizing Stitch to Access QuickBooks {#authorize-stitch}

Lastly, you'll be directed to QuickBooks' website to complete the setup.

1. If you're not already signed into your QuickBooks account, enter your credentials and click **Login**.
2. A screen asking for authorization to QuickBooks will display. **Note that Stitch will only ever read your data.**
3. Click **Authorize.**
4. After the authorization process successfully completes, you'll be redirected back to Stitch.
5. Click {{ app.buttons.finish-int-setup }}.

{% include integrations/shared-setup/initial-syncs.html %}
{% endcontentfor %}
