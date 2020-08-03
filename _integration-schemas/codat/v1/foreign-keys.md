---
tap-reference: "codat"

version: "1"

foreign-keys:
  - id: "account-name"
    attribute: "name" 
    table: "accounts"
    all-foreign-keys:
      - table: "accounts"
        join-on: "name"
      - table: "bank_accounts"
        join-on: "accountName"  
        
  - id: "account-id"
    attribute: "accountId"
    table: "accounts"
    all-foreign-keys:
      - table: "accounts"
        join-on: "id"
      - table: "balance_sheets"
        subattribute: "reports.assets"
      - table: "balance_sheets"
        subattribute: "reports.equity"
      - table: "balance_sheets"
        subattribute: "reports.liabilities"
      - table: "profit_and_loss"
        subattribute: "reports.costOfSales"
      - table: "profit_and_loss"
        subattribute: "reports.expenses"
      - table: "profit_and_loss"
        subattribute: "reports.income"
      - table: "profit_and_loss"
        subattribute: "reports.otherExpenses"
      - table: "profit_and_loss"
        subattribute: "reports.otherIncome"
      - table: "bills"
        subattribute: "lineItems.accountRef"
        join-on: "id"
      - table: "items"
        subattribute: "billItem.accountRef"
        join-on: "id"
      - table: "items"
        subattribute: "invoiceItem.accountRef"
        join-on: "id"
      - table: "journal_entries"
        subattribute: "journalLines.accountRef"
        join-on: "id"

  - id: "account-name"
    attribute: "accountName" 
    table: "accounts"
    all-foreign-keys:
      - table: "accounts"
        join-on: "name"
      - table: "bank_accounts"
      - table: "bank_statement_lines"

  - id: "bank-account-id"
    attribute: "id" 
    table: "bank_accounts"
    all-foreign-keys:
      - table: "bank_accounts"
        join-on: "id"        
      - table: "bank_account_transactions"
        join-on: "bankAccountId"

  - id: "bank-statement-id"
    attribute: ""
    table: "bank_statements"
    all-foreign-keys:
      - table: "bank_statements"
        join-on: "id"

  - id: "bill-id"
    attribute: "billId"
    table: "bills"
    all-foreign-keys:
      - table: "bills"
        join-on: "id"

  - id: "bill-payment-id"
    attribute: "id" 
    table: "bill_payments"
    all-foreign-keys:
      - table: "bill_payments"
        join-on: "id"

  - id: "company-id"
    attribute: "companyId"
    table: "companies"
    all-foreign-keys:
      - table: "companies"
        join-on: "id"
      - table: "balance_sheets"
      - table: "bank_statements"
      - table: "bank_statement_lines"
      - table: "bill_payments"
        subattribute: "supplierRef"
      - table: "bills"
      - table: "company_info"
      - table: "customers"
      - table: "invoices"
      - table: "payments"
      - table: "profit_and_loss"
      - table: "suppliers"
      - table: "connections"
      - table: "events"
      - table: "items"
      - table: "journal_entries"
      - table: "tax_rates"
      - table: "bill_payment"
      - table: "bank_account_transactions"
      - table: "bank_accounts"

  - id: "connection-id"
    table: "connections"
    attribute: "connectionId"
    all-foreign-keys:
      - table: "bank_accounts"
      - table: "connections"
        join-on: "id" 

  - id: "credit-note-id"
    attribute: "creditNoteId"
    table: "credit_notes"
    all-foreign-keys:
      - table: "credit_notes"
        join-on: "id"
      - table: "payments"
        subattribute: "lines.links"
        join-on: "id"

  - id: "customer-id"
    attribute: "customerId"
    table: "customers"
    all-foreign-keys:
      - table: "credit_notes"
        subattribute: "customerRef"
        join-on: "id"
      - table: "customers"
        join-on: "id"
      - table: "credit_notes"
        subattribute: "customerRef"
        join-on: "id"
      - table: "payments"
        subattribute: "customerRef"
        join-on: "id"

  - id: "invoice-id"
    attribute: "invoiceId"
    table: "invoices"
    all-foreign-keys:
      - table: "invoices"
        join-on: "id"
      - table: "payments"
        subattribute: "lines.links"
        join-on: "id"

  - id: "item-id"
    attribute: "id" 
    table: "items"
    all-foreign-keys:
      - table: "bills"
        subattribute: "lineItems.itemRef"
        join-on: "id"

      - table: "items"
        join-on: "id"
        
  - id: "journal-id"
    attribute: "id" 
    table: "journal_entries"
    all-foreign-keys:
      - table: "journal_entries"
        join-on: "id"

  - id: "payment-id"
    attribute: "paymentId"
    table: "payments"
    all-foreign-keys:
      - table: "payments"
        join-on: "id"
      - table: "payments"
        subattribute: "lines.links"
        join-on: "id"

  - id: "supplier-id"
    attribute: "supplierId"
    table: "suppliers"
    all-foreign-keys:
      - table: "bills"
        join-on: "supplierRef"
      - table: "suppliers"
        join-on: "id"

  - id: "event-time"
    attribute: "eventTimeUtc" 
    table: "events"
    all-foreign-keys:
      - table: "events"
        join-on: "eventTimeUtc" 

  - id: "supplier-id"
    table: "suppliers"
    attribute: "supplierRef"
    all-foreign-keys:
      - table: "bill_payments"
        subattribute: "supplierRef"
        join-on: "id"
      - table: "bills"

  - id: "tax-id"
    attribute: "id" 
    table: "tax_rates"
    all-foreign-keys:
      - table: "bills"
        subattribute: "lineItems.taxRateRef"
        join-on: "id"

      - table: "items"
        subattribute: "billItem.taxRateRef"
        join-on: "id"

      - table: "items"
        subattribute: "invoiceItem.taxRateRef"
        join-on: "id"

      - table: "tax_rates"
        join-on: "id"

  - id: "transaction-index-id"
    attribute: "transactionIndex" 
    table: "bank_account_transactions"
    all-foreign-keys:
      - table: "bank_account_transactions"
        join-on: "_transactionIndex"
  
  - id: "bank-account-id"
    attribute: "id" 
    table: "bank_accounts"
    all-foreign-keys:
      - table: "bank_accounts"
        join-on: "id"        
      - table: "bank_account_transactions"
        join-on: "bankAccountId"                                   
---