---
tap: "quickbooks"
version: "2"
key: "customer"

name: "customers"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/customer"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/customers.json"
description: |
  The `{{ table.name }}` table contains info about the consumers of your business's goods and services. **Note**: Both active and inactive customers are included in the data for this table.

replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Query a customer"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/customer#query-a-customer"

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The customer ID."
    foreign-key-id: "customer-id"

  - name: "Active"
    type: "boolean"
    description: ""

  - name: "AlternatePhone"
    type: "object"
    description: ""
    subattributes: &freeform-number
      - name: "FreeFormNumber"
        type: "string"
        description: ""

  - name: "ARAccountRef"
    type: "object"
    description: ""
    subattributes: &name-value
     - name: "name"
       type: "string"
       description: ""
       
     - name: "value"
       type: "string"
       description: ""

  - name: "Balance"
    type: "decimal"
    description: ""

  - name: "BalanceWithJobs"
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

      - name: "Line2"
        type: "string"
        description: ""

      - name: "Line3"
        type: "string"
        description: ""

      - name: "Line4"
        type: "string"
        description: ""

      - name: "Line5"
        type: "string"
        description: ""

      - name: "Long"
        type: "string"
        description: ""

      - name: "PostalCode"
        type: "string"
        description: ""

  - name: "BillWithParent"
    type: "boolean"
    description: ""

  - name: "BusinessNumber"
    type: "string"
    description: ""

  - name: "CompanyName"
    type: "string"
    description: ""

  - name: "CurrencyRef"
    type: "object"
    description: "Details about the currency used by the customer."
    subattributes: *name-value

  - name: "CustomerTypeRef"
    type: "object"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "DefaultTaxCodeRef"
    type: "object"
    description: "Details about the default tax code used for the customer."
    subattributes: *name-value

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
    subattributes: *freeform-number

  - name: "FullyQualifiedName"
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

  - name: "Job"
    type: "boolean"
    description: ""

  - name: "IsProject"
    type: "boolean"
    description: ""

  - name: "Level"
    type: "integer"
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
    subattributes: *freeform-number

  - name: "Notes"
    type: "string"
    description: ""

  - name: "ParentRef"
    type: "object"
    description: "If the customer is a sub-customer, this will contain details about the parent-level customer."
    subattributes:
      - name: "value"
        type: "string"
        description: "The customer ID."
        foreign-key-id: "customer-id"

  - name: "PaymentMethodRef"
    type: "object"
    description: "Details about the payment method used for the customer."
    subattributes: *name-value

  - name: "PreferredDeliveryMethod"
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
    subattributes: *freeform-number

  - name: "PrimaryTaxIdentifier"
    type: "string"
    description: ""

  - name: "PrintOnCheckName"
    type: "string"
    description: ""

  - name: "ResaleNum"
    type: "string"
    description: ""

  - name: "SalesTermRef"
    type: "object"
    description: "Details about the sales term associated with the customer."
    subattributes: *name-value

  - name: "SecondaryTaxIdentifier"
    type: "string"
    description: ""

  - name: "ShipAddr"
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

  - name: "Source"
    type: "string"
    description: ""

  - name: "Suffix"
    type: "string"
    description: ""

  - name: "SyncToken"
    type: "string"
    description: ""

  - name: "Taxable"
    type: "boolean"
    description: ""

  - name: "TaxExemptionReasonId"
    type: "integer"
    description: ""

  - name: "Title"
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