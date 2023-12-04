---
tap: "lever"
version: "1"
key: "source"

name: "sources"
doc-link: "https://hire.lever.co/developer/documentation#sources"
singer-schema: "https://github.com/singer-io/tap-lever/blob/master/tap_lever/schemas/sources.json"
description: |
  The `{{ table.name }}` table contains info about sources, or the ways that candidates enter into your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "List all sources"
  doc-link: "https://hire.lever.co/developer/documentation#list-all-sources"

attributes:
  - name: "text"
    type: "string"
    primary-key: true
    description: "A description of the source. For example: `Email Applicant`"
    # foreign-key-id: "source-id"

  - name: "count"
    type: "integer"
    description: "The number of candidates tagged with the source."
---