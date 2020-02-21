---
tap: "linkedin-ads"
version: "1"
key: "campaign"

name: "campaigns"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-linkedin-ads/blob/master/tap_linkedin_ads/schemas/campaigns.json"
description: |
  The `{{ table.name }}` table contains info about the campaigns in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "Search For Campaigns"
    doc-link: "https://docs.microsoft.com/en-us/linkedin/marketing/integrations/ads/account-structure/create-and-manage-campaigns#search-for-campaigns"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The campaign ID."
    foreign-key-id: "campaign-id"
  
  - name: "last_modified_time"
    type: "date-time"
    replication-key: true
    description: "The time the campaign was last modified."
    
  - name: "account"
    type: "string"
    description: "URN identifying the advertising account associated with the campaign."
  
  - name: "account_id"
    type: "integer"
    description: "The ID of the account associated with the campaign."
    foreign-key-id: "account-id"
  
  - name: "associated_entity"
    type: "string"
    description: "An URN identifying the intended beneficiary of the advertising campaign such as a specific company or member."
  
  - name: "associated_entity_organization_id"
    type: "integer"
    description: ""
  
  - name: "associated_entity_person_id"
    type: "string"
    description: ""
  
  - name: "audience_expansion_enabled"
    type: "boolean"
    description: "Indicates if Audience Expansion is enabled for the campaign provides query expansion for certain targeting criteria."
  
  - name: "campaign_group"
    type: "string"
    description: "URN identifying the campaign group associated with the campaign. If the campaign group is not specified, the campaign is assigned to account's default campaign group."
  
  - name: "campaign_group_id"
    type: "integer"
    description: "The ID of the campaign group associated with the campaign."
    foreign-key-id: "campaign-group-id"
  
  - name: "change_audit_stamps"
    type: "object"
    description: ""
    subattributes:
      - name: "created"
        type: "object"
        description: ""
        subattributes:
          - name: "time"
            type: "date-time"
            description: ""
      - name: "last_modified"
        type: "object"
        description: ""
        subattributes:
          - name: "time"
            type: "date-time"
            description: ""
  
  - name: "cost_type"
    type: "string"
    description: "The cost type - `CPM`, `CPC`, or `CPV`."
  
  - name: "created_time"
    type: "date-time"
    description: ""
  
  - name: "creative_selection"
    type: "string"
    description: "The creative selection - `ROUND_ROBIN` or `OPTIMIZED`."
  
  - name: "daily_budget"
    type: "object"
    description: "Details about the budget for the campaign."
    subattributes:
      - name: "amount"
        type: "number"
        description: "Maximum amount to spend per day UTC. The amount of money as a real number string."

      - name: "currency_code"
        type: "string"
        description: "The ISO currency code. The currency must match that of the parent account."
  
  - name: "locale"
    type: "object"
    description: "Details about the campaign's locale."
    subattributes:
      - name: "country"
        type: "string"
        description: "Locale of the campaign. An uppercase two-letter country code as defined by ISO-3166."
      - name: "language"
        type: "string"
        description: "Locale of the campaign. A lowercase two-letter language code as defined by ISO-639."
  
  - name: "name"
    type: "string"
    description: "The name of the campaign."
  
  - name: "offsite_delivery_enabled"
    type: "boolean"
    description: "Indicates if offsite delivery is enabled for the campaign."
  
  - name: "optimization_target_type"
    type: "string"
    description: |
      Determines how this campaign is optimized for spending. If this is not set, there is no optimization. Refer to [{{ integration.display_name }}' documentation](https://docs.microsoft.com/en-us/linkedin/marketing/integrations/ads/account-structure/create-and-manage-campaigns#optimization-of-campaigns){:target="new"} for more info.
  
  - name: "run_schedule"
    type: "object"
    description: "Details about the campaign's run schedule."
    subattributes:
      - name: "end"
        type: "date-time"
        description: "Scheduled date range to stop associated creatives. Represents the exclusive (strictly less than) value in which to end the range."
      - name: "start"
        type: "date-time"
        description: "Scheduled date range to run associated creatives."
  
  - name: "serving_statuses"
    type: "null"
    description: "The serving status of the campaign."
  
  - name: "status"
    type: "string"
    description: |
      The status of the campaign. Possible values are:

      - `ACTIVE` - Denotes that the campaign is fully servable.
      - `PAUSED` - Denotes that the campaign meets all requirements to be served, but temporarily should not be.
      - `ARCHIVED` - Denotes that the campaign is presently inactive, and should mostly be hidden in the UI until un-archived.
      - `COMPLETED` - Denotes that the campaign has reached a specified budgetary or chronological limit.
      - `CANCELED` - Denotes that the campaign has been permanently canceled, such as when an advertising account is permanently closed.
      - `DRAFT` - Denotes that the campaign is still being edited and not eligible for serving. Some validation will be postponed until the campaign is activated.
  
  - name: "targeting"
    type: "object"
    description: "**Deprecated by {{ integration.display_name }}**. Use `targeting_criteria` instead."
    subattributes:
      - name: "excluded_targeting_facets"
        type: "null"
        description: "**Deprecated by {{ integration.display_name }}**. Use `targeting_criteria` instead."
      - name: "included_targeting_facets"
        type: "null"
        description: "**Deprecated by {{ integration.display_name }}**. Use `targeting_criteria` instead."
  
  - name: "targeting_criteria"
    type: "object"
    description: |
      Specifies targeting criteria that the member should match. Refer to [{{ integration.display_name }}' documentation](https://docs.microsoft.com/en-us/linkedin/shared/references/v2/ads/targeting-criteria){:target="new"} for more info.
    doc-link: "https://docs.microsoft.com/en-us/linkedin/shared/references/v2/ads/targeting-criteria"
    subattributes:
      - name: "exclude"
        type: "null"
        description: ""
      - name: "include"
        type: "object"
        description: ""
        subattributes:
          - name: "and"
            type: "null"
            description: ""
  
  - name: "type"
    type: "string"
    description: |
      The type of the campaign. Possible values are:

      - `TEXT_AD` - Text-based ads that show up in the right column or top of the page on LinkedIn.
      - `SPONSORED_UPDATES` - Native ads that promote a company's content updates in the LinkedIn feed.
      - `SPONSORED_INMAILS` - Personalized messages with a call-to-action button delivered to a LinkedIn's member inbox.
      - `DYNAMIC` - Ads that are dynamically personalized.
  
  - name: "unit_cost"
    type: "object"
    description: "Amount to bid per click, impression, or other event depending on the pricing model."
    subattributes:
      - name: "amount"
        type: "number"
        description: "The amount to bid to the associated account."
      - name: "currency_code"
        type: "string"
        description: "The ISO currency code to the associated account."
  
  - name: "version"
    type: "object"
    description: "Details about the campaign's version."
    subattributes:
      - name: "version_tag"
        type: "string"
        description: "Each entity has a version tag associated with it. The version tag is initiated to 1 when the entity is created. Each single update to the entity increases its version tag by 1."
---