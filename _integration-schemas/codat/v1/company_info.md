---
tap: "codat"
version: "1.0"
key: "company-info"

name: "company_info"
doc-link: "https://docs.codat.io/reference/info"
singer-schema: "https://github.com/singer-io/tap-codat/blob/master/tap_codat/schemas/company_info.json"
description: |
  The `{{ table.name }}` table contains company info. In {{ integration.display_name }}, company info includes information about a linked company such as address, phone number and company registration.

replication-method: "Full Table"

api-method:
    name: "List basic info for a company"
    doc-link: "https://docs.codat.io/reference/info#info_list"

attributes:
  - name: "companyId"
    type: "string"
    primary-key: true
    description: "The company ID."
    foreign-key-id: "company-id"

  - name: "accountingPlatformRef"
    type: "string"
    description: "A company reference as provided by some accounting platforms."

  - name: "addresses"
    type: "array"
    description: "A list of addresses associated with the company."
    subattributes:
      - name: "city"
        type: "string"
        description: "The city."

      - name: "country"
        type: "string"
        description: "The country."

      - name: "line1"
        type: "string"
        description: "The first address line."

      - name: "line2"
        type: "string"
        description: "The second address line."

      - name: "postalCode"
        type: "string"
        description: "The zip or postal code."

      - name: "region"
        type: "string"
        description: "The region."

      - name: "type"
        type: "string"
        description: |
          The type of the address. Possible values are:

          - `Billing`
          - `Delivery`
          - `Unknown`

  - name: "baseCurrency"
    type: "string"
    description: "The currency set in the linked company's accounting platform."

  - name: "companyLegalName"
    type: "string"
    description: "The legal registered name of the linked company."

  - name: "companyName"
    type: "string"
    description: "The name of the linked company."

  - name: "createdDate"
    type: "string"
    description: "The date the linked company was created in the accounting platform."

  - name: "financialYearStartDate"
    type: "date-time"
    description: "The date for the start of the company's financial year."

  - name: "phoneNumbers"
    type: "array"
    description: "A list of phone numbers associated with the linked company."
    subattributes:
      - name: "number"
        type: "string"
        description: "The phone number."

      - name: "type"
        type: "string"
        description: |
          The type of phone number. Possible values are:

          - `Primary`
          - `Landline`
          - `Mobile`
          - `Fax`
          - `Unknown`

  - name: "registrationNumber"
    type: "string"
    description: "The registration number given to the linked company by the companies authority in the country of origin."

  - name: "taxNumber"
    type: "string"
    description: "The company tax number."

  - name: "webLinks"
    type: "array"
    description: "A list of web links associated with the company."
    subattributes:
      - name: "type"
        type: "string"
        description: |
          The type of web link. Possible values are:

          - `Website`
          - `Social`
          - `Unknown`

      - name: "url"
        type: "string"
        description: "The URL of the web link."
---