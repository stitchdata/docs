---
tap: "netsuite"
version: "1.0"

name: "Issue"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/issue.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Issue.json"
description: |
  The `{{ table.name }}` table contains info about the support cases in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "issue"

replication-method: "Key-based Incremental"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "issue-id"

  - name: "lastModifiedDate"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "assigned"
    type: "varies"
    description: ""

  - name: "brokenInVersionList"
    type: "varies"
    description: ""

  - name: "buildBroken"
    type: "varies"
    description: ""

  - name: "buildFixed"
    type: "varies"
    description: ""

  - name: "buildTarget"
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

  - name: "emailAssignee"
    type: "boolean, string"
    description: ""

  - name: "emailCellsList"
    type: "varies"
    description: ""

  - name: "emailEmployeesList"
    type: "varies"
    description: ""

  - name: "externalAbstract"
    type: "string"
    description: ""

  - name: "externalDetails"
    type: "string"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "fixedInVersionList"
    type: "varies"
    description: ""

  - name: "isOwner"
    type: "boolean, string"
    description: ""

  - name: "isReviewed"
    type: "boolean, string"
    description: ""

  - name: "isShowStopper"
    type: "boolean, string"
    description: ""

  - name: "issueAbstract"
    type: "string"
    description: ""

  - name: "issueNumber"
    type: "string"
    description: ""

  - name: "issueStatus"
    type: "varies"
    description: ""

  - name: "issueTagsList"
    type: "varies"
    description: ""

  - name: "issueType"
    type: "varies"
    description: ""

  - name: "item"
    type: "varies"
    description: ""

  - name: "module"
    type: "varies"
    description: ""

  - name: "newDetails"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "priority"
    type: "varies"
    description: ""

  - name: "product"
    type: "varies"
    description: ""

  - name: "productTeam"
    type: "varies"
    description: ""

  - name: "relatedIssuesList"
    type: "varies"
    description: ""

  - name: "reportedBy"
    type: "varies"
    description: ""

  - name: "reproduce"
    type: "varies"
    description: ""

  - name: "reviewer"
    type: "varies"
    description: ""

  - name: "severity"
    type: "varies"
    description: ""

  - name: "source"
    type: "varies"
    description: ""

  - name: "targetVersionList"
    type: "varies"
    description: ""

  - name: "trackCode"
    type: "varies"
    description: ""

  - name: "versionBroken"
    type: "varies"
    description: ""

  - name: "versionFixed"
    type: "varies"
    description: ""

  - name: "versionTarget"
    type: "varies"
    description: ""
---