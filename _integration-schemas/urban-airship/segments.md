---
tap: "urban-airship"
version: "1"

name: "segments"
doc-link: http://docs.urbanairship.com/api/ua.html#segments
singer-schema: 
description: |
  The `{{ table.name }}` table contains info about segments, or portions of your audience that have arbitrary metadata attached.

replication-method: "Key-based Incremental"
api-method:
  name: segmentListing
  doc-link: https://docs.urbanairship.com/api/ua/#segment-listing

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The segment ID."
    #foreign-key-id: "segment-id"

  - name: "creation_date"
    type: "date-time"
    replication-key: true
    description: "The date the segment was created."

  - name: "modification_date"
    type: "date-time"
    replication-key: true
    description: "The date that the segment was last updated."

  - name: "display_name"
    type: "string"
    description: "The display name of the segment."
---