---
tap-reference: "xero"

version: "1.0"

foreign-keys:
  - attribute: "AccountID"
    table: "accounts"
    join-on: "AccountID"

  - attribute: "BankTransferID"
    table: "bank_transfers"
    join-on: "BankTransferID"

  - attribute: "BankTransactionID"
    table: "bank_transactions"
    join-on: "BankTransactionID"

  - attribute: "BrandingThemeID"
    table: "branding_themes"
    join-on: "BrandingThemeID"

  - attribute: "ContactGroupID"
    table: "contact_groups"
    join-on: "ContactGroupID"

  - attribute: "ContactID"
    table: "contacts"
    join-on: "ContactID"

  - attribute: "CreditNoteID"
    table: "credit_notes"
    join-on: "CreditNoteID"

  - attribute: "CurrencyCode"
    table: "currencies"
    join-on: "Code"

  - attribute: "FromBankTransactionID"
    table: "bank_transactions"
    join-on: "BankTransactionID"

  - attribute: "ItemID"
    table: "items"
    join-on: "ItemID"

  - attribute: "LinkedTransactionID"
    table: "linked_transactions"
    join-on: "LinkedTransactionID"

  - attribute: "ManualJournalID"
    table: "manual_journals"
    join-on: "ManualJournalID"

  - attribute: "OrganisationID"
    table: "organisations"
    join-on: "OrganisationID"

  - attribute: "OverpaymentID"
    table: "overpayments"
    join-on: "OverpaymentID"

  - attribute: "PrepaymentID"
    table: "prepayments"
    join-on: "PrepaymentID"

  - attribute: "PurchaseOrderID"
    table: "purchase_orders"
    join-on: "PurchaseOrderID"

  - attribute: "ReceiptID"
    table: "receipts"
    join-on: "ReceiptID"

  - attribute: "RepeatingInvoiceID"
    table: "repeating_invoices"
    join-on: "RepeatingInvoiceID"

  # - attribute: "SourceLineItemID"
  #   table: ""
  #   join-on: ""

  # - attribute: "SourceTransactionID"
  #   table: ""
  #   join-on: ""

  - attribute: "TargetTransactionID"
    table: "invoices"
    join-on: "InvoiceID"

  # - attribute: "TargetLineItemID"
  #   table: ""
  #   join-on: ""

  - attribute: "ToBankTransactionID"
    table: "bank_transactions"
    join-on: "BankTransactionID"

  - attribute: "TrackingCategoryID"
    table: "tracking_categories"
    join-on: "TrackingCategoryID"

  - attribute: "UserID"
    table: "users"
    join-on: "UserID"

  - attribute: ""
    table: ""
    join-on: ""


---