---
tap: "github"
# version: ""

name: "reviews"
doc-link: https://developer.github.com/v3/pulls/reviews/
singer-schema: https://github.com/singer-io/tap-github/blob/master/tap_github/reviews.json
description: |
  The `reviews` table contains info about

replication-method: "Full Table"
api-method:
  name: "listReviewsOnPullRequest"
  doc-link: https://developer.github.com/v3/pulls/reviews/#list-reviews-on-a-pull-request

attributes:
  - name: "id"
    type: "integer"
    description: ""

  - name: "user"
    type: "object"
    description: ""
    object-attributes:
    - name: "login"
      type: "string"
      description: ""

    - name: "id"
      type: "integer"
      description: ""

  - name: "body"
    type: "string"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "commit_id"
    type: "string"
    description: ""

  - name: "html_url"
    type: "string"
    description: ""

  - name: "pull_request_url"
    type: "string"
    description: ""
---
