---
tap: "google-ads"
version: "1"

name: "accounts"
doc-link: https://developers.google.com/google-ads/api/reference/rpc/v9/CustomerService
singer-schema: https://github.com/singer-io/tap-google-ads/blob/main/tap_google_ads/schemas/accounts.json
description: |
  The `{{ table.name }}` table contains high-level info about the Google Ads account(s) you’ve connected to Stitch.

  [This is a **Core Object** table](#replication).

replication-method: "Full Table"
attribution-window: true

attributes:
  - name: "autoTaggingEnabled"
    type: "boolean"
    description: ""

  - name: "callReportingSetting"
    type: "object"
    description: ""
    subattributes:
      - name: "callConversionAction"
        type: "string"
        description: ""

      - name: "callConversionReportingEnabled"
        type: "boolean"
        description: ""

      - name: "callReportingEnabled"
        type: "boolean"
        description: ""

  - name: "conversionTrackingSetting"
    type: "object"
    description: ""
    subattributes:
      - name: "conversionTrackingId"
        type: "integer"
        description: ""
        
      - name: "crossAccountConversionTrackingId"
        type: "integer"
        description: ""

  - name: "currencyCode"
    type: "string"
    description: ""

  - name: "descriptiveName"
    type: "string"
    description: ""

  - name: "finalUrlSuffix"
    type: "string"
    description: ""

  - name: "hasPartnersBadge"
    type: "boolean"
    description: ""

  - name: "id"
    type: "integer"
    description: ""
    primary-key: true
    foreign-key-id: "customer_id"

  - name: "manager"
    type: "boolean"
    description: ""

  - name: "optimizationScore"
    type: "string"
    description: ""

  - name: "optimizationScoreWeight"
    type: "string"
    description: ""

  - name: "payPerConversionEligibilityFailureReasons"
    type: "array"
    description: ""
    subattributes:
      - name: "items"
        type: "string"
        description: ""

  - name: "remarketingSetting"
    type: "object"
    description: ""
    subattributes:
      - name: "googleGlobalSiteTag"
        type: "string"
        description: ""

  - name: "resourceName"
    type: "string"
    description: ""

  - name: "testAccount"
    type: "boolean"
    description: ""

  - name: "timeZone"
    type: "string"
    description: ""

  - name: "trackingUrlTemplate"
    type: "string"
    description: ""
---