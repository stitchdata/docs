---
tap: "snapchat-ads"
version: "1"
key: ""

name: "members"
doc-link: https://developers.snapchat.com/api/docs/?python#get-all-members-of-an-organization
singer-schema: https://github.com/singer-io/tap-snapchat-ads/tree/master/tap_snapchat_ads/schemas/members.json
description: "This stream retrieves the information of all Members of an Organization"

replication-method: "Key-based Incremental"

table-key-properties: "id"
valid-replication-keys: "updated_at"

attributes:
  - name: "id"
    primary-key: true
    type: "string"
    description: "Member's Id"

  - name: "updated_at"
    type: "date-time"
    description: "Latest Date and time at which member details were updated"
    replication-key: true

  - name: "created_at"
    type: "date-time"
    description: "Date and Time at which the member was created"

  - name: "email"
    type: "string"
    description: "Member's EmailId"

  - name: "organization_id"
    type: "string"
    description: "Id of the organization to which the members belongs to"

  - name: "display_name"
    type: "string"
    description: "DIsplay name of the member"

  - name: "member_status"
    type: "string"
    description: "Name of the Advertiser. Example: INVITED, MEMBER"
---