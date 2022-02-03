---
tap: "hubspot"
version: "2"
key: "contact-by-company"

name: "contacts_by_company"
singer-schema: https://github.com/singer-io/tap-hubspot/blob/master/tap_hubspot/schemas/contacts_by_company.json
description: |
  The `{{ table.name }}` table contains contact and company ID pairs, allowing you to join contacts to relevant company data.

  To replicate data from this table, you must also select the parent `companies` table.

replication-method: "Full Table"

attributes:
  - name: "contact-id"
    type: "integer"
    primary-key: true
    description: "The ID of the contact."
    foreign-key-id: "contact-id"

  - name: "company-id"
    type: "integer"
    primary-key: true
    description: "The ID of the company the contact is a part of."
    foreign-key-id: "company-id"
---
