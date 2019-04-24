---
tap: "netsuite"
version: "1.0"

name: "Topic"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/topic.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Topic.json"
description: |
  The `{{ table.name }}` table contains info about the topics used to organize knowledge base solutions in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "topic"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "topic-id"

  - name: "description"
    type: "string"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "longDescription"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "parentTopic"
    type: "varies"
    description: ""

  - name: "solutionList"
    type: "varies"
    description: ""

  - name: "title"
    type: "string"
    description: ""
---