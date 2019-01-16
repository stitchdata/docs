---
tap: "netsuite"
# version: "10-15-2015"

name: "netsuite_app_definition"
doc-link: 
description: |
  The `{{ table.name }}` table contains info about the app definitions in your NetSuite instance.

replication-method: "Full Table"
primary-key: "internalId"
abstract: false

permissions:
  - name: "Integration Application"
    level: "View"
    location: "Setup"

attributes:
  - name: "internalId"
    type: "integer"
    primary-key: true
    description: "The app definition ID."

  - name: "Your Selected Fields"
    description: |
      Other fields selected by you.
---