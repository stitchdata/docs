---
tap: "pepperjam"
version: "1"
key: "group"

name: "group"
doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#Group"
singer-schema: "https://github.com/singer-io/tap-pepperjam/blob/master/tap_pepperjam/schemas/group.json"
description: |
  The `{{ table.name }}` table contains information about groups in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "getGroup"
  doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#Group"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The group ID."
    foreign-key-id: "group-id"

  - name: "assigned_publishers"
    type: "integer"
    description: ""
  - name: "name"
    type: "string"
    description: ""
---
