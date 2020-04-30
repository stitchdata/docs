---
tap: "outreach"
version: "1"

name: "duties"
doc-link: "https://api.outreach.io/api/v2/docs#duty"
singer-schema: "https://github.com/singer-io/tap-outreach/blob/master/tap_outreach/schemas/duties.json"
description: |
  The {{ table.name }} table contains {{ integration.display_name }}-suggested job roles for users.

replication-method: "Full Table"

api-method:
    name: "Duty"
    doc-link: "https://api.outreach.io/api/v2/docs#duty"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The duty ID."
    #foreign-key-id: "duty-id"
    
  - name: "dutyType"
    type: "string"
    description: ""
  - name: "symbolicName"
    type: "string"
    description: ""
---
