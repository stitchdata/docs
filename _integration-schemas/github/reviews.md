---
tap: "github"
version: "1"

name: "reviews"
doc-link: https://developer.github.com/v3/pulls/reviews/
singer-schema: https://github.com/singer-io/tap-github/blob/master/tap_github/reviews.json
description: |
  The `reviews` table contains info about pull request reviews. A pull request review is a group of comments on a pull request.

    **Note**: In order to replicate this table, you must also set the [`pull_requests`](#pull_requests) table to replicate.

replication-method: "Full Table"

api-method:
  name: "listReviewsOnPullRequest"
  doc-link: https://developer.github.com/v3/pulls/reviews/#list-reviews-on-a-pull-request

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