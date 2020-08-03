---
tap: "codat"
version: "1"
key: "company"

name: "companies"
doc-link: "https://docs.codat.io/reference/companies"
singer-schema: "https://github.com/singer-io/tap-codat/blob/master/tap_codat/schemas/companies.json"
description: |
  The `{{ table.name }}` table contains info about the companies in your {{ integration.display_name }} instance. A company represents a business who can share the connection to their financial data sources.

replication-method: "Full Table"

api-method:
  name: "List companies"
  doc-link: "https://docs.codat.io/reference/companies#companies_listpaged"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The company ID."
    foreign-key-id: "company-id"

  - name: "lastSync"
    type: "date-time"
    description: ""

  - name: "name"
    type: "string"
    description: "The name of the company."

  - name: "platform"
    type: "string"
    description: ""

  - name: "redirect"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""
---