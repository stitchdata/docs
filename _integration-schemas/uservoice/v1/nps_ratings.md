---
tap: "uservoice"
# version: "1.0"

name: "nps_ratings"
doc-link: https://developer.uservoice.com/docs/api/v2/reference/#/
singer-schema: https://github.com/singer-io/tap-uservoice/blob/master/tap_uservoice/streams/nps_ratings.py
description: |
  The `{{ table.name }}` table contains info about NPS, or Net Promoter Scores. NPS is used to measure customer satisfaction on a scale from 0-10.

replication-method: "Key-based Incremental"

api-method:
  name: List NPS ratings
  doc-link: https://developer.uservoice.com/docs/api/v2/reference/#list-nps-ratings

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The NPS rating ID."
    #foreign-key-id: "nps-rating-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the NPS rating was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the NPS rating was created."

  - name: "rating"
    type: "integer"
    description: "The NPS score, which is a number from 0 to 10."

  - name: "previous_rating"
    type: "integer"
    description: "If applicable, the previous rating value."

  - name: "rating_delta"
    type: "integer"
    description: "The delta between `rating` and `previous_rating`."

  - name: "body"
    type: "string"
    description: "If applicable, the comment left by the user filling out the survey."

  - name: "prompt"
    type: "string"
    description: |
      The prompt that displays to users during the survey. It is a variation of _"How likely is it that you would recommend [our product/service] to a friend or colleague?_"

  - name: "group"
    type: "string"
    description: "The group the user's rating falls into. For example: `neutral`"

  - name: "links"
    type: "object"
    description: "Details about the origins of the NPS rating."
    object-attributes: 
      - name: "user"
        type: "integer"
        description: "The ID of the user who submitted the NPS rating."
        foreign-key-id: "user-id"

      - name: "ticket"
        type: "integer"
        description: "The ID of the ticket associated with the NPS rating."
---