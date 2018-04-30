---
tap-reference: "facebook-ads"

foreign-keys:
  - attribute: "adset_id"
    table: "adsets"
    join-on: "id"

  - attribute: "campaign_id"
    table: "campaigns"
    join-on: "id"

  - attribute: "ad_id"
    table: "ads"
    join-on: "id"

  - attribute: "creative_id"
    table: "adcreative"
    join-on: "id"
---