---
tap: "intercom"
version: "1"
key: "tag"

name: "tags"
doc-link: "https://developers.intercom.com/intercom-api-reference/reference#tag-model"
singer-schema: "https://github.com/singer-io/tap-intercom/blob/master/tap_intercom/schemas/tags.json"
description: |
  The `{{ table.name }}` table contains information about tags within your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "List all tags"
  doc-link: "https://developers.intercom.com/intercom-api-reference/reference#list-tags-for-an-app"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The tag ID."
    foreign-key-id: "tag-id"
    
  - name: "name"
    type: "string"
    description: "The name of the tag."

  - name: "type"
    type: "string"
    description: "This will be `tag`."
---