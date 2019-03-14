---
tap: "freshdesk"
# version:

name: "satisfaction_ratings"
doc-link: https://developers.freshdesk.com/api/#satisfaction-ratings
singer-schema: https://github.com/singer-io/tap-freshdesk/blob/master/tap_freshdesk/schemas/satisfaction_ratings.json
description: |
  The `satisfaction-ratings` table contains info about customer satisfaction survey responses, or satisfaction ratings."

replication-method: "Key-based Incremental"
api-method:
  name: "viewAllSatisfactionRatings"
  doc-link: https://developers.freshdesk.com/api/#view_all_satisfaction_ratings

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the satisfaction rating."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time when the satisfaction rating was last updated."

  - name: "user_id"
    type: "integer"
    description: "The requester ID of the ticket for which the satisfaction rating has been created **or** the ID of the user who created the satisfaction rating."

  - name: "feedback"
    type: "string"
    description: "Feedback given alongisde the satisfaction rating."

  - name: "created_at"
    type: "date-time"
    description: "The time the satisfaction rating was first created."

  - name: "agent_id"
    type: "integer"
    description: "The responder ID of the ticket for which the satisfaction rating has been created."

  - name: "group_id"
    type: "integer"
    description: "The group ID associated with the ticket for which the satisfaction rating has been created."

  - name: "ticket_id"
    type: "integer"
    description: "The ID of the ticket for which the satisfaction rating has been created."

  - name: "survey_id"
    type: "integer"
    description: "The survey ID of the satisfaction rating."

  - name: "ratings"
    type: "array"
    description: "Details about the questions and responses given by the user for the survey."
    doc-link: "https://developer.freshdesk.com/api/#create_satisfaction_rating"
    subattributes:
      - name: "question"
        type: "string"
        description: "The question associated with the survey."

      - name: "value"
        type: "integer"
        description: "The value of the user's response to the survey question."
---