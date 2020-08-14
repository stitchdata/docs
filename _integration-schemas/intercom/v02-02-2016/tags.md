---
tap: "intercom"
version: "02-02-2016"

name: "tags"
doc-link: https://developers.intercom.io/docs/tags
description: |
  The `{{ table.name }}` table contains info about the tags in your {{ integration.display_name }} account.

replication-method: "Full Table"
api-method:
  name: listTags
  doc-link: https://developers.intercom.io/docs/list-tags

attributes:
  - name: "id"
    primary-key: true
    type: "string"
    description: "The tag ID."
    foreign-key-id: "tag-id"

  - name: "name"
    type: "string"
    description: "The name of the tag."

  - name: "type"
    type: "string"
    description: "The value of this field will be `tag`."
---