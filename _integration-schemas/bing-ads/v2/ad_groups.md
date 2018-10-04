---
tap: "bing-ads"
# version: "2.0"

name: "ad_groups"
doc-link: https://docs.microsoft.com/en-us/bingads/campaign-management-service/adgroup
singer-schema: 
description: |
  The `ad_groups` table contains info about the ad groups associated with the campaigns in your Bing Ads account.

  [This is a **Core Object** table](#replication).

replication-method: "Full Table"

api-method:
  name: getAdGroupsbyCampaignId
  doc-link: https://docs.microsoft.com/en-us/bingads/campaign-management-service/getadgroupsbycampaignid

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ad group ID."
    foreign-key-id: "ad-group-id"

  - name: "adDistribution"
    type: "string"
    description: "Determines whether the ads within the ad group will be displayed on the content distribution channel, search distribution channel, or both."

  - name: "adRotation"
    type: "string"
    description: |
      Determines how often ads in the ad group show in relation to each other. If there are multiple ads within an ad group, the ads will rotate because only one ad from your account can show at a time.

      Possible values are:

      - `OptimizeForClicks` - In this rotation, Bing Ads will predominantly show ads that have the highest click-through rate, or CTR.
      - `RotateAdsEvenly` - In this rotation, Bing ads will rotate between ads on an equal basis.

  - name: "biddingScheme"
    type: "string"
    description: "The bid strategy type for how bids are managed."

  - name: "contentMatchBid"
    type: "number"
    description: "The bid to use when the keywords that the service extracts from the content page and the ad group's keywords match by using an exact match comparison."

  - name: "endDate"
    type: "date-time"
    description: "The date that the ads in the ad group will expire."

  - name: "forwardCompatibilityMap"
    type: "array"
    description: "Details about the forward compatibility settings for the ad group."
    doc-link: https://docs.microsoft.com/en-us/bingads/customer-management-service/keyvaluepairofstringstring
    array-attributes:
      - name: "keyValuePairOfStringString"
        type: "array"
        description: "Key and value pairs for the ad group's forward compatibility settings."
        array-attributes:
          - name: "key"
            type: "string"
            description: "The name of the setting."

          - name: "value"
            type: "string"
            description: "The value of the setting."

  - name: "language"
    type: "string"
    description: "The language of the ads and keywords in the ad group."

  - name: "name"
    type: "string"
    description: "The name of the ad group."

  - name: "nativeBidAdjustment"
    type: "integer"
    description: "The percent amount by which to adjust the bid for intent ads above or below the base ad group or keyword bid."

  - name: "network"
    type: "string"
    description: |
      The search networks where the ads will display. Possible values are:

      - `OwnedAndOperatedAndSyndicatedSearch`
      - `OwnedAndOperatedOnly`
      - `SyndicatedSearchOnly`

  - name: "pricingModel"
    type: "string"
    description: |
      The pricing model for the ad group. The only supported pricing model in Bing Ads is based on cost per click, or CPC.

      **This field has been deprecated by Bing Ads.**

  - name: "remarketingTargetingSetting"
    type: "string"
    description: |
      The targeting setting that is applicable for all audiences, or custom audiences and remarketing lists associated with the ad group.

      Possible values are:

      - `TargetAndBid`- Ads are shown only to people included in the audience
      - `BidOnly` - Ads can be shown to everyone, but the bid adjustment will apply to people included in the audience

  - name: "searchBid"
    type: "number"
    description: "The default bid to use when the user's query and the ad group's keywords match by using either a broad, exact or phrase match comparison."

  - name: "settings"
    type: "array"
    description: "Details about the settings applied to the ad group."
    array-attributes:
      - name: "type"
        type: "string"
        description: "The type of setting. For example: `ShoppingSetting`"
        doc-link: https://docs.microsoft.com/en-us/bingads/campaign-management-service/setting

  - name: "startDate"
    type: "date-time"
    description: "The date that the ads in the ad group can begin serving."

  - name: "status"
    type: "string"
    description: |
      The status of the ad group. Possible values are:

      - `Active`
      - `Expired`
      - `Paused`

  - name: "trackingUrlTemplate"
    type: "string"
    description: "The tracking template to use as a default for all URLs in your ad group."

  - name: "urlCustomParameters"
    type: "array"
    description: "The custom collection of key and value parameters for URL tracking."
---