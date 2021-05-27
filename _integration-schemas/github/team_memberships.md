---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "github"
version: "1"
key: "team-membership"

name: "team_memberships"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/team_memberships.json"
description: |
  The `{{ table.name }}` table contains info about membership of users in of organization teams that are visible to the user who authorized the integration.

  **Note**: In order to replicate this table, you must also set the [`teams`](#teams) table to replicate.


# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "Get team membership for a user"
  doc-link: "https://docs.github.com/en/rest/reference/teams#get-team-membership-for-a-user"

replication-method: "Key-based Incremental"
replication-key:
  name: "since"
  tooltip: "This is a query parameter used to extract new/updated data from GitHub. It will not be included in the table's fields."

dependent-table-key: "team"


# -------------------------- #
#       Table Attributes     #
# -------------------------- #

attributes:
  - name: "url"
    type: "string"
    primary-key: true
    description: ""

  - name: "_sdc_repository"
    type: "string"
    description: ""

  - name: "role"
    type: "string"
    description: ""

  - name: "state"
    type: "string"
    description: ""
---