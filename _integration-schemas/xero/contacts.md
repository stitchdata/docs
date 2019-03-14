---
tap: "xero"
version: "1.0"

name: "contacts"
doc-link: &api-doc https://developer.xero.com/documentation/api/contacts
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/contacts.json
description: |
  The `{{ table.name }}` table contains info about the customers and suppliers you do business with.

replication-method: "Key-based Incremental"

api-method:
  name: getContacts
  doc-link: *api-doc

attributes:
  - name: "ContactID"
    type: "string"
    primary-key: true
    description: "The contact ID."
    foreign-key-id: "contact-id"

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
    description: "Details about the contact's addresses."
    subattributes:
      - name: "Region"
        type: "string"
        description: "The region associated with the address."

      - name: "AddressType"
        type: "string"
        description: |
          The address type. Possible values are:

          - `POBOX`
          - `STREET`
          - `DELIVERY` - **Note**: This address type is not valid for `contacts`.

      - name: "AddressLine1"
        type: "string"
        description: "The first line of the address."

      - name: "AddressLine2"
        type: "string"
        description: "The second line of the address."

      - name: "AddressLine3"
        type: "string"
        description: "The third line of the address."

      - name: "AddressLine4" 
        type: "string"
        description: "The fourth line of the address."

      - name: "AttentionTo" 
        type: "string"
        description: "The name of the addressee."

      - name: "City" 
        type: "string"
        description: "The city associated with the address."

      - name: "PostalCode" 
        type: "string"
        description: "The postal code associated with the address."

      - name: "Country"
        type: "string"
        description: "The country associated with the address."

  - name: "Phones"
    type: "array"
    description: "Details about the contact's phone numbers."
    subattributes:
      - name: "PhoneNumber"
        type: "string"
        description: "The phone number."

      - name: "PhoneAreaCode"
        type: "string"
        description: "The area code associated with the phone number."

      - name: "PhoneCountryCode"
        type: "string"
        description: "The country code associated with the phone number."

      - name: "PhoneType"
        type: "string"
        description: |
          The type of phone number. Possible values are:

          - `DEFAULT`
          - `DDI`
          - `MOBILE`
          - `FAX`

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
    description: "Details about the contact persons associated with the contact."
    subattributes:
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
    subattributes: &tracking-categories
      - name: "TrackingCategoryID"
        type: "string"
        description: "The tracking category ID."
        foreign-key-id: "tracking-category-id"

      - name: "Status"
        type: "string"
        description: "The status of the tracking category."

      - name: "TrackingCategoryName"
        type: "string"
        description: "The name of the tracking category."

      - name: "Name"
        type: "string"
        description: "The name of the tracking option."

      - name: "Option"
        type: "string"
        description: "The value of the tracking option."

      - name: "Options"
        type: "array"
        description: "Details about the tracking option."
        subattributes:
          - name: "IsActive"
            type: "boolean"
            description: "If `true`, the tracking option is active."

          - name: "IsDeleted"
            type: "boolean"
            description: "If `true`, the tracking option has been deleted."

          - name: "TrackingOptionID"
            type: "string"
            description: "The ID of the tracking option."

          - name: "IsArchived"
            type: "boolean"
            description: "If `true`, the tracking option has been archived."

          - name: "Status"
            type: "string"
            description: "The status of the tracking option."

          - name: "Name"
            type: "string"
            description: "The name of the tracking option."

  - name: "PurchasesTrackingCategories"
    type: "array"
    description: "Details about the default purchases tracking categories for the contact."
    subattributes: *tracking-categories

  - name: "TrackingCategoryName"
    type: "string"
    description: "The name of the Tracking Category assigned to the contact."

  - name: "TrackingCategoryOption"
    type: "string"
    description: "The name of the Tracking Option assigned to the contact."

  - name: "PaymentTerms"
    type: "array"
    description: "Details about the contact's payment terms."
    subattributes:
      - name: "Sales"
        type: "object"
        description: "Details about the payment terms used for sales transactions."
        subattributes:
          - name: "Day"
            type: "integer"
            description: "An integer used with the payment term type to indicate the calendar date of the payment term used for sales transactions."

          - name: "Type"
            type: "integer"
            description: |
              The payment term type used for sales transactions. Possible values are:

              - `DAYSAFTERBILLDATE` - _n_ day(s) after the bill date
              - `DAYSAFTERBILLMONTH`- _n_ day(s) after the bill month
              - `OFCURRENTMONTH` - Of the current month
              - `OFFOLLOWINGMONTH` - Of the following month

      - name: "Bills"
        type: "object"
        description: "Details about the payment terms used for bills (invoices)."
        subattributes:
          - name: "Day"
            type: "integer"
            description: "An integer used with the payment term type to indicate the calendar date of the payment term used for bills."

          - name: "Type"
            type: "integer"
            description: |
              The payment term type used for bills (invoices). Possible values are:

              - `DAYSAFTERBILLDATE` - _n_ day(s) after the bill date
              - `DAYSAFTERBILLMONTH`- _n_ day(s) after the bill month
              - `OFCURRENTMONTH` - Of the current month
              - `OFFOLLOWINGMONTH` - Of the following month

  - name: "ContactGroups"
    type: ""
    description: |
      Details about the contact groups the contact is included in.

      {{ integration.subtable-note | flatify | replace: "table_name","contact_groups" }}
    foreign-key-id: "contact-group-id"

  - name: "Website"
    type: "string"
    description: "The website address of the contact."

  - name: "BrandingTheme"
    type: ""
    description: |
      Details about the branding theme applied to documents sent to the contact.

      {{ integration.subtable-note | flatify | replace: "table_name","branding_themes" }}
    foreign-key-id: "branding-theme-id"

  - name: "BatchPayments"
    type: "object"
    description: "Details about the batch payment details for the contact."
    subattributes:
      - name: "Details"
        type: "string"
        description: "Details about the batch payment."

      - name: "Reference"
        type: "string"
        description: "The reference number for the batch payment."

      - name: "Code"
        type: "string"
        description: "The code associated with the batch payment."

      - name: "BankAccountNumber"
        type: "string"
        description: "The bank account number associated with the batch payment."

      - name: "BankAccountName"
        type: "string"
        description: "The name of the bank account associated with the batch payment."

  - name: "Discount"
    type: "number"
    description: "The default discount rate for the contact."

  - name: "Balances"
    type: "object"
    description: "Details about the raw AR (sales invoices) and AP (bills) outstanding and overdue amounts associated with the contact."
    subattributes:

      - name: "AccountsReceivable"
        type: "object"
        description: "Details about the outstanding and/or overdue sales invoices associated with the contact, not converted to base currency."
        subattributes:
          - name: "Outstanding"
            type: "number"
            description: "The total amount of outstanding sales invoices associated with the contact."

          - name: "Overdue"
            type: "number"
            description: "The total amount of overdue sales invoices associated with the contact."

      - name: "AccountsPayable"
        type: "object"
        description: "Details about the outstanding and/or overdue bills associated with the contact, not converted to base currency."
        subattributes:
          - name: "Outstanding"
            type: "number"
            description: "The total amount of outstanding bills associated with the contact."

          - name: "Overdue"
            type: "number"
            description: "The total amount of overdue bills associated with the contact."

  - name: "HasAttachments"
    type: "boolean"
    description: "If `true`, the contact has an attachment."

  - name: "HasValidationErrors"
    type: "array"
    description: "Details about any validation errors associated with the contact."
    subattributes:
      - name: "Message"
        type: "string"
        description: "The validation error message."
---