---
tap: "deputy"
version: "1.0"
key: "stress-profile"

name: "stress_profiles"
doc-link: "https://www.deputy.com/api-doc/Resources/StressProfile"

description: |
  The `{{ table.name }}` table contains info about stress profiles.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The stress profile ID."
    #foreign-key-id: "stress-profile-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the stress profile was last modified."

  - name: "Name"
    type: "string"
    description: ""

  - name: "MaxHoursPerShift"
    type: "number"
    description: ""

  - name: "MaxHoursPerPeriod"
    type: "number"
    description: ""

  - name: "MaxDaysPerPeriod"
    type: "number"
    description: ""

  - name: "MaxHoursPerDay"
    type: "number"
    description: ""

  - name: "GapHoursBetweenShifts"
    type: "number"
    description: ""

  - name: "CustomRules"
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