---
tap: "quickbooks"
version: "2"
key: "vendor"

name: "vendors"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/vendor"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/vendors.json"
description: |
  The `{{ table.name }}` table contains info about the sellers your company purchases products from. **Note**: Both active and inactive vendors are included in the data for this table.

replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Query a vendor"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/vendor#query-a-vendor"

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The vendor ID."
    foreign-key-id: "vendor-id"

  - name: "AcctNum"
    type: "string"
    description: ""

  - name: "Active"
    type: "boolean"
    description: ""

  - name: "AlternatePhone"
    type: "object"
    description: ""
    subattributes:
      - name: "FreeFormNumber"
        type: "string"
        description: ""

  - name: "APAccountRef"
    type: "object"
    description: ""
    subattributes:
      - name: "name"
        type: "string"
        description: ""
        
      - name: "value"
        type: "string"
        description: ""

  - name: "Balance"
    type: "decimal"
    description: ""

  - name: "BillAddr"
    type: "object"
    description: ""
    subattributes:
      - name: "City"
        type: "string"
        description: ""

      - name: "Country"
        type: "string"
        description: ""

      - name: "CountrySubDivisionCode"
        type: "string"
        description: ""

      - name: "Id"
        type: "string"
        description: ""

      - name: "Lat"
        type: "string"
        description: ""

      - name: "Line1"
        type: "string"
        description: ""

      - name: "Long"
        type: "string"
        description: ""

      - name: "PostalCode"
        type: "string"
        description: ""

  - name: "BillRate"
    type: "decimal"
    description: ""

  - name: "BusinessNumber"
    type: "string"
    description: ""

  - name: "CompanyName"
    type: "string"
    description: ""

  - name: "CostRate"
    type: "decimal"
    description: ""

  - name: "CurrencyRef"
    type: "object"
    description: "Details about the currency used by the vendor."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: "The currency ID."
        foreign-key-id: "currency-id"

  - name: "DisplayName"
    type: "string"
    description: ""

  - name: "domain"
    type: "string"
    description: ""

  - name: "FamilyName"
    type: "string"
    description: ""

  - name: "Fax"
    type: "object"
    description: ""
    subattributes:
      - name: "FreeFormNumber"
        type: "string"
        description: ""

  - name: "GivenName"
    type: "string"
    description: ""

  - name: "GSTIN"
    type: "string"
    description: ""

  - name: "GSTRegistrationType"
    type: "string"
    description: ""

  - name: "HasTPAR"
    type: "string"
    description: ""

  - name: "MetaData"
    type: "object"
    description: ""
    subattributes:
      - name: "CreateTime"
        type: "date-time"
        description: ""

      - name: "LastUpdatedTime"
        type: "date-time"
        description: ""

  - name: "MiddleName"
    type: "string"
    description: ""

  - name: "Mobile"
    type: "object"
    description: ""
    subattributes:
      - name: "FreeFormNumber"
        type: "string"
        description: ""

  - name: "OthercontactInfo"
    type: "object"
    description: ""
    subattributes:
      - name: "Type"
        type: "string"
        description: ""

      - name: "Telephone"
        type: "string"
        description: ""

  - name: "PrimaryEmailAddr"
    type: "object"
    description: ""
    subattributes:
      - name: "Address"
        type: "string"
        description: ""

  - name: "PrimaryPhone"
    type: "object"
    description: ""
    subattributes:
      - name: "FreeFormNumber"
        type: "string"
        description: ""

  - name: "PrintOnCheckName"
    type: "string"
    description: ""

  - name: "Source"
    type: "string"
    description: ""

  - name: "Suffix"
    type: "string"
    description: ""

  - name: "SyncToken"
    type: "string"
    description: ""

  - name: "T4Eligible"
    type: "boolean"
    description: ""

  - name: "T5018Eligible"
    type: "boolean"
    description: ""

  - name: "TaxIdentifier"
    type: "string"
    description: ""

  - name: "TaxReportingBasis"
    type: "string"
    description: ""

  - name: "TermRef"
    type: "object"
    description: "Details about the sales term associated with the vendor."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: "The term ID."
        foreign-key-id: "term-id"

  - name: "Title"
    type: "string"
    description: ""

  - name: "Vendor1099"
    type: "boolean"
    description: ""

  - name: "VendorPaymentBankDetail"
    type: "object"
    description: ""
    subattributes:
      - name: "BankAccountName"
        type: "string"
        description: ""
        
      - name: "BankAccountNumber"
        type: "string"
        description: ""
        
      - name: "BankBranchIdentifier"
        type: "string"
        description: ""
        
      - name: "StatementText"
        type: "string"
        description: ""

  - name: "WebAddr"
    type: "object"
    description: ""
    subattributes:
      - name: "URI"
        type: "string"
        description: ""
---