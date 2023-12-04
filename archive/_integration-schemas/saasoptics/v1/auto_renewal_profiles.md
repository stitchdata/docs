---
tap: "saasoptics"
version: "1"
key: "auto-renewal-profile"

name: "auto_renewal_profiles"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-saasoptics/blob/master/tap_saasoptics/schemas/auto_renewal_profiles.json"
description: |
  The `{{ table.name }}` table contains info about auto-renwal profiles, or transaction renewal rules in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "Auto-Renewal Profiles List"
  doc-link: "https://saasoptics.zendesk.com/hc/en-us/articles/115013918268-Auto-Renewal-Profiles-R-"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "auto-renewal-profile-id"

  - name: "days"
    type: "integer"
    description: ""

  - name: "generate_revenue"
    type: "boolean"
    description: ""

  - name: "months"
    type: "integer"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "recognize"
    type: "boolean"
    description: ""
---