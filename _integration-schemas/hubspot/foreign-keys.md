---
tap-reference: "hubspot"

version: "2.0"

foreign-keys:
  - attribute: "form-id"
    table: "forms"
    join-on: "guid"

  - attribute: "static-list-id"
    table: "contact_lists"
    join-on: "listId"

  - attribute: "contact-id"
    table: "contacts"
    join-on: "contactId"

  - attribute: "company-id"
    table: "companies"
    join-on: "companyId"

  - attribute: ""
    table: "deals"
    join-on: "dealId"

  - attribute: "leadNurturingCampaignId"
    table: "campaigns"
    join-on: "campaignId"

  - attribute: "ownerId"
    table: "owners"
    join-on: "ownerId"
---