---
tap: "sailthru"
version: "1"
key: ""

name: "users"
doc-link: "https://getstarted.sailthru.com/developers/api/user/"
singer-schema: "https://github.com/singer-io/tap-sailthru/blob/master/tap_sailthru/schemas/users.json"
description: |
  The `{{ table.name }}` table contains user data from your {{ integration.display_name }} account. This is a child table of `blast_save_list`.

replication-method: "Full Table"

api-method:
    name: "get Users"
    doc-link: "https://getstarted.sailthru.com/developers/api/user/"

attributes:
  - name: "profile_id"
    type: "string"
    primary-key: true
    description: "The profile ID."
    #foreign-key-id: "profile-id"

  - name: "cookie"
    type: "string"
    description: ""
  - name: "email"
    type: "string"
    description: ""
  - name: "engagement"
    type: "string"
    description: ""
  - name: "lists"
    type: "array"
    description: "Information about lists."
    subattributes:
      - name: "value"
        type: "string"
        description: "The list ID."
        foreign-key-id: "list-id"
  - name: "optout_email"
    type: "string"
    description: ""
  
  - name: "vars"
    type: "string"
    description: ""
---
