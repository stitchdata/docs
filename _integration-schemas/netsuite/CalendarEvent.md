---
tap: "netsuite"
# version: "1.0"

name: "CalendarEvent"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/CalendarEvent.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "accessLevel"
    type: "anything"
    description: ""

  - name: "allDayEvent"
    type: "boolean, string"
    description: ""

  - name: "attendeeList"
    type: "anything"
    description: ""

  - name: "company"
    type: "anything"
    description: ""

  - name: "contact"
    type: "anything"
    description: ""

  - name: "createdDate"
    type: "date-time"
    description: ""

  - name: "customFieldList"
    type: "anything"
    description: ""

  - name: "customForm"
    type: "anything"
    description: ""

  - name: "endByDate"
    type: "date-time"
    description: ""

  - name: "endDate"
    type: "date-time"
    description: ""

  - name: "exclusionDateList"
    type: "anything"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "frequency"
    type: "anything"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "lastModifiedDate"
    type: "date-time"
    description: ""

  - name: "location"
    type: "string"
    description: ""

  - name: "message"
    type: "string"
    description: ""

  - name: "noEndDate"
    type: "boolean, string"
    description: ""

  - name: "nullFieldList"
    type: "anything"
    description: ""

  - name: "organizer"
    type: "anything"
    description: ""

  - name: "owner"
    type: "anything"
    description: ""

  - name: "period"
    type: "integer, string"
    description: ""

  - name: "recurrence"
    type: "string"
    description: ""

  - name: "recurrenceDow"
    type: "anything"
    description: ""

  - name: "recurrenceDowMaskList"
    type: "anything"
    description: ""

  - name: "recurrenceDowim"
    type: "anything"
    description: ""

  - name: "reminderMinutes"
    type: "anything"
    description: ""

  - name: "reminderType"
    type: "anything"
    description: ""

  - name: "resourceList"
    type: "anything"
    description: ""

  - name: "sendEmail"
    type: "boolean, string"
    description: ""

  - name: "seriesStartDate"
    type: "date-time"
    description: ""

  - name: "startDate"
    type: "date-time"
    description: ""

  - name: "status"
    type: "anything"
    description: ""

  - name: "supportCase"
    type: "anything"
    description: ""

  - name: "timeItemList"
    type: "anything"
    description: ""

  - name: "timedEvent"
    type: "boolean, string"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "transaction"
    type: "anything"
    description: ""
---
