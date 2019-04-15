---
tap: "netsuite"
version: "1.0"

name: "JobType"
doc-link: "https://975200-sb2.app.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/jobtype.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/JobType.json"
description: |
  The `{{ table.name }}` table contains info about the types that can be applied to projects in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

permission:
  tab: "Lists"
  name: "Projects"

feature-requirements:
  - tab: "Company"
    name: "Projects"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "job-type-id"

  - name: "externalId"
    type: "string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "parent"
    type: "varies"
    description: ""
---