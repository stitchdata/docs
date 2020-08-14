---
tap: "intercom"
version: "02-02-2016"

name: "segments"
doc-link: https://developers.intercom.com/reference#segments
description: |
  The `{{ table.name }}` table contains info about the segments - or groups of users defined by a set of rules - in your {{ integration.display_name }} account.

replication-method: "Full Table"
api-method:
  name: listSegments
  doc-link: https://developers.intercom.io/docs/list-segments

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The segment ID."
    foreign-key-id: "segment-id"

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