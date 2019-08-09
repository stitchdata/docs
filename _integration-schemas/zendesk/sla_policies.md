---
tap: "zendesk"
version: "1.0"

name: "sla_policies"
doc-link: https://developer.zendesk.com/rest_api/docs/support/sla_policies
singer-schema: https://github.com/singer-io/tap-zendesk/blob/master/tap_zendesk/schemas/sla_policies.json
description: |
  The `{{ table.name }}` table contains info about the Service Level Agreements (SLAs) in your {{ integration.display_name }} account. An SLA is a documented agreement between a support provider and their customers that defines performance measures for support.

  **Note**: Replicating SLA policies requires that you be on an Enterprise or Professional {{ integration.display_name }} plan, and have Admin permissions in {{ integration.display_name }}.

replication-method: "Full Table"

api-method:
  name: List SLA Policies
  doc-link: https://developer.zendesk.com/rest_api/docs/support/sla_policies#list-sla-policies

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The SLA policy ID."
    # foreign-key-id: "sla-policy-id"

  - name: "created_at"
    type: "date-time"
    description: "The time the SLA policy was created."

  - name: "description"
    type: "string"
    description: "The description of the SLA policy."

  - name: "filter"
    type: "object"
    description: "Details about the conditions that a ticket must match in order for the SLA policy to be applied to the ticket."
    subattributes:
      - name: "all"
        type: "array"
        description: "Indicates logical `AND`. Tickets must meet all of the conditions to be matched to the SLA policy."
        subattributes: &filter-attributes
          - name: "field"
            type: "string"
            description: "The name of a ticket field."
          - name: "operator"
            type: "string"
            description: "The comparison operator."
          - name: "value"
            type: "string"
            description: "The value of a ticket field."

      - name: "any"
        type: "array"
        description: "Indicates logical `OR`. Tickets must satisfy any of the conditions to be matched to the SLA policy."
        subattributes: *filter-attributes
  
  - name: "policy_metrics"
    type: "object"
    description: "Details about the metric targets for each value of the priority field in a ticket."
    subattributes:
      - name: "priority"
        type: "string"
        description: "The priority that a ticket must match. For example: `low`"

      - name: "target"
        type: "integer" 
        description: "The time in which the end-state for a metric should be met."

      - name: "business_hours"
        type: "boolean"
        description: "Indicates whether metric targets are measured in business hours or calendar hours."

      - name: "metric"
        type: "string"
        description: |
          The definition of the time that is being measured. Possible values are:

          - `agent_work_time`
          - `first_reply_time`
          - `next_reply_time`
          - `pausable_update_time`
          - `periodic_update_time`
          - `requester_wait_time`
        doc-link: "https://developer.zendesk.com/rest_api/docs/support/sla_policies#metrics"

  - name: "position"
    type: "integer"
    description: "The position of the SLA policy, which determines the order in which it is matched."

  - name: "title"
    type: "string"
    description: "The title of the SLA policy."

  - name: "updated_at"
    type: "date-time"
    description: "The time the SLA policy was last updated."

  - name: "url"
    type: "string"
    description: "The URL of the SLA policy in your Zendesk account."
---