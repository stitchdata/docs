---
tap-reference: "codat"

version: "1.0"

foreign-keys:
  - id: "-id"
    attribute: ""
    table: ""
    all-foreign-keys:
      - table: ""
        join-on: "id"

  - id: "account-id"
    attribute: "accountId"
    table: "accounts"
    all-foreign-keys:
      - table: "accounts"
        join-on: "id"
      - table: "balance_sheets"
        subtable: "reports.assets"
      - table: "balance_sheets"
        subtable: "reports.equity"
      - table: "balance_sheets"
        subtable: "reports.liabilities"
      - table: "profit_and_loss"
        subtable: "reports.costOfSales"
      - table: "profit_and_loss"
        subtable: "reports.expenses"
      - table: "profit_and_loss"
        subtable: "reports.income"
      - table: "profit_and_loss"
        subtable: "reports.otherExpenses"
      - table: "profit_and_loss"
        subtable: "reports.otherIncome"

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

  - id: "company-id"
    attribute: "companyId"
    table: "companies"
    all-foreign-keys:
      - table: "companies"
        join-on: "id"
      - table: "balance_sheets"
      - table: "bank_statements"
      - table: "bills"
      - table: "company_info"
      - table: "customers"
      - table: "invoices"
      - table: "payments"
      - table: "profit_and_loss"
      - table: "suppliers"

  - id: "credit-note-id"
    attribute: "creditNoteId"
    table: "credit_notes"
    all-foreign-keys:
      - table: "credit_notes"
        join-on: "id"
      - table: "payments"
        subtable: "lines.links"
        join-on: "id"

  - id: "customer-id"
    attribute: "customerId"
    table: "customers"
    all-foreign-keys:
      - table: "credit_notes"
        subtable: "customerRef"
        join-on: "id"
      - table: "customers"
        join-on: "id"
      - table: "credit_notes"
        subtable: "customerRef"
        join-on: "id"
      - table: "payments"
        subtable: "customerRef"
        join-on: "id"

  - id: "invoice-id"
    attribute: "invoiceId"
    table: "invoices"
    all-foreign-keys:
      - table: "invoices"
        join-on: "id"
      - table: "payments"
        subtable: "lines.links"
        join-on: "id"

  - id: "payment-id"
    attribute: "paymentId"
    table: "payments"
    all-foreign-keys:
      - table: "payments"
        join-on: "id"
      - table: "payments"
        subtable: "lines.links"
        join-on: "id"

  - id: "supplier-id"
    attribute: "supplierId"
    table: "suppliers"
    all-foreign-keys:
      - table: "bills"
        join-on: "supplierRef"
      - table: "suppliers"
        join-on: "id"
---