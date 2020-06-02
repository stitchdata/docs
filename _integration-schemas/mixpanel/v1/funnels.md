---
tap: "mixpanel"
version: "1"
key: "funnel"

name: "funnels"
doc-link: "https://developer.mixpanel.com/docs/data-export-api#section-funnels"
singer-schema: "https://github.com/singer-io/tap-mixpanel/blob/master/tap_mixpanel/schemas/funnels.json"
description: |
  The `{{ table.name }}` table contains data about your {{ integration.display_name }} funnels, segmented by funnel and day.

replication-method: "Key-based Incremental"

api-method:
  name: "Get funnels"
  doc-link: "https://developer.mixpanel.com/docs/data-export-api#section-funnels"

attributes:
  - name: "funnel_id"
    type: "integer"
    primary-key: true
    description: "The funnel ID."
    # foreign-key-id: "funnel-id"

  - name: "date"
    type: "date"
    primary-key: true
    replication-key: true
    description: "The date the data is for."

  - name: "analysis"
    type: "object"
    description: "Performance statistics about the funnel for the given `date`."
    subattributes:
      - name: "completion"
        type: "integer"
        description: ""

      - name: "starting_amount"
        type: "integer"
        description: ""

      - name: "steps"
        type: "integer"
        description: ""

      - name: "worst"
        type: "integer"
        description: ""

  - name: "datetime"
    type: "date-time"
    description: "The date the data is for."

  - name: "name"
    type: "string"
    description: "The name of the funnel."

  - name: "steps"
    type: "array"
    description: "Performance statistics about the steps in the funnel."
    subattributes:
      - name: "count"
        type: "integer"
        description: ""

      - name: "avg_time"
        type: "number"
        description: ""

      - name: "goal"
        type: "string"
        description: ""

      - name: "overall_conv_ratio"
        type: "number"
        description: ""

      - name: "event"
        type: "string"
        description: ""

      - name: "step_label"
        type: "string"
        description: ""

      - name: "time_buckets_from_start"
        type: "object"
        description: ""
        subattributes:
          - name: "lower"
            type: "integer"
            description: ""

          - name: "higher"
            type: "integer"
            description: ""

          - name: "buckets"
            type: "array"
            description: ""
            anchor-id: 1
            subattributes:
              - name: "value"
                type: "integer"
                description: ""

      - name: "time_buckets_from_prev"
        type: "object"
        description: ""
        subattributes:
          - name: "lower"
            type: "integer"
            description: ""

          - name: "higher"
            type: "integer"
            description: ""

          - name: "buckets"
            type: "array"
            description: ""
            anchor-id: 2
            subattributes:
              - name: "value"
                type: "integer"
                description: ""
---