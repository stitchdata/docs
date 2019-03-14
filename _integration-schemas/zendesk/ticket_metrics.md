---
tap: "zendesk"
version: "1.0"

name: "ticket_metrics"
doc-link: https://developer.zendesk.com/rest_api/docs/core/ticket_metrics
singer-schema: https://github.com/singer-io/tap-zendesk/blob/master/tap_zendesk/schemas/ticket_metrics.json
description: |
  The `ticket_metrics` table contains info about the metrics associated with Zendesk tickets. **Note**: This table will not include records for deleted tickets.

  **Note**: Retrieving ticket metric data requires Zendesk Admin permissions.

  #### Deleted ticket metrics
  As Zendesk's API doesn't currently support returning metrics for deleted tickets, this table will not contain any metrics for deleted tickets.

  If you believe you're missing records, check in your Zendesk account to see if the missing records are for deleted tickets.
  
  For more info on how Zendesk handles deleting tickets, [refer to their documentation](https://support.zendesk.com/hc/en-us/articles/203690936).

replication-method: "Key-based Incremental"

api-method:
  name: List ticket metrics
  doc-link: https://developer.zendesk.com/rest_api/docs/core/ticket_metrics#list-ticket-metrics

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ticket metric ID."
    # foreign-key-id: "ticket-metric"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The last time the ticket metric was updated."

  # - name: "metric"
  #   type: "string"
  #   description: ""

  # - name: "time"
  #   type: "string"
  #   description: ""

  # - name: "instance_id"
  #   type: "integer"
  #   description: ""

  - name: "ticket_id"
    type: "integer"
    description: "The ID of the associated ticket."
    foreign-key-id: "ticket-id"

  # - name: "status"
  #   type: "object"
  #   description: "The number of minutes  inside and outside of business hours."
  #   subattributes: 
  #     - name: "calendar"
  #       type: "integer"
  #       description:

  #     - name: "business"
  #       type: "integer"
  #       description: "The 

  # - name: "type"
  #   type: "string"
  #   description: ""

  - name: "agent_wait_time_in_minutes"
    type: "object"
    description: "The number of minutes the agent spent waiting inside and outside of business hours."
    subattributes:
      - name: "calendar"
        type: "integer"
        description: "The number of minutes the agent spent waiting outside of business hours."

      - name: "business"
        type: "integer"
        description: "The number of minutes the agent spent waiting inside of business hours."

  - name: "assignee_stations"
    type: "integer"
    description: "The number of assignees the ticket had."

  - name: "created_at"
    type: "date-time"
    description: "The time the ticket metric was created."

  - name: "first_resolution_time_in_minutes"
    type: "object"
    description: "The number of minutes to the first resolution time inside and outside of business hours."
    subattributes:
      - name: "calendar"
        type: "integer"
        description: "The number of minutes to the first resolution time outside of business hours."

      - name: "business"
        type: "integer"
        description: "The number of minutes to the first resolution time inside of business hours."

  - name: "full_resolution_time_in_minutes"
    type: "object"
    description: "The number of minutes to the full resolution inside and outside of business hours."
    subattributes:

  - name: "group_stations"
    type: "integer"
    description: "The number of groups the ticket passed through."

  - name: "latest_comment_added_at"
    type: "date-time"
    description: "The time the last comment was added to the ticket."

  - name: "on_hold_time_in_minutes"
    type: "object"
    description: "The number of minutes the ticket was on hold inside and outside of business hours."
    subattributes:
      - name: "calendar"
        type: "integer"
        description: "The number of minutes the ticket was on hold outside of business hours."

      - name: "business"
        type: "integer"
        description: "The number of minutes the ticket was on hold inside of business hours."

  - name: "reopens"
    type: "integer"
    description: "The total number of times the ticket was reopened."

  - name: "replies"
    type: "integer"
    description: "The total number of times the ticket was replied to."

  - name: "reply_time_in_minutes"
    type: "object"
    description: "The number of minutes to the first reply inside and outside of business hours."

  - name: "requester_updated_at"
    type: "date-time"
    description: "The time the requester last updated the ticket."

  - name: "requester_wait_time_in_minutes"
    type: "object"
    description: "The number of minutes the requester spent waiting inside and outside of business hours."
    subattributes:
      - name: "calendar"
        type: "integer"
        description: "The number of minutes the requester spent waiting outside of business hours."

      - name: "business"
        type: "integer"
        description: "The number of minutes the requester spent waiting inside of business hours."

  - name: "reply_time_in_minutes"
    type: "object"
    description: "Number of minutes to the first reply inside and out of business hours."
    subattributes:
      - name: "calendar"
        type: "integer"
        description: "The number of minutes to the first reply outside of business hours."

      - name: "business"
        type: "integer"
        description: "The number of minutes to the first reply inside of business hours."

  - name: "full_resolution_time_in_minutes"
    type: "object"
    description: "Number of minutes to the full resolution inside and out of business hours."
    subattributes:
      - name: "calendar"
        type: "integer"
        description: "The number of minutes to the full resolution outside of business hours."

      - name: "business"
        type: "integer"
        description: "The number of minutes to the full resolution inside of business hours."

  - name: "status_updated_at"
    type: "date-time"
    description: "The time the ticket's status was last updated."

  - name: "url"
    type: "string"
    description: "The API URL of the ticket metric."

  - name: "initially_assigned_at"
    type: "date-time"
    description: "The time the ticket was initially assigned."

  - name: "assigned_at"
    type: "date-time"
    description: "The time the ticket was last assigned."

  - name: "solved_at"
    type: "date-time"
    description: "The time the ticket was solved."

  - name: "assignee_updated_at"
    type: "date-time"
    description: "The time the assignee last updated the ticket."
---
