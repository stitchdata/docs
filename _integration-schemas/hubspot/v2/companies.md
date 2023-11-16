---
tap: "hubspot"
version: "2"
key: "company"

name: "companies"
doc-link: http://developers.hubspot.com/docs/methods/companies/get_company
singer-schema: https://github.com/singer-io/tap-hubspot/blob/master/tap_hubspot/schemas/companies.json
description: |
  The `{{ table.name }}` table contains info about the companies your {{ integration.display_name }} contacts belong to.

replication-method: "Key-based Incremental"

replication-key:
  name: "property_hs_lastmodifieddate"

api-method:
  name: "Get a company"
  doc-link: https://developers.hubspot.com/docs/methods/companies/get_company

attributes:
  - name: "companyId"
    type: "integer"
    primary-key: true
    description: "The ID of the company."
    foreign-key-id: "company-id"

  - name: "portalId"
    type: "integer"
    description: "The ID of the portal the company is associated with."
    foreign-key-id: "portal-id"

  - name: "isDeleted"
    type: "boolean"
    description: "If `true`, the company has been deleted."

  - name: "properties"
    type: "object"
    description: "Details about the company."
    subattributes:
      - name: "description"
        type: "string"
        description: "The description of the company."

      - name: "name"
        type: "string"
        description: "The name of the company."

      - name: "createdate"
        type: "date-time"
        description: "The time the company was created."
---