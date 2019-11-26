---
tap: "deputy"
version: "1.0"
key: "operational-unit"

name: "operational_units"
doc-link: "https://www.deputy.com/api-doc/Resources/OperationalUnit"

description: |
  The `{{ table.name }}` table contains info about operational units.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The operational unit ID."
    foreign-key-id: "operational-unit-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the operational unit was last modified."

  - name: "Company"
    type: "integer"
    description: ""
    foreign-key-id: "company-id"

  - name: "ParentOperationalUnit"
    type: "integer"
    description: ""
    foreign-key-id: "operational-unit-id"

  - name: "OperationalUnitName"
    type: "string"
    description: ""

  - name: "Active"
    type: "boolean"
    description: ""

  - name: "PayrollExportName"
    type: "string"
    description: ""

  - name: "Address"
    type: "integer"
    description: ""
    foreign-key-id: "address-id"

  - name: "Contact"
    type: "integer"
    description: ""
    foreign-key-id: "contact-id"

  - name: "RosterSortOrder"
    type: "integer"
    description: ""

  - name: "ShowOnRoster"
    type: "boolean"
    description: ""

  - name: "RosterActiveHoursSchedule"
    type: "integer"
    description: ""
    foreign-key-id: "schedule-id"

  - name: "DailyRosterBudget"
    type: "number"
    description: ""

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---