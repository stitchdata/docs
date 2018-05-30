---
tap: "zendesk"
version: "1.0"

name: "tags"
doc-link: https://developer.zendesk.com/rest_api/docs/core/tags
singer-schema: https://github.com/singer-io/tap-zendesk/blob/master/tap_zendesk/schemas/tags.json
description: |
  The `tags` table contains info about the tags in your Zendesk account.

  **Note**: Retrieving tag data requires Zendesk Admin permissions.

replication-method: "Full Table"

attributes:
  - name: "name"
    type: ""
    primary-key: true
    description: ""

  - name: ""
    type: 
    description:

---