---
tap: "bing-ads"
version: "2"

name: "campaigns"
doc-link: https://docs.microsoft.com/en-us/bingads/campaign-management-service/campaign
singer-schema: 
description: |
  The `{{ table.name }}` table contains info about the campaigns in your Bing Ads account.

  [This is a **Core Object** table](#replication).

  #### Schema changes from Bing Ads v1 {#renamed-v1-columns}

  In this version of Stitch's {{ integration.display_name }} integration, the schema of this table has changed. This was done to ensure consistency between the fields in our integration and [the changes made by Microsoft to the Bing Ads API](https://docs.microsoft.com/en-us/bingads/guides/migration-guide?view=bingads-12#reporting-downloadedcolumns){:target="new}.

  - `NativeBidAdjustment` has been removed
  - `AudienceAdsBidAdjustment` has been added
  - Additional fields have been added to `BiddingScheme` and `Settings`

replication-method: "Full Table"

api-method:
  name: getCampaignsByAccountId
  doc-link: https://docs.microsoft.com/en-us/bingads/campaign-management-service/getcampaignsbyaccountid

attributes:
  - name: "Id"
    type: "integer"
    primary-key: true
    description: "The campaign ID."
    foreign-key-id: "campaign-id"

  - name: "AudienceAdsBidAdjustment"
    type: "integer"
    description: |
      The percent amount by which to adjust your bid for intent ads above or below the base ad group or keyword bid.

      Possible values are negative one hundred `(-100)` through positive nine hundred `(900)`.

  - name: "BiddingScheme"
    type: "object"
    description: "The bid strategy type for how bids are managed."
    subattributes:
      - name: "Type"
        type: "string"
        description: |
          The type of bidding scheme set for the campaign, ad group, or keyword. Refer to [Microsoft's documentation](https://docs.microsoft.com/en-us/bingads/campaign-management-service/biddingscheme?view=bingads-12#remarks){:target="new"} for info about bidding scheme types.

      - name: "InheritedBidStrategyType"
        type: "string"
        description: |
          The type of bidding scheme that is inherited from the parent campaign or ad group. Possible values are:

          - `EnhancedCpc`
          - `ManualCpc`
          - `MaxClicks`
          - `MaxConversions`
          - `TargetCpa`

  - name: "BudgetId"
    type: "integer"
    description: "The ID of the budget that the campaign shares with other campaigns in the account. Refer to [Microsoft's documentation](https://docs.microsoft.com/en-us/bingads/campaign-management-service/budget) for more info on budgets."

  - name: "BudgetType"
    type: "string"
    description: "The budget type that determines how the budget is spent."

  - name: "CampaignType"
    type: "string"
    description: "The type of campaign."

  - name: "DailyBudget"
    type: "number"
    description: "The amount to spend daily on the campaign."

  - name: "Description"
    type: "string"
    description: "The description of the campaign."

  - name: "ForwardCompatibilityMap"
    type: "array"
    description: "Details about the forward compatibility settings for the campaign."
    doc-link: https://docs.microsoft.com/en-us/bingads/customer-management-service/keyvaluepairofstringstring
    subattributes:
      - name: "keyValuePairOfStringString"
        type: "array"
        description: "Key and value pairs for the campaign's forward compatibility settings."
        subattributes:
          - name: "key"
            type: "string"
            description: "The name of the setting."

          - name: "value"
            type: "string"
            description: "The value of the setting."

  - name: "Languages"
    type: "string"
    description: "The languages of the ads and keywords in the campaign."

  - name: "Name"
    type: "string"
    description: "The name of the campaign."

  - name: "Settings"
    type: "array"
    description: |
      Details about the settings applied to the campaign.

      Only certain attributes are applicable to different campaign settings. This means that only certain columns will contain values based on the `Type` field.
    subattributes:
      - name: "Type"
        type: "string"
        description: |
          The type of setting. Possible values are:

          - `CoOpSetting`
          - `DynamicSearchAdsSetting`
          - `ShoppingSetting`

        doc-link: https://docs.microsoft.com/en-us/bingads/campaign-management-service/setting

      - name: "BidBoostValue"
        type: "number"
        description: |
          **Applicable to Cooperative Bidding campaigns,** or `Type: CoOpSetting`. The percentage that allows your cooperative bid to flex.

      - name: "BidMaxValue"
        type: "number"
        description: |
          **Applicable to Cooperative Bidding campaigns,** or `Type: CoOpSetting`. The flat amount of your cooperative bid.

      - name: "BidOption"
        type: "string"
        description: |
          **Applicable to Cooperative Bidding campaigns,** or `Type: CoOpSetting`. Determines whether or not to amplify your partner's bid.

      - name: "DomainName"
        type: "string"
        description: |
          **Applicable to Dynamic Search Ads campaigns,** or `Type: DynamicSearchAdsSetting`. The domain name of the website that you want to target for dynamic search ads.

      - name: "Language"
        type: "string"
        description: |
          **Applicable to Dynamic Search Ads campaigns,** or `Type: DynamicSearchAdsSetting`. The language of the website pages that you want to target for dynamic search ads.

      - name: "PageFeedIds"
        type: "array"
        description: |
          **Applicable to Dynamic Search Ads campaigns,** or `Type: DynamicSearchAdsSetting`. Reserved by Microsoft.
        subattributes:
          - name: "value"
            type: "integer"
            description: |
              **Applicable to Dynamic Search Ads campaigns,** or `Type: DynamicSearchAdsSetting`. Reserved by Microsoft.

      - name: "Source"
        type: "string"
        description: |
          **Applicable to Dynamic Search Ads campaigns,** or `Type: DynamicSearchAdsSetting`. Reserved by Microsoft.

      - name: "LocalInventoryAdsEnabled"
        type: "boolean"
        description: |
          **Applicable to feed-based audience or shopping campaigns,** or `Type: ShoppingSetting`. Determines whether local inventory ads are enabled for the Bing Merchant Center store.

      - name: "Priority"
        type: "integer"
        description: |
          **Applicable to feed-based audience or shopping campaigns,** or `Type: ShoppingSetting`. Determines which Bing Shopping campaign serves ads, in the event that two or more campaigns use the product catalog feed from the same Bing Merchant Center store.

          Possible value are `0`, `1`, or `2`. The higher numbers are given priority.

      - name: "SalesCountryCode"
        type: "string"
        description: |
          **Applicable to feed-based audience or shopping campaigns,** or `Type: ShoppingSetting`. The country code for the Bing Merchant Center store. Refer to [Microsoft's documentation](https://docs.microsoft.com/en-us/bingads/campaign-management-service/getbsccountries?view=bingads-12){:target="new"} for a list of possible values.

      - name: "StoreId"
        type: "integer"
        description: |
          **Applicable to feed-based audience or shopping campaigns,** or `Type: ShoppingSetting`. The ID for the Bing Merchant Center store that contains a product catalog feed that you want to use for the campaign.

  - name: "Status"
    type: "string"
    description: "The status of the campaign. Possible values are `Active` and `Paused`."

  - name: "TimeZone"
    type: "string"
    description: "The timezone where the campaign operates."

  - name: "TrackingUrlTemplate"
    type: "string"
    description: "The tracking template to use as a default for all URLs in the campaign."

  - name: "UrlCustomParameters"
    type: "string"
    description: "The custom collection of key and value parameters for URL tracking."
---