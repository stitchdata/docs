---
tap: "impact"
version: "1"
key: "company-information"

name: "company_information"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-impact/blob/master/tap_impact/schemas/company_information.json"
description: |
  The `{{ table.name }}` table contains details about companies.

replication-method: "Full Table"

api-method:
  name: "Get company info"
  doc-link: "https://developer.impact.com/default#operations-Company_Information-GetCompanyInfo"

attributes:
  - name: "company_name"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "company-info-id"

  - name: "billing_address"
    type: "object"
    description: ""
    subattributes:
      - name: "address_line1"
        type: "string"
        description: ""

      - name: "address_line2"
        type: "string"
        description: ""

      - name: "city"
        type: "string"
        description: ""

      - name: "country"
        type: "string"
        description: ""

      - name: "postal_code"
        type: "string"
        description: ""

      - name: "state"
        type: "string"
        description: ""

  - name: "commercial_contact"
    type: "object"
    description: ""
    subattributes:
      - name: "cell_phone_number"
        type: "string"
        description: ""

      - name: "cell_phone_number_country"
        type: "string"
        description: ""

      - name: "email"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "user_id"
        type: "integer"
        description: ""

      - name: "work_phone_number"
        type: "string"
        description: ""

      - name: "work_phone_number_country"
        type: "string"
        description: ""

  - name: "corporate_address"
    type: "object"
    description: ""
    subattributes:
      - name: "address_line1"
        type: "string"
        description: ""

      - name: "address_line2"
        type: "string"
        description: ""

      - name: "city"
        type: "string"
        description: ""

      - name: "country"
        type: "string"
        description: ""

      - name: "postal_code"
        type: "string"
        description: ""

      - name: "state"
        type: "string"
        description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "ein_ssn_foreign_tax_id"
    type: "string"
    description: ""

  - name: "financial_contact"
    type: "object"
    description: ""
    subattributes:
      - name: "cell_phone_number"
        type: "string"
        description: ""

      - name: "cell_phone_number_country"
        type: "string"
        description: ""

      - name: "email"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "user_id"
        type: "integer"
        description: ""

      - name: "work_phone_number"
        type: "string"
        description: ""

      - name: "work_phone_number_country"
        type: "string"
        description: ""

  - name: "indirect_tax_number"
    type: "string"
    description: ""

  - name: "industry"
    type: "object"
    description: ""
    subattributes:
      - name: "industry_id"
        type: "integer"
        description: ""

      - name: "industry_name"
        type: "string"
        description: ""

  - name: "minimum_contact_rating"
    type: "integer"
    description: ""

  - name: "organization_type"
    type: "string"
    description: ""

  - name: "primary_phone_number"
    type: "string"
    description: ""

  - name: "primary_phone_number_country"
    type: "string"
    description: ""

  - name: "registered_for_indirect_tax"
    type: "boolean"
    description: ""

  - name: "secondary_phone_number"
    type: "string"
    description: ""

  - name: "secondary_phone_number_country"
    type: "string"
    description: ""

  - name: "technical_contact"
    type: "object"
    description: ""
    subattributes:
      - name: "cell_phone_number"
        type: "string"
        description: ""

      - name: "cell_phone_number_country"
        type: "string"
        description: ""

      - name: "email"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "user_id"
        type: "integer"
        description: ""

      - name: "work_phone_number"
        type: "string"
        description: ""

      - name: "work_phone_number_country"
        type: "string"
        description: ""

  - name: "timezone"
    type: "string"
    description: ""

  - name: "uri"
    type: "string"
    description: ""

  - name: "website"
    type: "string"
    description: ""
---