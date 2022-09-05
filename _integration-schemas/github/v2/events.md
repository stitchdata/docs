---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "github"
version: "2"
key: "event"

name: "events"
doc-link: "https://developer.github.com/v3/activity/events/"
singer-schema: "https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/events.json"
description: |
  The `{{ table.name }}` table contains information about events in the repositories specified for the integration.


# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "List events for a repository"
  doc-link: "https://docs.github.com/en/rest/activity/events#list-repository-events"

replication-method: "Key-based Incremental"
replication-key:
  name: "since"
  based-on: "`updated_at` if non-NULL; otherwise `created_at`"
  tooltip: "This is a query parameter used to extract new/updated data from GitHub. It will not be included in the table's fields."


# -------------------------- #
#       Table Attributes     #
# -------------------------- #

attributes:
  - name: "id"
    type: "number"
    primary-key: true
    description: "The event ID."
    foreign-key-id: "event-id"

  - name: "actor"
    type: "object"
    description: "Information about the user that triggered an event."
    subattributes:
      - name: "avatar_url"
        type: "string"
        description: ""

      - name: "display_login"
        type: "string"
        description: ""

      - name: "gravatar_id"
        type: "string"
        description: ""

      - name: "id"
        type: "number"
        description: ""

      - name: "login"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""

  - name: "created_at"
    type: "date-time"
    description: "The date the event was created."
  
  - name: "distinct_size"
    type: "number"
    description: "The number of distinct commits in a push."

  - name: "head"
    type: "string"
    description: "The SHA of the most recent commit on `ref` after the push."
  
  - name: "org"
    type: "object"
    description: "Information about the organization."
    subattributes:
      - name: "avatar_url"
        type: "string"
        description: ""

      - name: "gravatar_id"
        type: "string"
        description: ""

      - name: "id"
        type: "number"
        description: ""

      - name: "login"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""

  - name: "payload"
    type: "object"
    description: "Information about the events payload."
    subattributes:
      - name: "action"
        type: "string"
        description: ""

      - name: "before"
        type: "string"
        description: ""

      - name: "comment"
        type: "string"
        description: ""

      - name: "commits"
        type: "array"
        description: ""
        subattributes:
          - name: "author"
            type: "object"
            description: ""
            subattributes:
              - name: "email"
                type: "string"
                description: ""

              - name: "name"
                type: "string"
                description: ""

          - name: "distinct"
            type: "boolean"
            description: ""

          - name: "message"
            type: "string"
            description: ""

          - name: "sha"
            type: "string"
            description: ""
            foreign-key-id: "sha"

          - name: "url"
            type: "string"
            description: ""

      - name: "description"
        type: "string"
        description: ""

      - name: "issue"
        type: "string"
        description: ""

      - name: "master_branch"
        type: "string"
        description: ""

      - name: "pusher_type"
        type: "string"
        description: ""

      - name: "ref"
        type: "string"
        description: ""

      - name: "ref_type"
        type: "string"
        description: ""

  - name: "public"
    type: "boolean"
    description: "When a private repository becomes public."

  - name: "push_id"
    type: "number"
    description: "The push ID."

  - name: "ref"
    type: "string"
    description: "The full `git ref` that was pushed."

  - name: "repo"
    type: "object"
    description: "Information about the repository where the event occurred."
    subattributes:
      - name: "id"
        type: "number"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""

  - name: "_sdc_repository"
    type: "string"
    description: ""

  - name: "size"
    type: "number"
    description: "The number of commits in the push."

  - name: "type"
    type: "string"
    description: "The event type."
---