---
tap: "netsuite"
version: "1.0"

name: "Usage"
doc-link: "https://975200-sb2.app.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/usage.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Usage.json"
description: |
  The `{{ table.name }}` table contains info about the subscription billing lines in your {{ integration.display_name }} account. For example: Money, time, cellular data, internet data, etc.

  {{ integration.permission-for-table | flatify }}

permission:
  tab: "Lists"
  name: "Subscriptions"

feature-requirements:
  - name: "SuiteBilling"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "usage-id"

  - name: "customForm"
    type: "varies"
    description: ""

  - name: "customer"
    type: "varies"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "item"
    type: "varies"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "subscriptionPlan"
    type: "varies"
    description: ""

  - name: "usageDate"
    type: "date-time"
    description: ""

  - name: "usageQuantity"
    type: "number, string"
    description: ""

  - name: "usageSubscription"
    type: "varies"
    description: ""

  - name: "usageSubscriptionLine"
    type: "varies"
    description: ""
---