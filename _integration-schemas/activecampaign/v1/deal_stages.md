---
tap: "activecampaign"
version: "0.4"
key: ""

name: "deal_stages"
doc-link: "https://developers.activecampaign.com/reference#deal-stages"
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/deal_stages.json"
description: |
  The `{{ table.name }}` table contains information about grouped deals within a pipeline in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List all stages"
    doc-link: "https://developers.activecampaign.com/reference#list-all-deal-stages"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The stage ID."
    foreign-key-id: "stage-id"

  - name: "udate"
    type: "date-time"
    description: "The stage udate."
    replication-key: true

  - name: "card_region1"
    type: "string"
    description: ""
  - name: "card_region2"
    type: "string"
    description: ""
  - name: "card_region3"
    type: "string"
    description: ""
  - name: "card_region4"
    type: "string"
    description: ""
  - name: "card_region5"
    type: "string"
    description: ""
  - name: "cdate"
    type: "date-time"
    description: ""
  - name: "color"
    type: "string"
    description: ""
  - name: "deal_order"
    type: "string"
    description: ""
  - name: "group"
    type: "integer"
    description: "The pipeline ID."
    foreign-key-id: "pipeline-id"
  
  - name: "order"
    type: "integer"
    description: "The order ID."
    foreign-key-id: "order-id"
  - name: "title"
    type: "string"
    description: ""

  - name: "width"
    type: "integer"
    description: ""
---
