---
tap: "netsuite"
# version: "1.0"

name: "ProjectTask"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/ProjectTask.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "actualWork"
    type: "number, string"
    description: ""

  - name: "assigneeList"
    type: "anything"
    description: ""

  - name: "company"
    type: "anything"
    description: ""

  - name: "constraintType"
    type: "anything"
    description: ""

  - name: "contact"
    type: "anything"
    description: ""

  - name: "customFieldList"
    type: "anything"
    description: ""

  - name: "customForm"
    type: "anything"
    description: ""

  - name: "endDate"
    type: "date-time"
    description: ""

  - name: "endDateBaseline"
    type: "date-time"
    description: ""

  - name: "estimatedWork"
    type: "number, string"
    description: ""

  - name: "estimatedWorkBaseline"
    type: "number, string"
    description: ""

  - name: "eventId"
    type: "anything"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "finishByDate"
    type: "date-time"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "isMilestone"
    type: "boolean, string"
    description: ""

  - name: "isOnCriticalPath"
    type: "string"
    description: ""

  - name: "lateEnd"
    type: "date-time"
    description: ""

  - name: "lateStart"
    type: "date-time"
    description: ""

  - name: "message"
    type: "string"
    description: ""

  - name: "nonBillableTask"
    type: "boolean, string"
    description: ""

  - name: "nullFieldList"
    type: "anything"
    description: ""

  - name: "order"
    type: "anything"
    description: ""

  - name: "owner"
    type: "anything"
    description: ""

  - name: "parent"
    type: "anything"
    description: ""

  - name: "percentTimeComplete"
    type: "number, string"
    description: ""

  - name: "predecessorList"
    type: "anything"
    description: ""

  - name: "priority"
    type: "anything"
    description: ""

  - name: "remainingWork"
    type: "number, string"
    description: ""

  - name: "slackMinutes"
    type: "number, string"
    description: ""

  - name: "startDate"
    type: "date-time"
    description: ""

  - name: "startDateBaseline"
    type: "date-time"
    description: ""

  - name: "status"
    type: "anything"
    description: ""

  - name: "timeItemList"
    type: "anything"
    description: ""

  - name: "title"
    type: "string"
    description: ""
---
