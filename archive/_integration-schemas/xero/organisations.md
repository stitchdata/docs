---
tap: "xero"
version: "1"

name: "organisations"
doc-link: &api-doc https://developer.xero.com/documentation/api/organisation
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/organisations.json
description: |
  The `{{ table.name }}` table contains info about the organisations in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: getOrganisation
  doc-link: *api-doc

attributes:
  - name: "OrganisationID"
    type: "string"
    primary-key: true
    description: "The organisation ID."
   #foreign-key-id: "organisation-id"

  - name: "APIKey"
    type: "string"
    description: |
      The organisation's unique key for [{{ integration.display_name }}-to-{{ integration.display_name }} transactions](http://help.xero.com/#X2XSendKey){:target="new"}.

  - name: "Name"
    type: "string"
    description: "The display name of the organisation in {{ integration.display_name }}."

  - name: "LegalName"
    type: "string"
    description: "The legal name of the organisation, as shown in reports."

  - name: "PaysTax"
    type: "boolean"
    description: "If `true`, the organisation is registered with a local tax authority."

  - name: "Version"
    type: "string"
    description: |
      The version of the organisation. Refer to [{{ integration.display_name }}'s documentation](https://developer.xero.com/documentation/api/types#version){:target="new"} for possible versions.
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
    description: |
      The country code (ISO 3166-2 of the organisation. Refer to [XE.com](http://countrycode.org/){:target="new"} for a list currency codes.

  - name: "IsDemoCompany"
    type: "boolean"
    description: "If `true`, the organisation is a demo company."

  - name: "OrganisationStatus"
    type: "string"
    description: "This value will be `ACTIVE` if you can connect to the organisation via the {{ integration.display_name }} API."

  - name: "RegistrationNumber"
    type: "string"
    description: "**Only applicable to New Zealand, Australian, and UK organisations.** The registration number of the organisation."

  - name: "TaxNumber"
    type: "string"
    description: |
      The organisation's tax number. Depending on the version of {{ integration.display_name }} you're using, this could be one of the following in the {{ integration.display_name }} UI:

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
    description: |
      The accounting basis used for tax returns. Refer to [{{ integration.display_name }}'s documentation](https://developer.xero.com/documentation/api/types#SalesTaxBasis){:target="new"} for a list of possible values.
    doc-link: https://developer.xero.com/documentation/api/types#SalesTaxBasis

  - name: "SalesTaxPeriod"
    type: "string"
    description: |
      The frequency with which tax returns are processed. Refer to [{{ integration.display_name }}'s documentation](https://developer.xero.com/documentation/api/types#SalesTaxPeriod){:target="new"} for a list of possible values.
    doc-link: https://developer.xero.com/documentation/api/types#SalesTaxPeriod

  - name: "DefaultSalesTax"
    type: "string"
    description: "The default tax used for line amounts on sales transactions."

  - name: "DefaultPurchaseTax"
    type: "string"
    description: "The default tax used for line amounts on purchase transactions."

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
    description: |
      The timezone the organisation is in. Refer to [{{ integration.display_name }}'s documenation](https://github.com/XeroAPI/XeroAPI-Schemas/blob/master/src/main/resources/XeroSchemas/v2.00/Timezone.xsd){:target="new"} for a list of possible timezone values.
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
    description: |
      The description of the business, as defined in the [organisation's settings](https://go.xero.com/Settings/Organisation){:target="new"}.

  - name: "Addresses"
    type: "array"
    description: "Details about the addresses associated with the organisation."
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
    description: "Details about the phone numbers associated with the organisation."
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

  - name: "ExternalLinks"
    type: "array"
    description: |
      Details about profile links for the organisation, such as Facebook, Twitter, LinkedIn, etc. These are set in the [organisation's settings](https://go.xero.com/Settings/Organisation){:target="new"}.
    subattributes:
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
    type: "array"
    description: "Details about the default payment terms for the organisation."
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
---