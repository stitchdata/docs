---
tap: "bing-ads"
version: "1.0"

name: "campaigns"
doc-link: https://docs.microsoft.com/en-us/bingads/campaign-management-service/campaign
singer-schema: 
description: |
  The `campaigns` table contains info about the campaigns in your Bing Ads account.

  [This is a **Core Object** table](#replication).

replication-method: "Full Table"

api-method:
  name: getCampaignsByAccountId
  doc-link: https://docs.microsoft.com/en-us/bingads/campaign-management-service/getcampaignsbyaccountid

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The campaign ID."
    foreign-key-id: "campaign-id"

  - name: "biddingScheme"
    type: "object"
    doc-link: https://docs.microsoft.com/en-us/bingads/campaign-management-service/biddingscheme
    description: "Details about the bid strategy type used to manage the campaign."
    object-attributes:
      - name: "type"
        type: "string"
        description: "The type of bidding scheme set for the campaign."
        doc-link: https://docs.microsoft.com/en-us/bingads/campaign-management-service/biddingscheme

  - name: "budgetId"
    type: "integer"
    description: "The ID of the budget that the campaign shares with other campaigns in the account. Refer to [Microsoft's documentation](https://docs.microsoft.com/en-us/bingads/campaign-management-service/budget) for more info on budgets."

  - name: "budgetType"
    type: "string"
    description: "The budget type that determines how the budget is spent."

  - name: "campaignType"
    type: "string"
    description: "The type of campaign."

  - name: "dailyBudget"
    type: "number"
    description: "The amount to spend daily on the campaign."

  - name: "description"
    type: "string"
    description: "The description of the campaign."

  - name: "forwardCompatibilityMap"
    type: "array"
    description: "Details about the forward compatibility settings for the campaign."
    doc-link: https://docs.microsoft.com/en-us/bingads/customer-management-service/keyvaluepairofstringstring
    array-attributes:
      - name: "keyValuePairOfStringString"
        type: "array"
        description: "Key and value pairs for the campaign's forward compatibility settings."
        array-attributes:
          - name: "key"
            type: "string"
            description: "The name of the setting."

          - name: "value"
            type: "string"
            description: "The value of the setting."

  - name: "languages"
    type: "string"
    description: "The languages of the ads and keywords in the campaign."

  - name: "name"
    type: "string"
    description: "The name of the campaign."

  - name: "nativeBidAdjustment"
    type: "integer"
    description: "The percent amount by which to adjust the bid for intent ads above or below the base ad group or keyword bid."

  - name: "settings"
    type: "array"
    description: "The settings for the campaign."
    array-attributes:
      - name: "type"
        type: "string"
        description: "The type of setting. For example: `ShoppingSetting`"
        doc-link: https://docs.microsoft.com/en-us/bingads/campaign-management-service/setting

  - name: "status"
    type: "string"
    description: "The status of the campaign. Possible values are `Active` and `Paused`."

  - name: "timeZone"
    type: "string"
    description: "The timezone where the campaign operates."

  - name: "trackingUrlTemplate"
    type: "string"
    description: "The tracking template to use as a default for all URLs in the campaign."

  - name: "urlCustomParameters"
    type: "string"
    description: "The custom collection of key and value parameters for URL tracking."
---