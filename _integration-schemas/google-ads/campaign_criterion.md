---
tap: "google-ads"
version: "1"
name: "campaign_criterion"
doc-link: https://developers.google.com/google-ads/api/reference/rpc/v10/CampaignCriterion
description: |
  The `{{ table.name }}` table contains info about campaign criteria.

  [This is a **Core Object** table](#replication).

replication-method: "Full Table"
attribution-window: true

attributes:
  - name: "customer_id"
    type: "integer"
    description: ""

  - name: "campaign_id"
    type: "integer"
    description: ""
    primary_key: true

  - name: "resource_name"
    type: "string"
    description: ""

  - name: "display_name"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "campaign"
    type: "string"
    description: ""

  - name: "criterion_id"
    type: "integer"
    description: ""
    primary-key: true

  - name: "bid_modifier"
    type: "float"
    description: ""

  - name: "negative"
    type: "boolean"
    description: ""

  - name: "criterion"
    type: "object"
    description: "The ad group criterion. It is one of the objects listed under criterion in the [Google Ads API documentation](https://developers.google.com/google-ads/api/reference/rpc/v10/CampaignCriterion#criterion)."

---