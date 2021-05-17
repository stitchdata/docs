---
tap-reference: "xero"

version: "1"

foreign-keys:
  - id: "account-id"
    attribute: "AccountID"
    table: "accounts"
    all-foreign-keys:
      - table: "accounts"
      - table: "bank_transactions"
        subattribute: "BankAccount"
      - table: "bank_transfers"
        subattribute: "FromBankAccount"
      - table: "bank_transfers"
        subattribute: "ToBankAccount"
      - table: "journals"
        subattribute: "JournalLines"
      - table: "payments"
        subattribute: "Account"

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
        subattribute: "BrandingTheme"
      - table: "credit_notes"
      - table: "invoices"
      - table: "purchase_orders"
      - table: "quotes"
      - table: "quotes"
        subattribute: "Contact.BrandingTheme"
      - table: "repeating_invoices"

  - id: "contact-group-id"
    attribute: "ContactGroupID"
    table: "contact_groups"
    all-foreign-keys:
      - table: "contact_groups"
      - table: "contacts"
        subattribute: "ContactGroups"
      - table: "quotes"
        subattribute: "Contacts.ContactGroups"

  - id: "contact-id"
    attribute: "ContactID"
    table: "contacts"
    all-foreign-keys:
      - table: "contacts"
      - table: "credit_notes"
        subattribute: "Contact"
      - table: "invoices"
        subattribute: "Contact"
      - table: "linked_transactions"
      - table: "overpayments"
        subattribute: "Contact"
      - table: "prepayments"
        subattribute: "Contact"
      - table: "quotes"
        subattribute: "Contact"
      - table: "receipts"
        subattribute: "Contact"
      - table: "repeating_invoices"
        subattribute: "Contact"

  - id: "credit-note-id"
    attribute: "CreditNoteID"
    table: "credit_notes"
    all-foreign-keys:
      - table: "credit_notes"
      - table: "invoices"
        subattribute: "CreditNotes"

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
        subattribute: "SourceTransactionID"
      - table: "linked_transactions"
        join-on: "TargetTransactionID"
      - table: "overpayments"
        subattribute: "Allocations.Invoice"
      - table: "payments"
        subattribute: "Invoice"
      - table: "prepayments"
        subattribute: "Allocations.Invoice"

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
        subattribute: "Overpayments"
      - table: "overpayments"
      - table: "payments"
        subattribute: "Overpayment"

  - id: "payment-id"
    attribute: "PaymentID"
    table: "payments"
    all-foreign-keys:
      - table: "expense_claims"
        subattribute: "Payments"
      - table: "invoices"
        subattribute: "Payments"
      - table: "overpayments"
        subattribute: "Payments"
      - table: "payments"

  - id: "prepayment-id"
    attribute: "PrepaymentID"
    table: "prepayments"
    all-foreign-keys:
      - table: "bank_transactions"
      - table: "invoices"
        subattribute: "Prepayments"
      - table: "payments"
        subattribute: "Prepayments"
      - table: "prepayments"

  - id: "purchase-order-id"
    attribute: "PurchaseOrderID"
    table: "purchase_orders"
    all-foreign-keys:
      - table: "purchase_orders"

  - id: "quote-id"
    table: "quotes"
    attribute: "QuoteID"
    all-foreign-keys:
      - table: "quotes"

  - id: "receipt-id"
    attribute: "ReceiptID"
    table: "receipts"
    all-foreign-keys:
      - table: "expense_claims"
        subattribute: "Receipts"
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
        subattribute: "JournalLines"

  - id: "tracking-category-id"
    attribute: "TrackingCategoryID"
    table: "tracking_categories"
    all-foreign-keys:
      - table: "contacts"
        subattribute: "SalesTrackingCategories"
      - table: "contacts"
        subattribute: "PurchasesTrackingCategories"
      - table: "credit_notes"
        subattribute: "LineItems.Tracking"
      - table: "invoices"
        subattribute: "LineItems.Tracking"
      - table: "journals"
        subattribute: "JournalLines.TrackingCategories"
      - table: "manual_journals"
        subattribute: "JournalLines.TrackingCategories"
      - table: "overpayments"
        subattribute: "LineItems.Tracking"
      - table: "prepayments"
        subattribute: "LineItems.Tracking"
      - table: "purchase_orders"
        subattribute: "LineItems.Tracking"
      - table: "quotes"
        subattribute: "LineItems.Tracking"
      - table: "quotes"
        subattribute: "LineItems.Tracking.SalesTrackingCategories"
      - table: "quotes"
        subattribute: "LineItems.Tracking.PurchasesTrackingCategories"
      - table: "quotes"
        subattribute: "TrackingCategory"
      - table: "receipts"
        subattribute: "LineItems.Tracking"
      - table: "repeating_invoices"
        subattribute: "LineItems.Tracking"
      - table: "tracking_categories"

  - id: "user-id"
    attribute: "UserID"
    table: "users"
    all-foreign-keys:
      - table: "expense_claims"
        subattribute: "User"
      - table: "receipts"
        subattribute: "User"
---