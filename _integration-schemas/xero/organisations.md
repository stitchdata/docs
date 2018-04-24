---
tap: "xero"
version: "1.0"

name: "organisations"
doc-link: &api-doc https://developer.xero.com/documentation/api/organisation
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/organisations.json
description: |
  The `organisations` table contains info about the organisations in your Xero account.

replication-method: "Full Table"

api-method:
  name: getOrganisation
  doc-link: *api-doc

attributes:
  - name: "OrganisationID"
    type: "string"
    primary-key: true
    description: "The organisation ID."

  - name: "APIKey"
    type: "string"
    description: "The organisation's unique key for [Xero-to-Xero transactions](http://help.xero.com/#X2XSendKey)."

  - name: "Name"
    type: "string"
    description: "The display name of the organisation in Xero."

  - name: "LegalName"
    type: "string"
    description: "The legal name of the organisation, as shown in reports."

  - name: "PaysTax"
    type: "boolean"
    description: "If `true`, the organisation is registered with a local tax authority."

  - name: "Version"
    type: "string"
    description: "The version of the organisation. Refer to [Xero's documentation](https://developer.xero.com/documentation/api/types#version) for possible versions."
    doc-link: https://developer.xero.com/documentation/api/types#version

  - name: "OrganisationType"
    type: "string"
    description: |
      The type of the organisation. Possible values are:

      - `COMPANY`
      - `CHARITY`
      - `CLUBSOCIETY`
      - `PARTNERSHIP`
      - `PRACTICE`
      - `PERSON`
      - `SOLETRADER`
      - `TRUST`

  - name: "BaseCurrency"
    type: "string"
    description: "The default currency (ISO 4217) of the organisation. Refer to [XE.com](http://www.xe.com/iso4217.php) for a list currency codes."
    doc-link: http://www.xe.com/iso4217.php

  - name: "CountryCode"
    type: "string"
    description: "The country code (ISO 3166-2 of the organisation. Refer to [XE.com](http://countrycode.org/) for a list currency codes."

  - name: "IsDemoCompany"
    type: "boolean"
    description: "If `true`, the organisation is a demo company."

  - name: "OrganisationStatus"
    type: "string"
    description: "This value will be `ACTIVE` if you can connect to the organisation via the Xero API."

  - name: "RegistrationNumber"
    type: "string"
    description: "**Only applicable to New Zealand, Australian, and UK organisations.** The registration number of the organisation."

  - name: "TaxNumber"
    type: "string"
    description: |
      The organisation's tax number. Depending on the version of Xero you're using, this could be one of the following in the Xero UI:

      - Australia - ABN
      - New Zealand - GST Number
      - UK - VAT Number
      - US and global - Tax ID Number

  - name: "FinancialYearEndDay"
    type: "integer"
    description: "The calendar day that the organisation's financial year end occurs. Possible values are `0-31`."

  - name: "FinancialYearEndMonth"
    type: "integer"
    description: "The calendar month that the organisation's financial year end occurs. Possible values are `1-12`."

  - name: "SalesTaxBasis"
    type: "string"
    description: "The accounting basis used for tax returns. Refer to [Xero's documentation](https://developer.xero.com/documentation/api/types#SalesTaxBasis) for a list of possible values."
    doc-link: https://developer.xero.com/documentation/api/types#SalesTaxBasis

  - name: "SalesTaxPeriod"
    type: "string"
    description: "The frequency with which tax returns are processed. Refer to [Xero's documentation](https://developer.xero.com/documentation/api/types#SalesTaxPeriod) for a list of possible values."
    doc-link: https://developer.xero.com/documentation/api/types#SalesTaxPeriod

  - name: "DefaultSalesTax"
    type: "string"
    description: "The default "

  - name: "DefaultPurchaseTax"
    type: "string"
    description: ""

  - name: "PeriodLockDate"
    type: "date-time"
    description: "The period lock date for the organisation, if set."
    doc-link: https://help.xero.com/Settings_LockDate

  - name: "EndOfYearLockDate"
    type: "date-time"
    description: "The year end lock date for the organisation, if set."
    doc-link: https://help.xero.com/Settings_LockDate

  - name: "CreatedDateUTC"
    type: "date-time"
    description: "The date the organisation was created, in UTC."

  - name: "Timezone"
    type: "string"
    description: "The timezone the organisation is in. Refer to [Xero's documenation](https://github.com/XeroAPI/XeroAPI-Schemas/blob/master/src/main/resources/XeroSchemas/v2.00/Timezone.xsd) for a list of possible timezone values."
    doc-link: https://github.com/XeroAPI/XeroAPI-Schemas/blob/master/src/main/resources/XeroSchemas/v2.00/Timezone.xsd

  - name: "OrganisationEntityType"
    type: "string"
    description: |
      The entity type of the organisation. Possible values are:

      - `COMPANY`
      - `CHARITY`
      - `CLUBSOCIETY`
      - `PARTNERSHIP`
      - `PRACTICE`
      - `PERSON`
      - `SOLETRADER`
      - `TRUST`

  - name: "ShortCode"
    type: "string"
    description: "A unique ID for the organisation."

  - name: "LineOfBusiness"
    type: "string"
    description: "The description of the business, as defined in the [organisation's settings](https://go.xero.com/Settings/Organisation)."

  - name: "Addresses"
    type: "array"
    description: ""
    array-attributes:

  - name: "Phones"
    type: "array"
    description: ""
    array-attributes:

  - name: "ExternalLinks"
    type: "array"
    description: "Details about profile links for the organisation, such as Facebook, Twitter, LinkedIn, etc. These are set in the [organisation's settings](https://go.xero.com/Settings/Organisation)."
    array-attributes:
      - name: "LinkType"
        type: "string"
        description: |
          The external link type. Possible values are:

          - `Facebook`
          - `GooglePlus`
          - `LinkedIn`
          - `Twitter`
          - `Website`

      - name: "Url"
        type: "string"
        description: "The URL for the service."

  - name: "PaymentTerms"
    type: 
    description: ""

---