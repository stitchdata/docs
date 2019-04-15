---
tap: "netsuite"
version: "1.0"

name: "BillingSchedule"
doc-link: "https://975200-sb2.app.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/billingschedule.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/BillingSchedule.json"
description: |
  The `{{ table.name }}` table contains info about the billing schedules in your {{ integration.display_name }} account. Billing schedules are used to define how bills for transactions are relayed to customers. In general, a billing schedule determines the frequency with which the customer is billed and the amount of each bill. However, the exact effect of a billing schedule varies depending on its type.

  {{ integration.permission-for-table | flatify }}

permission:
  tab: "Lists"
  name: "Billing Schedules"

feature-requirements:
  - tab: &tab "Accounting"
    name: "Advanced Billing"
    description: "(Required for any billing schedule type)"
  - tab: *tab
    name: "Project Management"
    description: "(Required for Charge-based, Fix-bid interval, Fixed-bid milestone, and Time and materials billing schedules)"
  - tab: *tab
    name: "Charge-based Billing"
    description: "(Required for Charge-based billing schedules)"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "billing-schedule-id"

  - name: "applyToSubtotal"
    type: "boolean, string"
    description: ""

  - name: "billForActuals"
    type: "boolean, string"
    description: ""

  - name: "dayPeriod"
    type: "integer, string"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "frequency"
    type: "varies"
    description: ""

  - name: "inArrears"
    type: "boolean, string"
    description: ""

  - name: "initialAmount"
    type: "string"
    description: ""

  - name: "initialTerms"
    type: "varies"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "isPublic"
    type: "boolean, string"
    description: ""

  - name: "milestoneList"
    type: "varies"
    description: ""

  - name: "monthDom"
    type: "integer, string"
    description: ""

  - name: "monthDow"
    type: "varies"
    description: ""

  - name: "monthDowim"
    type: "varies"
    description: ""

  - name: "monthMode"
    type: "varies"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "numberRemaining"
    type: "integer, string"
    description: ""

  - name: "project"
    type: "varies"
    description: ""

  - name: "recurrenceDowMaskList"
    type: "varies"
    description: ""

  - name: "recurrenceList"
    type: "varies"
    description: ""

  - name: "recurrencePattern"
    type: "varies"
    description: ""

  - name: "recurrenceTerms"
    type: "varies"
    description: ""

  - name: "repeatEvery"
    type: "varies"
    description: ""

  - name: "scheduleType"
    type: "varies"
    description: ""

  - name: "seriesStartDate"
    type: "date-time"
    description: ""

  - name: "transaction"
    type: "varies"
    description: ""

  - name: "yearDom"
    type: "integer, string"
    description: ""

  - name: "yearDow"
    type: "varies"
    description: ""

  - name: "yearDowim"
    type: "varies"
    description: ""

  - name: "yearDowimMonth"
    type: "varies"
    description: ""

  - name: "yearMode"
    type: "varies"
    description: ""

  - name: "yearMonth"
    type: "varies"
    description: ""
---