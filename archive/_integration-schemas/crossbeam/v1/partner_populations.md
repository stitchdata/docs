---
tap: "crossbeam"
version: "1"
key: ""

name: "partner_populations"
doc-link: "https://developers.crossbeam.com/#53c31e87-71ed-4712-85b5-65877d0c0a0f"
singer-schema: "https://github.com/singer-io/tap-crossbeam/blob/master/tap_crossbeam/schemas/partner_populations.json"
description: |
  The `{{ table.name }}` table contains information about the populations that your partners have shared with you in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
    name: "get Partner"
    doc-link: "https://developers.crossbeam.com/#53c31e87-71ed-4712-85b5-65877d0c0a0f"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The partner population ID."
    
  - name: "name"
    type: "string"
    description: ""
  - name: "organization_id"
    type: "integer"
    description: ""
  - name: "population_type"
    type: "string"
    description: ""
---
