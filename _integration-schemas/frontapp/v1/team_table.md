---
tap: "frontapp"
version: "1.0"

name: "team_table"
doc-link: "https://dev.frontapp.com/#analytics"
singer-schema: "https://github.com/singer-io/tap-frontapp/blob/master/tap_frontapp/schemas/team_table.json"
description: |
  The `{{ table.name }}` table contains a list of team member statistics since the last completed replication job through the most recent iteration of the defined [**Incremental Range**](#add-stitch-data-source) (daqy or hour).

  This table will include team members from all teams in your {{ integration.display_name }} account.

  **Note**: During the historical replication job, all increments since the **Start Date** will be replicated. This will result in the first record for this table being an aggregated record across all team members.

replication-method: "Key-based Incremental"

api-method:
    name: "Get analytics"
    doc-link: "https://dev.frontapp.com/#get-analytics"

attributes:
  - name: "analytics_range"
    type: "string"
    primary-key: true
    description: "The range the analytics pertain to."

  - name: "teammate_v"
    type: "string"
    primary-key: true
    description: "The team member's ID."
    # foreign-key-id: "teammate-id"

  - name: "teammate_id"
    type: "integer"
    description: ""

  - name: "analytics_date"
    type: "date"
    primary-key: true
    replication-key: true
    description: "The date the analytics pertain to."

  - name: "avg_first_reaction_time_p"
    type: "number"
    description: "The team member's average first reaction time for the previous period."

  - name: "avg_first_reaction_time_v"
    type: "number"
    description: "The team member's average first reaction time for the current period."

  - name: "avg_message_conversations_p"
    type: "number"
    description: "The team member's average number of message conversations for the previous period."

  - name: "avg_message_conversations_v"
    type: "number"
    description: "The team member's average number of message conversations for the current period."

  - name: "avg_reaction_time_p"
    type: "number"
    description: "The team member's average reaction time for the previous period."

  - name: "avg_reaction_time_v"
    type: "number"
    description: "The team member's average reaction time for the current period."

  - name: "num_composed_p"
    type: "integer"
    description: "The team member's number of composed messages for the previous period."

  - name: "num_composed_v"
    type: "integer"
    description: "The team member's number of composed messages for the current period."

  - name: "num_conversations_p"
    type: "integer"
    description: "The team member's number of conversations for the previous period."

  - name: "num_conversations_v"
    type: "integer"
    description: "The team member's number of conversations for the current period."

  - name: "num_messages_p"
    type: "integer"
    description: "The team member's number of messages for the previous period."

  - name: "num_messages_v"
    type: "integer"
    description: "The team member's number of messages for the current period."

  - name: "num_replied_p"
    type: "integer"
    description: "The team member's number of replies for the previous period."

  - name: "num_replied_v"
    type: "integer"
    description: "The team member's number of replies for the current period."

  - name: "num_sent_p"
    type: "integer"
    description: "The team member's number of sent messages for the previous period."

  - name: "num_sent_v"
    type: "integer"
    description: "The team member's number of sent messages for the current period."

  - name: "teammate_p"
    type: "string"
    description: ""

  - name: "teammate_url"
    type: "string"
    description: "The team member's URL in {{ integration.display_name }}."
---