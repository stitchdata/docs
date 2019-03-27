---
tap: "zendesk"
version: "1.0"

name: "tags"
doc-link: https://developer.zendesk.com/rest_api/docs/support/tags
singer-schema: https://github.com/singer-io/tap-zendesk/blob/master/tap_zendesk/schemas/tags.json
description: |
  The `{{ table.name }}` table the names and total number of applications of the tags in your {{ integration.display_name }} account.

  **Note**: Retrieving tag data requires {{ integration.display_name }} Admin permissions.

replication-method: "Full Table"

api-method:
  name: List tags
  doc-link: https://developer.zendesk.com/rest_api/docs/support/tags#list-tags

attributes:
  - name: "name"
    type: "string"
    primary-key: true
    description: "The name of the tag."
    foreign-key-id: "tag-id"

  - name: "count"
    type: "integer"
    description: "The total number of times the tag has been applied to objects in your {{ integration.display_name }} account."
---