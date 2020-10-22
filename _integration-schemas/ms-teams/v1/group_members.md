---
tap: "ms-teams"
version: "1"
key: ""

name: "group_members"
doc-link: "https://docs.microsoft.com/en-us/graph/api/group-list-members?view=graph-rest-1.0&tabs=http"
singer-schema: "https://github.com/singer-io/tap-ms-teams/blob/master/tap_ms_teams/schemas/group_members.json"
description: |
  The `{{ table.name }}` table contains information about group members in your Microsoft account. Members can be users, organizational contacts, devices, service principals, and other groups.

replication-method: "Full Table"

api-method:
    name: "List members"
    doc-link: "https://docs.microsoft.com/en-us/graph/api/group-list-members?view=graph-rest-1.0&tabs=http"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The member ID."
    #foreign-key-id: "member-id"
    
  - name: "business_phones"
    type: "null"
    description: ""
  - name: "display_name"
    type: "string"
    description: ""
  - name: "given_name"
    type: "string"
    description: ""
  
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
