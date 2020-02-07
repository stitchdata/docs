---
tap-reference: "taboola"

version: "1"

foreign-keys: 
  - id: "campaign-id"
    attribute: "campaign_id"
    table: "campaign"
    all-foreign-keys:
      - table: "campaign"
        join-on: "id"
      - table: "campaign_performance"
---