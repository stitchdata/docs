---
tap: "xero"
version: "1.0"

name: "contacts"
doc-link: &api-doc https://developer.xero.com/documentation/api/contacts
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/contacts.json
description: |
  The `contacts` table contains info about the customers and suppliers you do business with.

replication-method: "Incremental"

api-method:
  name: getContacts
  doc-link: *api-doc

attributes:
  - name: "ContactID"
    type: "string"
    primary-key: true
    description: "The contact ID."

  - name: "UpdatedDateUTC"
    type: "date-time"
    replication-key: true
    description: "The date the contact was last updated, in UTC."

  - name: "ContactNumber"
    type: "string"
    description: "An identifier for the contact used in an external system. In Xero, this is the **Contact Code** field in the Contacts UI."

  - name: "AccountNumber"
    type: "string"
    description: "The account number associated with the contact."

  - name: "ContactStatus"
    type: "string"
    description: |
      The current status of the contact. Possible values are:

      - `ACTIVE`
      - `ARCHIVED`

  - name: "Name"
    type: "string"
    description: "The full name of the contact/organisation."

  - name: "FirstName"
    type: "string"
    description: "The first name of the contact."

  - name: "LastName"
    type: "string"
    description: "The last name of the contact."

  - name: "EmailAddress"
    type: "string"
    description: "The email address of the contact."

  - name: "SkypeUserName"
    type: "string"
    description: "The Skype username of the contact."

  - name: "BankAccountDetails"
    type: "string"
    description: "The bank account number of the contact."

  - name: "TaxNumber"
    type: "string"
    description: |
      The tax number of the contact. Depending on the version of Xero you're using, this could be one of the following in the Xero UI:

      - Australia - ABN
      - New Zealand - GST Number
      - UK - VAT Number
      - US and global - Tax ID Number

  - name: "AccountsReceivableTaxType"
    type: "string"
    description: "The default tax type used on AR invoices for the contact."

  - name: "AccountsPayableTaxType"
    type: "string"
    description: "The default tax type used on AP invoices for the contact."

  - name: "Addresses"
    type: "array"
    description: ""

  - name: "Phones"
    type: "array"
    description: ""

  - name: "IsSupplier"
    type: "boolean"
    description: "If `true`, the contact has AP invoices entered against them."

  - name: "IsCustomer"
    type: "boolean"
    description: "If `true`, the contact has AR invoices entered against them."

  - name: "DefaultCurrency"
    type: "string"
    description: "The default currency for raising invoices against the contact."

  - name: "ContactPersons"
    type: "array"
    description: ""
    array-attributes:
      - name: "FirstName"
        type: "string"
        description: "The first name of the contact person."

      - name: "LastName"
        type: "string"
        description: "The last name of the contact person."

      - name: "EmailAddress"
        type: "string"
        description: "The email address of the contact person."

      - name: "IncludeInEmails"
        type: "string"
        description: "If `true`, the contact person should be included on emails with invoices, etc."

  - name: "SalesDefaultAccountCode"
    type: "string"
    description: "The default sales account code for the contact."

  - name: "PurchasesDefaultAccountCode"
    type: "string"
    description: "The default purchases account code for the contact."

  - name: "SalesTrackingCategories"
    type: "array"
    description: "Details about the default sales tracking categories for the contact."

  - name: "PurchasesTrackingCategories"
    type: "array"
    description: "Details about the default purchases tracking categories for the contact."

  - name: "TrackingCategoryName"
    type: "string"
    description: "The name of the Tracking Category assigned to the contact."

  - name: "TrackingCategoryOption"
    type: "string"
    description: "The name of the Tracking Option assigned to the contact."

  - name: "PaymentTerms"
    type: "array"
    description: ""

  - name: "ContactGroups"
    type: "array"
    description: "Details about the contact groups the contact is included in."
    array-attributes:

  - name: "Website"
    type: "string"
    description: "The website address of the contact."

  - name: "BrandingTheme"
    type: "array"
    description: ""
    array-attributes:

  - name: "BatchPayments"
    type: "object"
    description: "Details about the batch payment details for the contact."
    object-attributes:
      - name: "Details"
        type: "string"
        description: ""

      - name: "Reference"
        type: "string"
        description: ""

      - name: "Code"
        type: "string"
        description: ""

      - name: "BankAccountNumber"
        type: "string"
        description: ""

      - name: "BankAccountName"
        type: "string"
        description: ""

  - name: "Discount"
    type: "number"
    description: "The default discount rate for the contact."

  - name: "Balances"
    type: "object"
    description: "Details about the raw AR (sales invoices) and AP (bills) outstanding and overdue amounts associated with the contact."
    object-attributes:
      - name: "AccountsReceivable"
        type: "object"
        description: "Details about the outstanding and/or overdue sales invoices associated with the contact, not converted to base currency."
        object-attributes:
          - name: "Outstanding"
            type: "number"
            description: "The total amount of outstanding sales invoices associated with the contact."

          - name: "Overdue"
            type: "number"
            description: "The total amount of overdue sales invoices associated with the contact."

      - name: "AccountsPayable"
        type: "object"
        description: "Details about the outstanding and/or overdue bills associated with the contact, not converted to base currency."
        object-attributes:
          - name: "Outstanding"
            type: "number"
            description: "The total amount of outstanding bills associated with the contact."

          - name: "Overdue"
            type: "number"
            description: "The total amount of overdue bills associated with the contact."

  - name: "HasAttachments"
    type: "boolean"
    description: "If `true`, the contact has an attachment."

  # - name: "HasValidationErrors"
  #   type: "array"
  #   description: ""
---