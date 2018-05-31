---
tap: "github"
# version: ""

name: "reviews"
doc-link: https://developer.github.com/v3/pulls/reviews/
singer-schema: https://github.com/singer-io/tap-github/blob/master/tap_github/reviews.json
description: |
  The `reviews` table contains info about pull request reviews. A pull request review is a group of comments on a pull request.

replication-method: "Full Table"

api-method:
  name: "listReviewsOnPullRequest"
  doc-link: https://developer.github.com/v3/pulls/reviews/#list-reviews-on-a-pull-request

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The review ID."

  - name: "body"
    type: "string"
    description: "The description of the review."

  - name: "commit_id"
    type: "string"
    description: "The ID of the commit the review was performed on."
    foreign-key: true

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
    object-attributes:
      - name: "id"
        type: "integer"
        description: "The user ID."

      - name: "login"
        type: "string"
        description: "The user's GitHub username."
---
