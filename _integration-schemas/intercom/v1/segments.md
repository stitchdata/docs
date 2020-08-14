---
tap: "intercom"
version: "1"

name: "segments"
doc-link: "https://developers.intercom.com/intercom-api-reference/v2.0/reference#segment-model"
singer-schema: "https://github.com/singer-io/tap-intercom/blob/master/tap_intercom/schemas/segments.json"
description: 
  The `{{ table.name }}` table contains information about segments within your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "List all segments"
  doc-link: "https://developers.intercom.com/intercom-api-reference/v2.0/reference#list-segments"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The segment ID."
    foreign-key-id: "segment-id"

  - name: "updated_at"
    type: "date-time"
    description: "The time the segment was last updated."
    replication-key: true  

  - name: "count"
    type: "integer"
    description: "The number of items in the segment."

  - name: "created_at"
    type: "date-time"
    description: "The time the segment was created."
  
  - name: "name"
    type: "string"
    description: "The name of the segment."

  - name: "type"
    type: "string"
    description: "This will be `segment`."
---