---
tap: "zendesk"
version: "1.0"

name: "satisfaction_ratings"
doc-link: https://developer.zendesk.com/rest_api/docs/core/satisfaction_ratings
singer-schema: https://github.com/singer-io/tap-zendesk/blob/master/tap_zendesk/schemas/satisfaction_ratings.json
description: |
  The `{{ table.name }}` table contains info about ratings users have offered on support tickets. 

  **Note**: This table is only available if satisfaction ratings are enabled in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: List satisfaction ratings
  doc-link: https://developer.zendesk.com/rest_api/docs/core/satisfaction_ratings#list-satisfaction-ratings

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The satisfaction rating ID."

  - name: "updated_at"
    type: "string"
    replication-key: true
    description: "The time the rating was last updated."

  - name: "assignee_id"
    type: "integer"
    description: "The ID of the agent assigned at the time of the rating."
    foreign-key-id: "user-id"

  - name: "created_at"
    type: "string"
    description: "The time the rating was created."

  - name: "group_id"
    type: "integer"
    description: "The ID of the group assigned at the time of the rating."
    foreign-key-id: "group-id"

  - name: "reason_id"
    type: "integer"
    description: |
      The ID of the reason the user selected for giving a negative rating. Possible values are:

      - `0` - No reason provided (user didn't select a reason from the list menu)
      - `5` - The issue took too long to resolve
      - `6` - The issue wasn't resolved
      - `7` - The agent's knowledge is unsatisfactory
      - `8` - The agent's attitude is unsatisfactory
      - `100` - Some other reason

  - name: "requester_id"
    type: "integer"
    description: "The ID of the ticket requester submitting the rating."
    foreign-key-id: "user-id"

  - name: "ticket_id"
    type: "integer"
    description: "The ID of the ticket being rated."
    foreign-key-id: "ticket-id"

  - name: "url"
    type: "string"
    description: "The API URL of the rating."

  - name: "score"
    type: "string"
    description: |
      The rating. Possible values are:

      - `offered`
      - `unoffered`
      - `good`
      - `bad`

  - name: "reason"
    type: "string"
    description: |
      **Only applicable if [satisfaction reasons](https://support.zendesk.com/hc/en-us/articles/223152967){:target="new"} are enabled.** The reason for a bad rating, given by the requester in a follow-up question.

  - name: "comment"
    type: "string"
    description: "The comment recieved with the rating, if available."
---
