---
tap: "pepperjam"
version: "1"
key: "creative_promotion"

name: "creative_promotion"
doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#CreativePromotion"
singer-schema: "https://github.com/singer-io/tap-pepperjam/blob/master/tap_pepperjam/schemas/creative_promotion.json"
description: |
  The `{{ table.name }}` table contains information about promotion creatives in your {{ integration.display_name }} name account.

replication-method: "Full Table"

api-method:
  name: "getPromotionCreative"
  doc-link: "https://support.pepperjam.com/s/advertiser-api-documentation#CreativePromotion"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The promotion ID."
    foreign-key-id: "promotion-id"

  - name: "name"
    type: "string"
    description: ""
---