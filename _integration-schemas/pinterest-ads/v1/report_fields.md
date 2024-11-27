---
tap: "pinterest-ads"
version: "1"
key: "report-field"

name: "report_fields"
doc-link: "https://developers.pinterest.com/docs/redoc/adsreporting/#tag/reports"
singer-schema: "https://github.com/singer-io/tap-pinterest-ads/blob/master/tap_pinterest_ads/schemas/report_fields.json"
description: |
  The `{{ table.name }}` table contains information about report field definitions.

replication-method: "Full Table"

api-method:
  name: "Get async advertiser delivery metrics report"
  doc-link: "https://developers.pinterest.com/docs/redoc/adsreporting/#tag/reports"

attributes:
  - name: "definition"
    type: "string"
    description: "The definition of the field."
    
  - name: "name"
    type: "string"
    primary-key: true
    description: "The field name."
---
