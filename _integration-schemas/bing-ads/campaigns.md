---
tap: "bing-ads"
# version: "1.0"

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
    type: ""
    primary-key: true
    description: "The campaign ID."

  - name: "biddingScheme"
    type: ""
    doc-link: https://docs.microsoft.com/en-us/bingads/campaign-management-service/biddingscheme
    description: "Details about the bid strategy type used to manage the campaign."

  - name: "budgetId"
    type: ""
    description: "The ID of the budget that the campaign shares with other campaigns in the account. Refer to [Microsoft's documentation](https://docs.microsoft.com/en-us/bingads/campaign-management-service/budget) for more info on budgets."

  - name: "budgetType"
    type: ""
    description: "The budget type that determines how the budget is spent."

  - name: "campaignType"
    type: ""
    description: "The type of campaign."

  - name: "dailyBudget"
    type: ""
    description: "The amount to spend daily on the campaign."

  - name: "description"
    type: ""
    description: "The description of the campaign."

  - name: "forwardCompatibilityMap"
    type: "array"
    description: "Details about the forward compatibility "
    doc-link: https://docs.microsoft.com/en-us/bingads/customer-management-service/keyvaluepairofstringstring
    array-attributes:

  - name: "languages"
    type: ""
    description: 

  - name: "name"
    type: "string"
    description: "The name of the campaign."

  - name: "nativeBidAdjustment"
    type: "integer"
    description: "The percent amount by which to adjust the bid for intent ads above or below the base ad group or keyword bid."

  - name: "settings"
    type: ""
    description: "The settings for the campaign type."

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
    type: ""
    description: "The custom collection of key and value parameters for URL tracking."
---