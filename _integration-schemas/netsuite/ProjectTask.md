---
tap: "netsuite"
version: "1.0"

name: "ProjectTask"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/projecttask.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/ProjectTask.json"
description: |
  The `{{ table.name }}` table contains info about the project tasks in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "project-task"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "project-task-id"

  - name: "actualWork"
    type: "number, string"
    description: ""

  - name: "assigneeList"
    type: "varies"
    description: ""

  - name: "company"
    type: "varies"
    description: ""

  - name: "constraintType"
    type: "varies"
    description: ""

  - name: "contact"
    type: "varies"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "customForm"
    type: "varies"
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
    type: "varies"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "finishByDate"
    type: "date-time"
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
    type: "varies"
    description: ""

  - name: "order"
    type: "varies"
    description: ""

  - name: "owner"
    type: "varies"
    description: ""

  - name: "parent"
    type: "varies"
    description: ""

  - name: "percentTimeComplete"
    type: "number, string"
    description: ""

  - name: "predecessorList"
    type: "varies"
    description: ""

  - name: "priority"
    type: "varies"
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
    type: "varies"
    description: ""

  - name: "timeItemList"
    type: "varies"
    description: ""

  - name: "title"
    type: "string"
    description: ""
---