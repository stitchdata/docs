---
tap: "intercom"
# version:

name: "tags"
doc-link: https://developers.intercom.io/docs/tags
description: |
  The `tags` table contains info about the tags in your Intercom account.

replication-method: "Full Table"
api-method:
  name: listTags
  doc-link: https://developers.intercom.io/docs/list-tags

attributes:
  - name: "id"
    primary-key: true
    type: "string"
    description: "The tag ID."
    # foreign-keys:
    #   - table: "leads__tags"
    #     attribute: "id"
    #   - table: "conversations__tags"
    #     attribute: "id"

  - name: "name"
    type: "string"
    description: "The name of the tag."

  - name: "type"
    type: "string"
    description: "The value of this field will be `tag`."
---