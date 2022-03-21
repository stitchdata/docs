---
tap: "google-ads"
version: "1"

name: "ad_groups"
doc-link: https://developers.google.com/google-ads/api/reference/rpc/v9/AdGroupService
singer-schema: https://github.com/singer-io/tap-google-ads/blob/main/tap_google_ads/schemas/ad_groups.json
description: |
  The `{{ table.name }}` table contains detailed info about your ad groups.

  [This is a **Core Object** table](#replication).
notes:

replication-method: "Full Table"
attribution-window: true

attributes:
  - name: "adRotationMode"
    type: "string"
    description: ""

  - name: "baseAdGroup"
    type: "string"
    description: ""

  - name: "campaign"
    type: "string"
    description: ""

  - name: "cpcBidMicros"
    type: "integer"
    description: ""

  - name: "cpmBidMicros"
    type: "integer"
    description: ""

  - name: "cpvBidMicros"
    type: "integer"
    description: ""

  - name: "displayCustomBidDimension"
    type: "string"
    description: ""

  - name: "effectiveTargetCpaMicros"
    type: "integer"
    description: ""

  - name: "effectiveTargetCpaSource"
    type: "string"
    description: ""

  - name: "effectiveTargetRoas"
    type: "string"
    description: ""

  - name: "effectiveTargetRoasSource"
    type: "string"
    description: ""

  - name: "excludedParentAssetFieldTypes"
    type: "array"
    description: ""
    subattributes:
      - name: "items"
        type: "string"
        description: ""

  - name: "explorerAutoOptimizerSetting"
    type: "object"
    description: ""
    subattributes:
      - name: "optIn"
        type: "boolean"
        description: ""

  - name: "finalUrlSuffix"
    type: "string"
    description: ""

  - name: "id"
    type: "integer"
    description: ""
    foreign-key-id: "ad_group_id"
    primary-key: true

  - name: "labels"
    type: "array"
    description: ""
    subattributes:
      - name: "items"
        type: "string"
        description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "percentCpcBidMicros"
    type: "integer"
    description: ""

  - name: "resourceName"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "targetCpaMicros"
    type: "integer"
    description: ""

  - name: "targetCpmMicros"
    type: "integer"
    description: ""

  - name: "targetRoas"
    type: "string"
    description: ""

  - name: "targetingSetting"
    type: "object"
    description: ""
    subattributes:
      - name: "targetRestrictionOperations"
        type: "array"
        description: ""
        subattributes:
          - name: "operator"
            type: "string"
            description: ""

          - name: "targetRestriction"
            type: "object"
            description: ""
            subattributes:
              - name: "bidOnly"
                type: "boolean"
                description: ""
                
              - name: "targetingDimension"
                type: "string"
                description: ""
        
      - name: "targetRestrictions"
        type: "array"
        description: ""
          subattributes:
            - name: "items"
              type: "object"
              description: ""
              subattributes:
                - name: "bidOnly"
                  type: "boolean"
                  description: ""
                  
                - name: "targetingDimension"
                  type: "string"
                  description: ""

  - name: "trackingUrlTemplate"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "urlCustomParameters"
    type: "array"
    description: ""
    subattributes:
      - name: "items"
        type: "object"
        description: ""
          subattributes:
            - name: "key"
              type: "string"
              description: ""
              
            - name: "value"
              type: "string"
              description: ""
---