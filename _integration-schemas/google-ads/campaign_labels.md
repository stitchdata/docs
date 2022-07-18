---
tap: "google-ads"
version: "1"
name: "campaign_labels"
doc-link: https://developers.google.com/google-ads/api/reference/rpc/v10/CampaignLabel
description: |
  The `{{ table.name }}` table contains info about the relationship between campaigns and labels

  [This is a **Core Object** table](#replication).

replication-method: "Full Table"
attribution-window: true

attributes:
  - name: "resource_name"
    type: "string"
    description: ""
    primary-key: true

  - name: "campaign"
    type: "string"
    description: ""

  - name: "label"
    type: "string"
    description: ""

---