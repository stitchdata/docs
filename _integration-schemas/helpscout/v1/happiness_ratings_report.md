---
tap: "helpscout"
version: "1"
key: ""

name: "happiness_ratings_report"
doc-link: https://developer.helpscout.com/mailbox-api/endpoints/reports/happiness/reports-happiness-ratings/
singer-schema: https://github.com/singer-io/tap-helpscout/tree/master/tap_helpscout/schemas/happiness_ratings_report.json
description: "The happiness ratings report provides a company’s ratings for a specified time range."

replication-method: "Full Table"

table-key-properties: "rating_customer_id, conversation_id, rating_created_at"
valid-replication-keys: ""

attributes:
  - name: "conversation_id"
    type: "integer"
    description: "Conversation ID"
    primary-key: true

  - name: "rating_comments"
    type: "string"
    description: "Rating Comments from customer"

  - name: "rating_created_at"
    type: "date-time"
    description: "Date of creation of rating"
    primary-key: true

  - name: "rating_customer_id"
    type: "integer"
    description: "ID of the custimer who gave the rating"
    primary-key: true

  - name: "rating_customer_name"
    type: "string"
    description: "Name of the custimer who gave the rating"

  - name: "rating_id"
    type: "integer"
    description: "Rating ID. Possible values are 1,2,3  1: Great, 2: Ok, 3: Not Good"

  - name: "rating_user_id"
    type: "integer"
    description: "ID of the user who got the rating"

  - name: "rating_user_name"
    type: "string"
    description: "Name of the user who got the rating"

  - name: "thread_created_at"
    type: "date-time"
    description: "Date of creation of conversation thread"

  - name: "thread_id"
    type: "integer"
    description: "Converstaion thread ID"

  - name: "type"
    type: "string"
    description: "Rating given via. Example: email, chat etc.."
---