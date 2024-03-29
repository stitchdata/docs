---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "quickbooks"

version: "2"

foreign-keys:
  - id: "account-id"
    table: "accounts"
    attribute: "value"
    all-foreign-keys:
      - table: "accounts"
        join-on: "Id"
      - table: "accounts"
        subattribute: "ParentRef"
      - table: "bill_payments"
        subattribute: "APAccountRef"
      - table: "bill_payments"
        subattribute: "CheckPayment.BankAccountRef"
      - table: "bill_payments"
        subattribute: "CreditCardPayment.CCAccountRef"
      - table: "bills"
        subattribute: "APAccountRef"
      - table: "bills"
        subattribute: "Line.AccountBasedExpenseLineDetail"
      - table: "budgets"
        subattribute: "BudgetDetail.AccountRef"
      - table: "deposits"
        subattribute: "CashBack.AccountRef"
      - table: "deposits"
        subattribute: "DepositToAccountRef"
      - table: "deposits"
        subattribute: "Line.DepositLineDetail.AccountRef"
      - table: "invoices"
        subattribute: "DepositToAccountRef"
      - table: "invoices"
        subattribute: "Line.DiscountLineDetail.DiscountAccountRef"
      - table: "items"
        subattribute: "AssetAccountRef"
      - table: "items"
        subattribute: "ExpenseAccountRef"
      - table: "items"
        subattribute: "IncomeAccountRef"
      - table: "journal_entries"
        subattribute: "ARAccountRef"
      - table: "journal_entries"
        subattribute: "Line.JournalEntryLineDetail.AccountRef"
      - table: "payments"
        subattribute: "DepositToAccountRef"
      - table: "purchase_orders"
        subattribute: "APAccountRef"
      - table: "purchases"
        subattribute: "AccountRef"
      - table: "purchases"
        subattribute: "Line.AccountBasedExpenseLineDetail.AccountRef"
      - table: "refund_receipts"
        subattribute: "DepositToAccountRef"
      - table: "sales_receipts"
        subattribute: "DepositToAccountRef"
      - table: "sales_receipts"
        subattribute: "Line.DiscountLineDetail.DiscountAccountRef"
      - table: "transfers"
        subattribute: "FromAccountRef"
      - table: "transfers"
        subattribute: "ToAccountRef"
      - table: "vendor_credits"
        subattribute: "APAccountRef"
      - table: "vendor_credits"
        subattribute: "Line.AccountBasedExpenseLineDetail.AccountRef"

  - id: "bill-payment-id"
    table: "bill_payments"
    attribute: ""
    all-foreign-keys:
      - table: "bill_payments"
        join-on: "Id"
      - table: "bills"
        subattribute: "LinkedTxn"
        join-on: "TxnId"

  - id: "bill-id"
    table: "bills"
    attribute: "LinkedTxn.TxnId"
    all-foreign-keys:
      - table: "bill_payments"
        subattribute: "Line"
      - table: "bills"
        join-on: "Id"
      - table: "purchase_orders"

  - id: "class-id"
    table: "classes"
    attribute: "ClassRef.value"
    all-foreign-keys:
      - table: "budgets"
        subattribute: "BudgetDetail"
      - table: "classes"
        join-on: "Id"
      - table: "classes"
        subattribute: "ParentRef"
        join-on: "value"
      - table: "credit_memos"
      - table: "estimates"
      - table: "invoices"
      - table: "invoices"
        subattribute: "Line.SalesItemLineDetail"
      - table: "items"
      - table: "purchase_orders"
      - table: "purchase_orders"
        subattribute: "Line.ItemBasedExpenseLineDetail"
      - table: "purchases"
        subattribute: "Line.AccountBasedExpenseLineDetail"
      - table: "refund_receipts"
      - table: "sales_receipts"
      - table: "time_activities"
      - table: "vendor_credits"
        subattribute: "Line.AccountBasedExpenseLineDetail"

  - id: "credit-memo-id"
    table: "credit_memos"
    attribute: "value"
    all-foreign-keys:
      - table: "credit_memos"
        join-on: "Id"
      - table: "payments"
        subattribute: "Line.LinkedTxn"
        join-on: "TxnId"

  - id: "currency-id"
    table: ""
    attribute: "CurrencyRef.value"
    all-foreign-keys:
      - table: "accounts"
      - table: "bill_payments"
      - table: "bills"
      - table: "credit_memos"
      - table: "customers"
      - table: "deposits"
      - table: "estimates"
      - table: "invoices"
      - table: "journal_entries"
      - table: "payments"
      - table: "purchase_orders"
      - table: "purchases"
      - table: "refund_receipts"
      - table: "sales_receipts"
      - table: "transfers"
      - table: "vendor_credits"
      - table: "vendors"

  - id: "customer-id"
    table: "customers"
    attribute: "CustomerRef.value"
    all-foreign-keys:
      - table: "bills"
        subattribute: "Line.AccountBasedExpenseLineDetail"
      - table: "budgets"
        subattribute: "BudgetDetail"
      - table: "credit_memos"
      - table: "customers"
        join-on: "Id"
      - table: "customers"
        subattribute: "ParentRef"
      - table: "estimates"
      - table: "invoices"
      - table: "payments"
      - table: "purchase_orders"
        subattribute: "Line.ItemBasedExpenseLineDetail"
      - table: "purchases"
        subattribute: "Line.AccountBasedExpenseLineDetail"
      - table: "purchases"
        subattribute: "EntityRef"
      - table: "refund_receipt"
      - table: "sales_receipt"
      - table: "vendor_credits"
        subattribute: "Line.AccountBasedExpenseLineDetail"

  - id: "department-id"
    table: "departments"
    attribute: "DepartmentRef.value"
    all-foreign-keys:
      - table: "bills"
      - table: "bill_payments"
      - table: "budgets"
        subattribute: "BudgetDetail"
      - table: "departments"
        subattribute: "ParentRef"
        join-on: "value"
      - table: "departments"
        join-on: "Id"
      - table: "deposits"
      - table: "estimates"
      - table: "invoices"
      - table: "purchase_orders"
      - table: "purchases"
      - table: "refund_receipts"
      - table: "sales_receipts"
      - table: "time_activities"
      - table: "vendor_credits"

  - id: "deposit-id"
    table: "deposits"
    attribute: "value"
    all-foreign-keys:
      - table: "deposits"
        join-on: "Id"

  - id: "employee-id"
    table: "employees"
    attribute: "value"
    all-foreign-keys:
      - table: "employees"
        join-on: "Id"
      - table: "purchases"
        subattribute: "EntityRef"
      - table: "time_activities"
        subattribute: "EmployeeRef"

  - id: "entity-id"
    table: "purchases"
    attribute: "value"
    all-foreign-keys:
      - table: "customers"
      - table: "employees"
      - table: "vendors"

  - id: "estimate-id"
    table: "estimates"
    attribute: "value"
    all-foreign-keys:
      - table: "estimates"
        join-on: "Id"
      - table: "invoices"
        subattribute: "LinkedTxn"
        join-on: "TxnId"

  - id: "invoice-id"
    table: "invoices"
    attribute: "LinkedTxn.TxnId"
    all-foreign-keys:
      - table: "estimates"
      - table: "invoices"
        join-on: "Id"
      - table: "payments"
        subattribute: "Line"

  - id: "item-id"
    table: "items"
    attribute: "ItemRef.value"
    all-foreign-keys:
      - table: "bills"
        subattribute: "Line.ItemBasedExpenseLineDetail"
      - table: "credit_memos"
        subattribute: "Line.SalesItemLineDetail"
      - table: "estimates"
        subattribute: "Line.SalesItemLineDetail"
      - table: "invoices"
        subattribute: "Line.SalesItemLineDetail"
      - table: "items"
        join-on: "Id"
      - table: "items"
        subattribute: "ParentRef"
        join-on: "value"
      - table: "purchase_orders"
        subattribute: "Line.ItemBasedExpenseLineDetail"
      - table: "purchases"
        subattribute: "Line.ItemBasedExpenseLineDetail"
      - table: "refund_receipts"
        subattribute: "Line.SalesItemLineDetail"
      - table: "sales_receipts"
        subattribute: "Line.SalesItemLineDetail"
      - table: "time_activities"

  - id: "journal-entry-id"
    table: "journal_entries"
    attribute: "LinkedTxn.TxnId"
    all-foreign-keys:
      - table: "bill_payments"
        subattribute: "Line"
      - table: "deposits"
        subattribute: "Line"
      - table: "journal_entries"
        join-on: "Id"

  - id: "payment-id"
    table: "payments"
    attribute: "LinkedTxn.TxnId"
    all-foreign-keys:
      - table: "deposits"
        subattribute: "Line"
      - table: "invoices"
      - table: "payments"
        join-on: "Id"

  - id: "payment-method-id"
    table: "payment_methods"
    attribute: "PaymentMethodRef.value"
    all-foreign-keys:
      - table: "customers"
      - table: "deposits"
        subattribute: "Line.DepositLineDetail"
      - table: "payment_methods"
        join-on: "Id"
      - table: "payments"
      - table: "purchases"
      - table: "refund_receipts"
      - table: "sales_receipts"

  - id: "purchase-id"
    table: "purchases"
    attribute: "LinkedTxn.TxnId"
    all-foreign-keys:
      - table: "invoices"
      - table: "payments"
        subattribute: "Line"
      - table: "purchases"
        join-on: "Id"

  - id: "purchase-order-id"
    table: "purchase_orders"
    attribute: "value"
    all-foreign-keys:
      - table: "bills"
        subattribute: "LinkedTxn"
        join-on: "TxnId"
      - table: "purchase_orders"
        join-on: "Id"

  - id: "refund-receipt-id"
    table: "refund_receipts"
    attribute: "LinkedTxn.TxnId"
    all-foreign-keys:
      - table: "deposits"
        subattribute: "Line"
      - table: "refund_receipts"
        join-on: "Id"

  - id: "sales-receipt-id"
    table: "sales_receipts"
    attribute: "LinkedTxn.TxnId"
    all-foreign-keys:
      - table: "deposits"
        subattribute: "Line"
      - table: "sales_receipts"
        join-on: "Id"

  - id: "tax-agency-id"
    table: "tax_agencies"
    attribute: "value"
    all-foreign-keys:
      - table: "tax_agencies"
        join-on: "Id"
      - table: "tax_rates"
        subattribute: "AgencyRef"

  - id: "tax-code-id"
    table: "tax_codes"
    attribute: "TaxCodeRef.value"
    all-foreign-keys:
      - table: "bills"
        subattribute: "Line.AccountBasedExpenseLineDetail"
      - table: "bills"
        subattribute: "Line.ItemBasedExpenseLineDetail"
      - table: "credit_memos"
        subattribute: "Line.SalesItemLineDetail"
      - table: "customers"
        subattribute: "DefaultTaxCodeRef"
        join-on: "value"
      - table: "estimates"
        subattribute: "Line.SalesItemLineDetail"
      - table: "estimates"
        subattribute: "TxnTaxDetail.TxnTaxCodeRef"
      - table: "invoices"
        subattribute: "Line.SalesItemLineDetail"
      - table: "invoices"
        subattribute: "TxnTaxDetail.TxnTaxCodeRef"
      - table: "items"
        subattribute: "PurchaseTaxCodeRef.value"
      - table: "items"
        subattribute: "SalesTaxCodeRef.value"
      - table: "journal_entries"
        subattribute: "TxnTaxDetail.TxnTaxCodeRef"
        join-on: "value"
      - table: "purchase_orders"
        subattribute: "Line.ItemBasedExpenseLineDetail"
      - table: "purchases"
        subattribute: "Line.AccountBasedExpenseLineDetail"
      - table: "purchases"
        subattribute: "Line.ItemBasedExpenseLineDetail"
      - table: "refund_receipts"
        subattribute: "Line.SalesItemLineDetail"
      - table: "sales_receipts"
        subattribute: "Line.SalesItemLineDetail"
      - table: "vendor_credits"
        subattribute: "Line.AccountBasedExpenseLineDetail"

  - id: "tax-rate-id"
    table: "tax_rates"
    attribute: "TaxRateRef.value"
    all-foreign-keys:
      - table: "estimates"
        subattribute: "TxnTaxDetail.TaxLine.TaxLineDetail"
      - table: "invoices"
        subattribute: "TxnTaxDetail.TaxLine.TaxLineDetail"
      - table: "journal_entries"
      - table: "journal_entries"
        subattribute: "TxnTaxDetail.TaxLine.TaxLineDetail"
      - table: "tax_codes"
        subattribute: "PurchaseTaxRateList.TaxLine.TaxRateDetail"
      - table: "tax_codes"
        subattribute: "SalesTaxRateList.TaxLine.TaxRateDetail"
      - table: "tax_rates"
        join-on: "Id"

  - id: "term-id"
    table: "terms"
    attribute: "SalesTermRef.value"
    all-foreign-keys:
      - table: "bills"
      - table: "credit_memos"
      - table: "customers"
      - table: "estimates"
      - table: "invoices"
      - table: "purchase_orders"
      - table: "terms"
        join-on: "Id"
      - table: "vendors"
        subattribute: "TermRef"

  - id: "time-activity-id"
    table: "time_activities"
    attribute: "value"
    all-foreign-keys:
      - table: "invoices"
        subattribute: "LinkedTxn"
        join-on: "TxnId"
      - table: "time_activities"
        join-on: "Id"

  - id: "transaction-bill-payment-id"
    table: "bill_payments"
    attribute: "Id"
    all-foreign-keys:
      - table: "bills"
      - table: "journal_entries"
      - table: "vendor_credits"

  - id: "transaction-bill-id"
    table: "bills"
    attribute: "Id"
    all-foreign-keys:
      - table: "bill_payment"
      - table: "purchase_orders"

  - id: "transaction-deposit-id"
    table: "deposits"
    attribute: "Id"
    all-foreign-keys:
      - table: "journal_entries"
      - table: "payments"
      - table: "refund_receipts"
      - table: "sales_receipts"
      - table: "transfers"

  - id: "transaction-invoice-id"
    table: "invoices"
    attribute: "Id"
    all-foreign-keys:
      - table: "estimates"
      - table: "payments"
      - table: "purchases"
      - table: "time_activities"

  - id: "transaction-payment-id"
    table: "payments"
    attribute: "Id"
    all-foreign-keys:
      - table: "credit_memos"
      - table: "invoices"
      - table: "purchases"

  - id: "transfer-id"
    table: "transfers"
    attribute: "LinkedTxn.TxnId"
    all-foreign-keys:
      - table: "deposits"
        subattribute: "Line"
      - table: "transfers"
        join-on: "Id"

  - id: "vendor-credit-id"
    table: "vendor_credits"
    attribute: ""
    all-foreign-keys:
      - table: "bill_payments"
        subattribute: "Line.LinkedTxn"
        join-on: "TxnId"
      - table: "vendor_credits"
        join-on: "Id"

  - id: "vendor-id"
    table: "vendors"
    attribute: "VendorRef.value"
    all-foreign-keys:
      - table: "bill_payments"
      - table: "bills"
      - table: "items"
        subattribute: "PrefVendorRef"
        join-on: "value"
      - table: "purchase_orders"
      - table: "purchases"
        subattribute: "EntityRef"
      - table: "time_activities"
      - table: "vendor_credits"
      - table: "vendors"
        join-on: "Id"
---