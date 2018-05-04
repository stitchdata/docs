---
tap-reference: "bing-ads"

# version: "1.0"

foreign-keys:
  - attribute: "accountId"
    table: "accounts"
    join-on: "id"

  - attribute: "ad"
    table: "ads"
    join-on: "id"

  - attribute: "adGroupId"
    table: "ad_groups"
    join-on: "id"

  - attribute: "campaignId"
    table: "campaigns"
    join-on: "id"

---