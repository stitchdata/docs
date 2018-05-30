---
tap: "zendesk"
version: "1.0"

name: "tags"
doc-link: https://developer.zendesk.com/rest_api/docs/core/tags
singer-schema: https://github.com/singer-io/tap-zendesk/blob/master/tap_zendesk/schemas/tags.json
description: |
  The `tags` table the names and total number of applications of the tags in your Zendesk account.

  **Note**: Retrieving tag data requires Zendesk Admin permissions.

replication-method: "Full Table"

api-method:
  name: 
  doc-link: 

attributes:
  - name: "name"
    type: "string"
    primary-key: true
    description: "The name of the tag."

  - name: "count"
    type: "integer"
    description: "The total number of times the tag has been applied to objects in your Zendesk account."

---