---
tap: "ms-teams"
version: "1"
key: ""

name: "group_owners"
doc-link: "https://docs.microsoft.com/en-us/graph/api/group-list-owners?view=graph-rest-1.0&tabs=http"
singer-schema: "https://github.com/singer-io/tap-ms-teams/blob/master/tap_ms_teams/schemas/group_owners.json"
description: |
  The `{{ table.name }}` table contains information about groups' owners in your Microsoft account. The owners can be a set of users or service principals that have modifying priviligges. Groups created in Microsoft Exchange will not be available in this table.

replication-method: "Full Table"

api-method:
    name: "List owners"
    doc-link: "https://docs.microsoft.com/en-us/graph/api/group-list-owners?view=graph-rest-1.0&tabs=http"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The group owner ID."
    #foreign-key-id: "owner-id"

  - name: "business_phones"
    type: "null"
    description: ""
  - name: "display_name"
    type: "string"
    description: ""
  - name: "given_name"
    type: "string"
    description: ""
  - name: "group_id"
    type: "string"
    description: "The group ID."
    foreign-key-id: "group-id"

  - name: "job_title"
    type: "string"
    description: ""
  - name: "mail"
    type: "string"
    description: ""
  - name: "mobile_phone"
    type: "string"
    description: ""
  - name: "office_location"
    type: "string"
    description: ""
  - name: "preferred_language"
    type: "string"
    description: ""
  - name: "surname"
    type: "string"
    description: ""
  - name: "user_principal_name"
    type: "string"
    description: ""
---
