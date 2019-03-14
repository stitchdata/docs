---
tap: "toggl"
version: "1.0"

name: "time_entries"
doc-link: "https://github.com/toggl/toggl_api_docs/blob/master/reports/detailed.md"
singer-schema: "https://github.com/singer-io/tap-toggl/blob/master/tap_toggl/schemas/time_entries.json"
description: |
  The `{{ table.name }}` table contains info about time entries. **Note**: This table uses an attribution window to replicate data. Refer to the [Replicating time entry data](#replicating-time-entry-data) section for more info.

  #### Time entries and user permissions {#time-entries-user-permissions}

  The time entries Stitch replicates are dependent upon the user whose API token is used to create the integration in Stitch. Stitch is only able to access the same data as the user whose token is used.

  For example: If the user is unable to access a workspace, or is not an Admin in that workspace, Stitch will not be able to replicate time entry data for those workspaces. In this case, only the user's own time entries will be accessible by Stitch.

  If data from a workspace is missing, verify that the user whose API token is being used in Stitch has Admin permissions in that workspace.

replication-method: "Key-based Incremental"
api-method:
    name: "Get detailed report"
    doc-link: "https://github.com/toggl/toggl_api_docs/blob/master/reports/detailed.md"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The time entry ID."

  - name: "updated"
    type: "date-time"
    replication-key: true
    description: "The date and time the time entry was last updated."

  - name: "billable"
    type: "number"
    description: "The billed amount for the time entry."

  - name: "client"
    type: "string"
    description: "The client name for which the time entry was recorded."

  - name: "cur"
    type: "string"
    description: "The billable amount currency."

  - name: "description"
    type: "string"
    description: "The description of the time entry."

  - name: "dur"
    type: "integer"
    description: "The time entry duration in milliseconds."

  - name: "end"
    type: "date-time"
    description: |
      The end time of the time entry in[ISO 8601 date and time format](https://en.wikipedia.org/wiki/ISO_8601){:target="new"}.

  - name: "is_billable"
    type: "boolean"
    description: "Indicates if the time entry is billable or not."

  - name: "pid"
    type: "integer"
    description: "The ID of the project associated with the time entry."
    foreign-key-id: "project-id"

  - name: "project"
    type: "string"
    description: "The name of the project for which the time entry was recorded."

  - name: "start"
    type: "date-time"
    description: |
      The start time of the time entry in[ISO 8601 date and time format](https://en.wikipedia.org/wiki/ISO_8601){:target="new"}.

  - name: "tags"
    type: "array"
    description: "A list of tag names associated with the time entry."
    subattributes:
      - name: "value"
        type: "string"
        description: "The name of the tag."

  - name: "task"
    type: "string"
    description: "The task name for which the time entry was recorded."

  - name: "tid"
    type: "integer"
    description: "The ID of the task associated with the time entry."
    foreign-key-id: "task-id"

  - name: "uid"
    type: "integer"
    description: "The ID of the user associated with the time entry."
    foreign-key-id: "user-id"

  - name: "use_stop"
    type: "boolean"
    description: "Indicates if the stop time is saved on the time entry according to the `user`'s personal settings."

  - name: "user"
    type: "string"
    description: "The full name of the user associated with the time entry."
---