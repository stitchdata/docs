---
tap: "google-adwords"
version: "1.0"

name: "campaigns"
doc-link: https://developers.google.com/adwords/api/docs/reference/v201806/CampaignService.Campaign
singer-schema: https://github.com/singer-io/tap-adwords/blob/master/tap_adwords/schemas/campaigns.json
description: |
  The `{{ table.name }}` table contains detailed info about your Google AdWords campaigns.

  [This is a **Core Object** table](#replication).

replication-method: "Full Table"
attribution-window: true

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the campaign."
    foreign-key-id: "campaign-id"

  - name: "adServingOptimizationStatus"
    type: "string"
    description: "The campaign's ad serving optimization status."

  - name: "advertisingChannelType"
    type: "string"
    description: "The primary serving target for ads within the campaign."

  - name: "baseCampaignId"
    type: "integer"
    description: "The ID of the base campaign of the draft or trial campaign."
    foreign-key-id: "base-campaign-id"

  - name: "conversionOptimizerEligibility"
    type: "object"
    description: "Eligibility data for the campaign to transition to Conversion Optimizer."
    subattributes:
      - name: "eligible"
        type: "integer"
        description: "Indicates if the campaign is eligible to enter Conversion Optimizer."

  - name: "campaignTrialType"
    type: "string"
    description: "Indicates the campaign type."
    doc-link: https://developers.google.com/adwords/api/docs/reference/v201806/CampaignService.CampaignTrialType

  - name: "customerId"
    type: "integer"
    description: "The ID of the AdWords account that the record belongs to."
    foreign-key-id: "customer-id"

  - name: "endDate"
    type: "date-time"
    description: "The date the campaign ends."

  - name: "frequencyCap"
    type: "object"
    description: "Details about the frequency cap for the campaign."
    subattributes:
      - name: "impressions"
        type: "integer"
        description: "The maximum number of impressions allowed during the time range by this cap."

      - name: "timeUnit"
        type: "string"
        description: "The unit of time the cap is defined at."

  - name: "labels"
    type: "array"
    description: "Labels attached to the campaign."
    subattributes:
      - name: "id"
        type: "integer"
        primary-key: true
        description: "The ID of the label applied to the campaign."
        foreign-key-id: "label-id"

      - name: "name"
        type: "string"
        description: "The name of the label applied to the campaign."

      - name: "status"
        type: "string"
        description: "The status of the label applied to the campaign."

      - name: "Label.Type"
        type: "string"
        description: "Indicates that this instance is a subtype of Label."

      - name: "attribute"
        type: "object"
        description: "Details about the label attached to the campaign."
        subattributes:
          - name: "backgroundColor"
            type: "string"
            description: "The background color of the label in RGB format."

          - name: "LabelAttribute.Type"
            type: "string"
            description: "Indicates that this instance is a subtype of LabelAttribute."

          - name: "description"
            type: "string"
            description: "The description of the label."

  - name: "name"
    type: "string"
    description: "The name of the campaign."

  - name: "networkSetting"
    type: "object"
    description: "Network settings for the campaign."
    subattributes:
      - name: "targetGoogleSearch"
        type: "integer"
        description: "Indicates if ads in the campaign will be served with Google.com search results."

  - name: "settings"
    type: "object"
    description: "List of settings for the campaign."
    subattributes:
      - name: "languageCode"
        type: "string"
        description: "The language code that indicates what language the domain's content is in. For example: `en` signifies English."

      - name: "negativeGeoTargetType"
        type: "string"
        description: "The negative geotargeting setting used for the campaign."

      - name: "Setting.Type"
        type: "string"
        description: "Indicates that this instance is a subtype of Setting."

      - name: "positiveGeoTargetType"
        type: "string"
        description: "The positive geotargeting setting used for the campaign."

      - name: "domainName"
        type: "string"
        description: "The domain name that the setting represents. For example: google.com"

  - name: "startDate"
    type: "date-time"
    description: "The date the campaign starts."

  - name: "status"
    type: "string"
    description: "The status of the campaign."
---