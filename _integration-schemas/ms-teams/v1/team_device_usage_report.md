---
tap: "ms-teams"
version: "1"
key: ""

name: "team_device_usage_report"
doc-link: "https://docs.microsoft.com/en-us/graph/api/reportroot-getteamsdeviceusageuserdetail?view=graph-rest-beta"
singer-schema: "https://github.com/singer-io/tap-ms-teams/blob/master/tap_ms_teams/schemas/team_device_usage_report.json"
description: |
  The `{{ table.name }}` table contains information about a group's device usage in {{ integration.display_name }}.

replication-method: "Key-based Incremental"

api-method:
    name: |
      reportRoot: getTeamsDeviceUsageUserDetail
    doc-link: "https://docs.microsoft.com/en-us/graph/api/reportroot-getteamsdeviceusageuserdetail?view=graph-rest-beta"
    
attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The device ID."
    #foreign-key-id: "device-id"

  - name: "report_refresh_date"
    type: "string"
    description: "The date the report was last refreshed."
    replication-key: true

  - name: "deleted_date"
    type: "string"
    description: ""
  - name: "is_deleted"
    type: "string"
    description: ""
  - name: "last_activity_date"
    type: "string"
    description: ""
  - name: "report_period"
    type: "string"
    description: ""
  
  - name: "used_android_phone"
    type: "string"
    description: ""
  - name: "used_i_os"
    type: "string"
    description: ""
  - name: "used_mac"
    type: "string"
    description: ""
  - name: "used_web"
    type: "string"
    description: ""
  - name: "used_windows"
    type: "string"
    description: ""
  - name: "used_windows_phone"
    type: "string"
    description: ""
  - name: "user_principal_name"
    type: "string"
    description: ""
---
