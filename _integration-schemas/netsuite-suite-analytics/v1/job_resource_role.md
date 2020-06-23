---
tap: "netsuite-suite-analytics"
version: "1"
key: "job-resource-role"

name: "job_resource_role"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/job_resource_role.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "description"
    type: "string"
    description: ""

  - name: "has_own_time_approval"
    type: "string"
    description: ""

  - name: "has_replace_assignments"
    type: "string"
    description: ""

  - name: "is_project_time_approver"
    type: "string"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "job_resource_role_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "job-resource-role-id"

  - name: "name"
    type: "string"
    description: ""

  - name: "send_mail_for_ratoff_conflict"
    type: "string"
    description: ""
---