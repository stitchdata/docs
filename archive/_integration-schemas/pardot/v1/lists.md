---
tap: "pardot"
version: "1"
key: "list"

name: "lists"
doc-link: "http://developer.pardot.com/kb/object-field-references/#list"
singer-schema: "https://github.com/singer-io/tap-pardot/blob/master/tap_pardot/schemas/lists.json"
description: |
  The `{{ table.name }}` table contains info about the lists in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Query lists"
  doc-link: "http://developer.pardot.com/kb/api-version-3/lists/"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The list ID."
    foreign-key-id: "list-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The last time the list was updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the list was created."

  - name: "description"
    type: "string"
    description: "The description of the list."

  - name: "is_crm_visible"
    type: "boolean"
    description: "If `true`, the list will be visible in a CRM."

  - name: "is_dynamic"
    type: "boolean"
    description: "If `true`, the list has prospects dynamically added to it via a set of chosen rules."

  - name: "is_public"
    type: "boolean"
    description: "If `true`, the list will show on EPC pages to prospects."

  - name: "name"
    type: "string"
    description: "The name of the list."

  - name: "title"
    type: "string"
    description: "The title of the list, as it displays to subscribers."
---