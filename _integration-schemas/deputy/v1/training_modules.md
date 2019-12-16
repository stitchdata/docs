---
tap: "deputy"
version: "1.0"
key: "training-module"

name: "training_modules"
doc-link: "https://www.deputy.com/api-doc/Resources/TrainingModule"

description: |
  The `{{ table.name }}` table contains info about training modules.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The training module ID."
    foreign-key-id: "training-module-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the training module was last modified."

  - name: "Title"
    type: "string"
    description: ""

  - name: "Provider"
    type: "string"
    description: ""

  - name: "ProviderAddress"
    type: "string"
    description: ""

  - name: "Cost"
    type: "number"
    description: ""

  - name: "TimeRequiredDays"
    type: "integer"
    description: ""

  - name: "RenewalPeriodMonths"
    type: "integer"
    description: ""

  - name: "Comment"
    type: "string"
    description: ""

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---