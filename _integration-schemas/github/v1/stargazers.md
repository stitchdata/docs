---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "github"
version: "1"
key: "stargazer"

name: "stargazers"
doc-link: ""
singer-schema: https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/stargazers.json
description: |
  The `{{ table.name }}` table contains info about users who have starred the repositories specified for the integration.


# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "List stargazers"
  doc-link: "https://docs.github.com/en/rest/reference/activity#list-stargazers"

replication-method: "Key-based Incremental"
replication-key:
  name: "since"
  based-on: "starred_at"
  tooltip: "This is a query parameter used to extract new/updated data from GitHub. It will not be included in the table's fields."


# -------------------------- #
#       Table Attributes     #
# -------------------------- #

attributes:
  - name: "user_id"
    type: "integer"
    primary-key: true
    description: "The user ID."
    # foreign-key-id: "stargazer-id"

  - name: "_sdc_repository"
    type: "string"
    description: ""

  - name: "starred_at"
    type: "string"
    description: "The time the user starred the repository."

  - name: "user"
    type: "object"
    description: "Details about the user who starred the repository."
    subattributes:
      - name: "id"
        type: "integer"
        description: "The user ID."
---
