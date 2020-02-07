---
tap: "deputy"
version: "1"
key: "employment-condition"

name: "employment_conditions"
doc-link: "https://www.deputy.com/api-doc/Resources/EmploymentCondition"

description: |
  The `{{ table.name }}` table contains info about employment conditions.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The employment condition ID."
    foreign-key-id: "employment-condition-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the employment condition was last modified."

  - name: "Name"
    type: "string"
    description: ""

  - name: "Description"
    type: "string"
    description: ""

  - name: "AwardLevel"
    type: "string"
    description: ""

  - name: "EmploymentBasis"
    type: "integer"
    description: ""

  - name: "EmploymentCategory"
    type: "integer"
    description: ""
    foreign-key-id: "category-id"

  - name: "EmploymentPeriod"
    type: "integer"
    description: ""

  - name: "EmploymentStatus"
    type: "integer"
    description: ""

  - name: "ProbationaryPeriod"
    type: "integer"
    description: ""

  - name: "WorkingDaysPerPeriod"
    type: "number"
    description: ""

  - name: "UsualStartTime"
    type: "string"
    description: ""

  - name: "UsualFinishTime"
    type: "string"
    description: ""

  - name: "UsualMealbreak"
    type: "string"
    description: ""

  - name: "AvgHoursPerDay"
    type: "number"
    description: ""

  - name: "MinHoursPerDay"
    type: "number"
    description: ""

  - name: "MinHoursForLeave"
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