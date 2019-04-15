---
tap: "netsuite"
version: "1.0"

name: "Solution"
doc-link: "https://975200-sb2.app.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/solution.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Solution.json"
description: |
  The `{{ table.name }}` table contains info about the solutions, or answers to customer issues, in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

permission:
  tab: "Lists"
  name: "Knowledge Base"

feature-requirements:
  - tab: "CRM"
    name: "Knowledge Base"

replication-method: "Key-based Incremental"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "solution-id"

  - name: "lastModifiedDate"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "assigned"
    type: "varies"
    description: ""

  - name: "createdDate"
    type: "date-time"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "customForm"
    type: "varies"
    description: ""

  - name: "displayOnline"
    type: "boolean, string"
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

  - name: "message"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "solutionCode"
    type: "string"
    description: ""

  - name: "solutionsList"
    type: "varies"
    description: ""

  - name: "status"
    type: "varies"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "topicsList"
    type: "varies"
    description: ""
---