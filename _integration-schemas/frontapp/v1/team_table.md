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
    description: "The team member's previous average first reaction time."

  - name: "avg_first_reaction_time_v"
    type: "number"
    description: "The team member's current average first reaction time."

  - name: "avg_message_conversations_p"
    type: "number"
    description: "The team member's previous average number of message conversations."

  - name: "avg_message_conversations_v"
    type: "number"
    description: "The team member's current average number of message conversations."

  - name: "avg_reaction_time_p"
    type: "number"
    description: "The team member's previous average reaction time."

  - name: "avg_reaction_time_v"
    type: "number"
    description: "The team member's current average reaction time."

  - name: "num_composed_p"
    type: "integer"
    description: "The team member's previous number of composed messages."

  - name: "num_composed_v"
    type: "integer"
    description: "The team member's current number of composed messages."

  - name: "num_conversations_p"
    type: "integer"
    description: "The team member's previous number of conversations."

  - name: "num_conversations_v"
    type: "integer"
    description: "The team member's current number of conversations."

  - name: "num_messages_p"
    type: "integer"
    description: "The team member's previous number of messages."

  - name: "num_messages_v"
    type: "integer"
    description: "The team member's current number of messages."

  - name: "num_replied_p"
    type: "integer"
    description: "The team member's previous number of replies."

  - name: "num_replied_v"
    type: "integer"
    description: "The team member's current number of replies."

  - name: "num_sent_p"
    type: "integer"
    description: "The team member's previous number of sent messages."

  - name: "num_sent_v"
    type: "integer"
    description: "The team member's current number of sent messages."

  - name: "teammate_p"
    type: "string"
    description: ""

  - name: "teammate_url"
    type: "string"
    description: "The team member's URL in {{ integration.display_name }}."
---