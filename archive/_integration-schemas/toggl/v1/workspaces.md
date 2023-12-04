---
tap: "toggl"
version: "1"

name: "workspaces"
doc-link: "https://github.com/toggl/toggl_api_docs/blob/master/chapters/workspaces.md"
singer-schema: "https://github.com/singer-io/tap-toggl/blob/master/tap_toggl/schemas/a_workspaces.json"
description: |
  The `{{ table.name }}` table contains info about the workspaces in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "Get workspaces"
    doc-link: "https://github.com/toggl/toggl_api_docs/blob/master/chapters/workspaces.md#get-workspaces"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The workspace ID."
    foreign-key-id: "workspace-id"

  - name: "at"
    type: "date-time"
    replication-key: true
    description: "The date and time the workspace was last updated."

  - name: "admin"
    type: "boolean"
    description: "Indicates whether the currently requesting user has admin access to the workspace."

  - name: "default_currency"
    type: "string"
    description: "The default currency for the workspace."

  - name: "default_hourly_rate"
    type: "integer"
    description: "The default hourly rate for the workspace."

  - name: "logo_url"
    type: "string"
    description: "The URL pointing to the workspace logo."

  - name: "name"
    type: "string"
    description: "The name of the workspace."

  - name: "only_admins_may_create_projects"
    type: "boolean"
    description: "Indicates whether only admins can create projects."

  - name: "only_admins_see_billable_rates"
    type: "boolean"
    description: "Indicates whether only admins can see billable rates."

  - name: "premium"
    type: "boolean"
    description: "Indicates if the workspace is a pro workspace."

  - name: "rounding"
    type: "integer"
    description: |
      The type of rounding used by the workspace. Possible values are:

      - `-1` - Round down
      - `0` - Nearest
      - `1` - Round up

  - name: "rounding_minutes"
    type: "integer"
    description: "Round up to the nearest minute."
---