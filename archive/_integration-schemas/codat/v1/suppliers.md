---
tap: "codat"
version: "1"
key: "supplier"

name: "suppliers"
doc-link: "https://docs.codat.io/docs/suppliers-2"
singer-schema: "https://github.com/singer-io/tap-codat/blob/master/tap_codat/schemas/suppliers.json"
description: |
  The `{{ table.name }}` table contains info about the suppliers in your {{ integration.display_name }} instance. A supplier is a person or organization that provides a product or service.

replication-method: "Key-based Incremental"

replication-key:
  name: "modifiedDate"

api-method:
  name: "Get suppliers for a company"
  doc-link: "https://docs.codat.io/reference/suppliers#suppliers_listpaged"

attributes:
  - name: "companyId"
    type: "string"
    primary-key: true
    description: "The company ID."
    foreign-key-id: "company-id"

  - name: "id"
    type: "string"
    primary-key: true
    description: "The supplier ID."
    foreign-key-id: "supplier"

  - name: "addresses"
    type: "array"
    description: "A list of addresses associated with the supplier."
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

  - name: "contactName"
    type: "string"
    description: "The name of the main contact for the supplier."

  - name: "emailAddress"
    type: "string"
    description: " The supplier's email address."

  - name: "phone"
    type: "string"
    description: "The supplier's phone number."

  - name: "registrationNumber"
    type: "string"
    description: "The company number of the supplier."

  - name: "status"
    type: "string"
    description: |
      The status of the supplier. Possible values are:

      - `Unknown`
      - `Active`
      - `Archived`

  - name: "supplierName"
    type: "string"
    description: "The name of the supplier as recorded in the accounting system."

  - name: "taxNumber"
    type: "string"
    description: "The supplier's company tax number."
---