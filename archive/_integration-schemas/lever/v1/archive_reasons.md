---
tap: "lever"
version: "1"
key: "archive-reason"

name: "archive_reasons"
doc-link: "https://hire.lever.co/developer/documentation#archive-reasons"
singer-schema: "https://github.com/singer-io/tap-lever/blob/master/tap_lever/schemas/archive_reasons.json"
description: |
  The `{{ table.name }}` table contains info about the reasons candidates have exited your active hiring pipeline. Refer to [{{ integration.display_name }}'s documentation](https://help.lever.co/hc/articles/204502125){:target="new"} for more info.

replication-method: "Full Table"

api-method:
  name: "List all archive reasons"
  doc-link: "https://hire.lever.co/developer/documentation#list-all-archive-reasons"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The archive reason ID."
    foreign-key-id: "archive-reason-id"

  - name: "text"
    type: "string"
    description: "A description for the archive reason. For example: `Withdrew`"
---