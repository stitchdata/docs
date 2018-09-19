---
tap: "google-adwords"
version: "1.0"

name: "ad_groups"
doc-link: https://developers.google.com/adwords/api/docs/reference/v201806/AdGroupService.AdGroup
singer-schema: https://github.com/singer-io/tap-adwords/blob/master/tap_adwords/schemas/ad_groups.json
description: |
  The `ad_groups` table contains detailed info about your ad groups.

  [This is a **Core Object** table](#replication).
notes:

replication-method: "Full Table"
attribution-window: true

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    alias: "adGroupId"
    description: "The ID of the ad group."

  - name: "adGroupType"
    type: "string"
    description: "The type of the ad group."
    doc-link: https://developers.google.com/adwords/api/docs/reference/v201806/AdGroupService.AdGroupType

  - name: "baseAdGroupId"
    type: "integer"
    description: "The ID of the base ad group from which the draft/trial ad group was created. This field will be `NULL` if the ad group was created in the draft or trial and has no corresponding base ad group."

  - name: "baseCampaignId"
    type: "integer"
    description: "The ID of the base campaign from which the draft/trial ad group was created."

  - name: "biddingStrategyConfiguration"
    type: "object"
    inclusion: "automatic"
    description: ""
    object-attributes:
      - name: "bidSource"
        type: "string"
        description: "Indicates where the bidding strategy is associated i.e. campaign, ad group, or ad group criterion."

      - name: "BidsType"
        type: "string"
        description: "The type of bidding strategy to be attached."

      - name: "bids"
        type: "array"
        description: "Value details associated with bids."
        array-attributes:
          - name: "bid"
            type: "object"
            description: "Value details associated with bids."
            object-attributes: 
              - name: "ComparableValue.Type"
                type: "string"
                description: "Indicates that this instance is a subtype of ComparableValue."
                doc-link: https://developers.google.com/adwords/api/docs/reference/v201806/AdGroupService.Money

              - name: "microAmount"
                type: "integer"
                description: "The bid amount in micros. One million is equivalent to one unit."

  - name: "campaignId"
    type: "integer"
    description: "The ID of the campaign associated with the ad group."

  - name: "campaignName"
    type: "string"
    description: "The name of the campaign associated with the ad group."

  - name: "customerId"
    type: "integer"
    description: "The ID of the AdWords account that the record belongs to."

  - name: "labels"
    type: "array"
    description: "Details about the labels applied to the ad."
    array-attributes:
      - name: "id"
        type: "integer"
        primary-key: true
        description: "The ID of the label applied to the ad."

      - name: "name"
        type: "string"
        description: "The name of the label applied to the ad."

      - name: "status"
        type: "string"
        description: "The status of the label applied to the ad."

      - name: "attribute"
        type: "object"
        object-attributes:
          - name: "backgroundColor"
            type: "string"
            description: "The background color of the label in RGB format."

  - name: "name"
    type: "string"
    description: "The name of the ad group."

  - name: "status"
    type: "string"
    description: "The status of the ad group."

  - name: "settings"
    type: "array"
    description: "Details about the settings defined for the ad group."
    array-attributes:
      - name: "optIn"
        type: "integer"
        description: "Indicates the Opt In setting for the Display Campaign Optimizer."

      - name: "Setting.Type"
        type: "string"
        description: "Indicates that this instance is a subtype of Setting."

      - name: "details"
        type: "array"
        description: "Contains details about the settings applied to the ad group, including the target and criterion group settings."
        array-attributes:
          - name: "targetAll"
            type: "integer"
            description: "Indicates if criteria of this type can be used to modify bidding but not restrict targeting of ads."
            doc-link: https://developers.google.com/adwords/api/docs/reference/v201806/AdGroupService.TargetingSettingDetail

          - name: "criterionTypeGroup"
            type: "string"
            description: "The criterion group that the settings apply to."
---