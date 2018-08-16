---
tap: "hubspot"
version: "2.0"

name: "contacts_by_company"
doc-link: 
singer-schema: https://github.com/singer-io/tap-hubspot/blob/master/tap_hubspot/schemas/contacts_by_company.json
description: |
  The `{{ table.name }}` table contains contact and company ID pairs, allowing you to join contacts to relevant company data.

replication-method: "Full Table"
api-method:
  name: 
  doc-link: 

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
