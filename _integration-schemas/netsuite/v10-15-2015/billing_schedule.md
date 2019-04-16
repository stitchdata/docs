---
tap: "netsuite"
version: "10-15-2015"

name: "netsuite_billing_schedule"
doc-link: 
description: |
  The `{{ table.name }}` table contains info about the accounts in your NetSuite instance.



replication-method: "Full Table"
primary-key: "internalId"
abstract: false

permissions:
  - name: "Billing Schedules"
    level: "View"
    location: "Lists"

attributes:
  - name: "internalId"
    type: "integer"
    primary-key: true
    description: "The account ID."

  - name: "Your Selected Fields"
    description: |
      Other fields selected by you.
---