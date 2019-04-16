---
tap: "netsuite"
# version: "1.0"

name: "Issue"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Issue.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
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

  - name: "internalId"
    type: "string"
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

  - name: "lastModifiedDate"
    type: "date-time"
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
