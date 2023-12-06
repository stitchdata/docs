---
tap: "pardot"
version: "1"
key: "list-membership"

name: "list_memberships"
doc-link: "http://developer.pardot.com/kb/object-field-references/#list-membership"
singer-schema: "https://github.com/singer-io/tap-pardot/blob/master/tap_pardot/schemas/list_memberships.json"
description: |
  The `{{ table.name }}` table contains info about list memberships.

  **Note**: To replicate this table, the [`lists`](#lists) table must also be set to replicate.

replication-method: "Key-based Incremental"

api-method:
  name: "Query list memberships"
  doc-link: "http://developer.pardot.com/kb/api-version-3/list-memberships/"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    replication-key: true
    description: "The list membership ID."
    foreign-key-id: "list-membership-id"

  - name: "list_id"
    type: "integer"
    replication-key: true
    description: "The ID of the list associated with this membership."
    foreign-key-id: "list-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the membership was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the membership was created in {{ integration.display_name }}."

  - name: "opted_out"
    type: "integer"
    description: "If `1`, the prospect has unsubscribed from receiving emails from this list."

  - name: "prospect_id"
    type: "integer"
    description: "The ID of the prospect associated with the membership."
    foreign-key-id: "prospect-id"
---