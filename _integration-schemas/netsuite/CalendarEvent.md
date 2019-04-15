---
tap: "netsuite"
version: "1.0"

name: "CalendarEvent"
doc-link: "https://975200-sb2.app.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/calendarevent.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/CalendarEvent.json"
description: |
  The `{{ table.name }}` table contains info about the scheduled activities, or events, that are on the calendar in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

permission:
  tab: "Lists"
  name: "Calendar"

replication-method: "Key-based Incremental"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "calendar-event-id"

  - name: "lastModifiedDate"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "accessLevel"
    type: "varies"
    description: ""

  - name: "allDayEvent"
    type: "boolean, string"
    description: ""

  - name: "attendeeList"
    type: "varies"
    description: ""

  - name: "company"
    type: "varies"
    description: ""

  - name: "contact"
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

  - name: "endByDate"
    type: "date-time"
    description: ""

  - name: "endDate"
    type: "date-time"
    description: ""

  - name: "exclusionDateList"
    type: "varies"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "frequency"
    type: "varies"
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
    type: "varies"
    description: ""

  - name: "organizer"
    type: "varies"
    description: ""

  - name: "owner"
    type: "varies"
    description: ""

  - name: "period"
    type: "integer, string"
    description: ""

  - name: "recurrence"
    type: "string"
    description: ""

  - name: "recurrenceDow"
    type: "varies"
    description: ""

  - name: "recurrenceDowMaskList"
    type: "varies"
    description: ""

  - name: "recurrenceDowim"
    type: "varies"
    description: ""

  - name: "reminderMinutes"
    type: "varies"
    description: ""

  - name: "reminderType"
    type: "varies"
    description: ""

  - name: "resourceList"
    type: "varies"
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
    type: "varies"
    description: ""

  - name: "supportCase"
    type: "varies"
    description: ""

  - name: "timeItemList"
    type: "varies"
    description: ""

  - name: "timedEvent"
    type: "boolean, string"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "transaction"
    type: "varies"
    description: ""
---