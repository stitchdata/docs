---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "github"
version: "1"
key: "review"

name: "reviews"
doc-link: https://developer.github.com/v3/pulls/reviews/
singer-schema: https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/reviews.json
description: |
  The `{{ table.name }}` table contains info about pull request reviews in the repositories specified for the integration. A pull request review is a group of comments on a pull request.


# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "List reviews for a pull request"
  doc-link: "https://docs.github.com/en/rest/reference/pulls#list-reviews-for-a-pull-request"

replication-method: "Key-based Incremental"
replication-key:
  name: "since"
  based-on: "updated_at"
  tooltip: "This is a query parameter used to extract new/updated data from GitHub. It will not be included in the table's fields."

dependent-table-key: "pull-request"


# -------------------------- #
#       Table Attributes     #
# -------------------------- #

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The review ID."
    # foreign-key-id: "review-id"

  - name: "body"
    type: "string"
    description: "The description of the review."

  - name: "commit_id"
    type: "string"
    description: "The ID of the commit the review was performed on."
    foreign-key-id: "commit-id"

  - name: "html_url"
    type: "string"
    description: "The HTML URL to the review."

  - name: "pull_request_url"
    type: "string"
    description: "The URL to the pull request being reviewed."

  - name: "state"
    type: "string"
    description: |
      The state of the review. Possible values are:

      - `APPROVED`
      - `PENDING`
      - `CHANGES_REQUESTED`

  - name: "submitted_at"
    type: "date-time"
    description: ""

  - name: "user"
    type: "object"
    description: "Details about the user who submitted the review."
    subattributes:
      - name: "id"
        type: "integer"
        description: "The user ID."
        foreign-key-id: "collaborator-id"

      - name: "login"
        type: "string"
        description: "The user's GitHub username."
---