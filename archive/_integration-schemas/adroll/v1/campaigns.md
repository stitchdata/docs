---
tap: "adroll"
version: "1"
key: "campaign"

name: "campaigns"
doc-link: "https://developers.nextroll.com/docs/crud-api/reference.html#get--api-v1-campaign-get"
singer-schema: "https://github.com/singer-io/tap-adroll/blob/master/tap_adroll/schemas/campaigns.json"
description: |
  The `{{ table.name }}` table contains information about the advertising campaigns in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "Get advertisable campaigns"
  doc-link: "https://developers.nextroll.com/docs/crud-api/reference.html#get--api-v1-advertisable-get_campaigns"

attributes:
  - name: "eid"
    type: "string"
    primary-key: true
    description: "The campaign EID."
    # foreign-key-id: "campaign-id"

  - name: "abm_type"
    type: "string"
    description: ""

  - name: "adgroups"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""
        foreign-key-id: "adgroup-id"

  - name: "advertisable"
    type: "string"
    description: ""
    foreign-key-id: "advertisable-id"

  - name: "bid_strategy"
    type: "string"
    description: ""

  - name: "bid_strategy_target"
    type: "string"
    description: ""

  - name: "bid_type"
    type: "string"
    description: ""

  - name: "budget"
    type: "number"
    description: ""

  - name: "campaign_type"
    type: "string"
    description: ""

  - name: "cpc"
    type: "number"
    description: ""

  - name: "cpm"
    type: "number"
    description: ""

  - name: "created_date"
    type: "date-time"
    description: ""
  
  - name: "end_date"
    type: "date-time"
    description: ""

  - name: "facebook_campaign_objective"
    type: "string"
    description: ""

  - name: "frequency_cap"
    type: "string"
    description: ""

  - name: "is_active"
    type: "boolean"
    description: ""

  - name: "is_apple"
    type: "boolean"
    description: ""

  - name: "is_cats4gold"
    type: "boolean"
    description: ""

  - name: "is_coop"
    type: "boolean"
    description: ""

  - name: "is_facebook"
    type: "boolean"
    description: ""

  - name: "is_fb_lookalike"
    type: "boolean"
    description: ""

  - name: "is_fb_wca"
    type: "boolean"
    description: ""

  - name: "is_fbx_newsfeed"
    type: "boolean"
    description: ""

  - name: "is_pubgraph"
    type: "boolean"
    description: ""

  - name: "is_retargeting"
    type: "boolean"
    description: ""

  - name: "is_rtb"
    type: "boolean"
    description: ""

  - name: "max_cpm"
    type: "number"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "pa_sales_stage_eid"
    type: "string"
    description: ""

  - name: "pricing_strategies"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "source"
    type: "string"
    description: ""

  - name: "spend_limit_until"
    type: "string"
    description: ""

  - name: "start_date"
    type: "date-time"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "ui_budget_daily"
    type: "boolean"
    description: ""

  - name: "updated_date"
    type: "date-time"
    description: ""

  - name: "use_case"
    type: "string"
    description: ""
---