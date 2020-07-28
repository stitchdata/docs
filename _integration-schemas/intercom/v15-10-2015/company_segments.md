---
tap: "intercom"
# version: "15-10-2015"

name: "company_segments"
doc-link: https://developers.intercom.io/docs/companies
description: |
  The `{{ table.name }}` table contains info about company segments. A segment is a group of users that are defined by a set of rules.

replication-method: "Full Table"
api-method:
  name: listSegments
  doc-link: https://developers.intercom.io/docs/list-segments

attribution-window: true

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The segment ID."
    foreign-key-id: "company-segment-id"

  - name: "updated_at"
    type: "date-time"
    description: "The time the segment was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the segment was created."

  - name: "name"
    type: "string"
    description: "The name of the segment."

  - name: "person_type"
    type: "string"
    description: "The type of record. This will either be `user` or `lead`."

  - name: "type"
    type: "string"
    description: "The value of this field will be `segment`."
---