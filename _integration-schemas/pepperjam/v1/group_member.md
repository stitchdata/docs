---
tap: "pepperjam"
version: "1"
key: "group_member"

name: "group_member"
doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#Member"
singer-schema: "https://github.com/singer-io/tap-pepperjam/blob/master/tap_pepperjam/schemas/group_member.json"
description: |
  The `{{ table.name }}` table contains information about members within groups in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "getGroupMember"
  doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#Member"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The group member ID."
    #foreign-key-id: "member-id"

  - name: "default"
    type: "string"
    description: ""
  - name: "group_id"
    type: "integer"
    description: "" 
    foreign-key-id: "group-id"
  - name: "name"
    type: "string"
    description: ""
  - name: "product_count"
    type: "integer"
    description: ""
---