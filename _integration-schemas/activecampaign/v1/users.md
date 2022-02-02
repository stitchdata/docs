---
tap: "activecampaign"
version: "1"
key: ""

name: "users"
doc-link: "https://developers.activecampaign.com/reference#users"
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/users.json"
description: |
  The `{{ table.name }}` table contains information about users who can login to your {{ integration.display_name }} account.
  
replication-method: "Full Table"

api-method:
    name: "List all users"
    doc-link: "https://developers.activecampaign.com/reference#list-all-users"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The user ID."
    foreign-key-id: "user-id"

  - name: "cdate"
    type: "date-time"
    description: ""
  - name: "email"
    type: "string"
    description: ""
  - name: "first_name"
    type: "string"
    description: ""
  
  - name: "last_name"
    type: "string"
    description: ""
  - name: "local_zone_id"
    type: "string"
    description: ""
  - name: "mfa_enabled"
    type: "integer"
    description: ""
  - name: "password_updated_utc_timestamp"
    type: "date-time"
    description: ""
  - name: "phone"
    type: "string"
    description: ""
  - name: "signature"
    type: "string"
    description: ""
  - name: "udate"
    type: "date-time"
    description: ""
  - name: "username"
    type: "string"
    description: ""
---
