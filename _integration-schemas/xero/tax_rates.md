---
tap: "xero"
version: "1.0"

name: "tax_rates"
doc-link: &api-doc https://developer.xero.com/documentation/api/tax-rates
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/tax_rates.json
description: |
  The `{{ table.name }}` table contains info about the tax rates set up in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: getTaxRates
  doc-link: *api-doc

attributes:
  - name: "Name"
    type: "string"
    primary-key: true
    description: "The name of the tax rate."
    foreign-key-id: "tax-name"

  - name: "TaxType"
    type: "string"
    description: "The tax type of the tax rate. Refer to [{{ integration.display_name }}'s documentation](https://developer.xero.com/documentation/api/types#TaxTypes) for a list of possible values."
    doc-link: https://developer.xero.com/documentation/api/types#TaxTypes

  - name: "TaxComponents"
    type: "array"
    description: "Details about the components that make up the tax rate."
    subattributes:
      - name: "Name"
        type: "string"
        description: "The name of the tax component."

      - name: "IsCompound"
        type: "boolean"
        description: "If `true`, the tax rate is compounded. Refer to [{{ integration.display_name }}'s documentation](https://help.xero.com/Tax-SetDefaults) for more info."

      - name: "IsNonRecoverable"
        type: "boolean"
        description: "If `true`, the tax rate is non-recoverable. Non-recoverable tax rates are only applicable to [Canadian organisations](http://help.xero.com/#Settings_TaxRates)."

      - name: "Rate"
        type: "number"
        description: "The tax rate."

  - name: "Status"
    type: "string"
    description: |
      The status of the tax rate. Possible values are:

      - `ACTIVE` - The tax rate is active and can be used in transactions.
      - `DELETED` - The tax rate is deleted and cannot be restored or used on transactions.
      - `ARCHIVED` - The tax rate has been used on a transaction, but has since been deleted. `ARCHIVED` tax rates cannot be restored or used in transactions.

  - name: "ReportTaxType"
    type: "string"
    description: "The report tax type. Refer to [{{ integration.display_name }}'s documentation](https://developer.xero.com/documentation/api/types#ReportTaxTypes) for a list of possible values."
    doc-link: https://developer.xero.com/documentation/api/types#ReportTaxTypes

  - name: "CanApplyToAssets"
    type: "boolean"
    description: "If `true`, the tax rate can be used for asset accounts."

  - name: "CanApplyToEquity"
    type: "boolean"
    description: "If `true`, the tax rate can be used for equity accounts."

  - name: "CanApplyToExpenses"
    type: "boolean"
    description: "If `true`, the tax rate can be used for expense accounts."

  - name: "CanApplyToLiabilities"
    type: "boolean"
    description: "If `true`, the tax rate can be used for liability accounts."

  - name: "CanApplyToRevenue"
    type: "boolean"
    description: "If `true`, the tax rate can be used for revenue accounts."

  - name: "DisplayTaxRate"
    type: "number"
    description: "The tax rate in decimal format. For example: `12.5000`"

  - name: "EffectiveRate"
    type: "number"
    description: "The effective tax rate."
---