---
tap-reference: "xero"

version: "1.0"

foreign-keys:
  - id: "account-id"
    attribute: "AccountID"
    table: "accounts"
    all-foreign-keys:
      - table: "accounts"
      - table: "bank_transactions"
        subtable: "BankAccount"
      - table: "bank_transfers"
        subtable: "FromBankAccount"
      - table: "bank_transfers"
        subtable: "ToBankAccount"
      - table: "journals"
        subtable: "JournalLines"
      - table: "payments"
        subtable: "Account"

  - id: "bank-transfer-id"
    attribute: "BankTransferID"
    table: "bank_transfers"
    all-foreign-keys:
      - table: "bank_transfers"

  - id: "bank-transaction-id"
    attribute: "BankTransactionID"
    table: "bank_transactions"
    all-foreign-keys:
      - table: "bank_transactions"
      - table: "linked_transactions"
        join-on: "SourceTransactionID"

  - id: "branding-theme-id"
    attribute: "BrandingThemeID"
    table: "branding_themes"
    all-foreign-keys:
      - table: "branding_themes"
      - table: "contacts"
        subtable: "BrandingTheme"
      - table: "credit_notes"
      - table: "invoices"
      - table: "purchase_orders"
      - table: "repeating_invoices"

  - id: "contact-group-id"
    attribute: "ContactGroupID"
    table: "contact_groups"
    all-foreign-keys:
      - table: "contact_groups"
      - table: "contacts"
        subtable: "ContactGroups"

  - id: "contact-id"
    attribute: "ContactID"
    table: "contacts"
    all-foreign-keys:
      - table: "contacts"
      - table: "credit_notes"
        subtable: "Contact"
      - table: "invoices"
        subtable: "Contact"
      - table: "linked_transactions"
      - table: "overpayments"
        subtable: "Contact"
      - table: "prepayments"
        subtable: "Contact"
      - table: "receipts"
        subtable: "Contact"
      - table: "repeating_invoices"
        subtable: "Contact"

  - id: "credit-note-id"
    attribute: "CreditNoteID"
    table: "credit_notes"
    all-foreign-keys:
      - table: "credit_notes"
      - table: "invoices"
        subtable: "CreditNotes"

  - id: "currency-code"
    attribute: "CurrencyCode"
    table: "currencies"
    all-foreign-keys:
      - table: "accounts"
      - table: "bank_transactions"
      - table: "credit_notes"
      - table: "currencies"
      - table: "invoices"
      - table: "prepayments"
      - table: "purchase_orders"
      - table: "repeating_invoices"

  - id: "employee-id"
    attribute: "EmployeeID"
    table: "employees"
    all-foreign-keys:
      - table: "employees"

  - id: "expense-claim-id"
    attribute: "ExpenseClaimID"
    table: "expense_claims"
    all-foreign-keys:
      - table: "expense_claims"

  - id: "invoice-id"
    attribute: "IvoiceID"
    table: "invoices"
    all-foreign-keys:
      - table: "invoices"
      - table: "linked_transactions"
        join-on: "SourceTransactionID"
      - table: "linked_transactions"
        join-on: "TargetTransactionID"
      - table: "overpayments"
        subtable: "Allocations"
        join-on: "Invoice__InvoiceID"
      - table: "payments"
        subtable: "Invoice"
      - table: "prepayments"
        subtable: "Allocations"
        join-on: "Invoice__InvoiceID"

  - id: "item-id"
    attribute: "ItemID"
    table: "items"
    all-foreign-keys:
      - table: "items"

  - id: "journal-id"
    attribute: "JournalID"
    table: "journals"
    all-foreign-keys:
      - table: "journals"

  - id: "linked-transaction-id"
    attribute: "LinkedTransactionID"
    table: "linked_transactions"
    all-foreign-keys:
      - table: "linked_transactions"

  - id: "manual-journal-id"
    attribute: "ManualJournalID"
    table: "manual_journals"
    all-foreign-keys:
      - table: "manial_journals"

  - id: "organisation-id"
    attribute: "OrganisationID"
    table: "organisations"
    all-foreign-keys:
      - table: "organisations"

  - id: "overpayment-id"
    attribute: "OverpaymentID"
    table: "overpayments"
    all-foreign-keys:
      - table: "bank_transactions"
      - table: "invoices"
        subtable: "Overpayments"
      - table: "overpayments"
      - table: "payments"
        subtable: "Overpayment"

  - id: "payment-id"
    attribute: "PaymentID"
    table: "payments"
    all-foreign-keys:
      - table: "expense_claims"
        subtable: "Payments"
      - table: "invoices"
        subtable: "Payments"
      - table: "overpayments"
        subtable: "Payments"
      - table: "payments"

  - id: "prepayment-id"
    attribute: "PrepaymentID"
    table: "prepayments"
    all-foreign-keys:
      - table: "bank_transactions"
      - table: "invoices"
        subtable: "Prepayments"
      - table: "payments"
        subtable: "Prepayments"
      - table: "prepayments"

  - id: "purchase-order-id"
    attribute: "PurchaseOrderID"
    table: "purchase_orders"
    all-foreign-keys:
      - table: "purchase_orders"

  - id: "receipt-id"
    attribute: "ReceiptID"
    table: "receipts"
    all-foreign-keys:
      - table: "expense_claims"
        subtable: "Receipts"
      - table: "receipts"

  - id: "repeating-invoice-id"
    attribute: "RepeatingInvoiceID"
    table: "repeating_invoices"
    all-foreign-keys:
      - table: "repeating_invoices"

  - id: "source-transaction-id"
    attribute: "SourceTransactionID"
    table: "linked_transactions"
    all-foreign-keys:
      - table: "bank_transactions"
        join-on: "BankTransactionID"
      - table: "invoices"
        join-on: "InvoiceID"

  - id: "tax-name"
    attribute: "TaxName"
    table: "tax_rates"
    all-foreign-keys:
      - table: "tax_rates"
      - table: "journals"
        subtable: "JournalLines"

  - id: "tracking-category-id"
    attribute: "TrackingCategoryID"
    table: "tracking_categories"
    all-foreign-keys:
      - table: "contacts"
        subtable: "SalesTrackingCategories"
      - table: "contacts"
        subtable: "PurchasesTrackingCategories"
      - table: "credit_notes"
        subtable: "LineItems__Tracking"
      - table: "invoices"
        subtable: "LineItems__Tracking"
      - table: "journals"
        subtable: "JournalLines__TrackingCategories"
      - table: "manual_journals"
        subtable: "JournalLines__TrackingCategories"
      - table: "overpayments"
        subtable: "LineItems__Tracking"
      - table: "prepayments"
        subtable: "LineItems__Tracking"
      - table: "purchase_orders"
        subtable: "LineItems__Tracking"
      - table: "receipts"
        subtable: "LineItems__Tracking"
      - table: "repeating_invoices"
        subtable: "LineItems__Tracking"
      - table: "tracking_categories"

  - id: "user-id"
    attribute: "UserID"
    table: "users"
    all-foreign-keys:
      - table: "expense_claims"
        subtable: "User"
      - table: "receipts"
        subtable: "User"
---