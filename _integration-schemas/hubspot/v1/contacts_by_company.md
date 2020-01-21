---
tap: "hubspot"
version: "1"

name: "hubspot_contacts_by_company"
doc-link: 
singer-schema: https://github.com/singer-io/tap-hubspot/blob/master/tap_hubspot/schemas/hubspot_contacts_by_company.json
description: |
  The `hubspot_contacts_by_company` table contains contact and company ID pairs, allowing you to join contacts to relevant company data.

  **Note:** to sync this table, you must set the [`companies`](#companies) table to sync. This table will then be automatically synced and created in your data warehouse. **It will not display in the Stitch app.**

notes: 

replication-method: "Full Table"
api-method:
  name: 
  doc-link: 

attributes:
## Primary Key
  - name: "contact-id"
    type: "integer"
    primary-key: true
    description: "The ID of the contact."

## Primary Key
  - name: "company-id"
    type: "integer"
    primary-key: true
    description: "The ID of the company the contact is a part of."
---