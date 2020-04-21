---
tap: "facebook-ads"
version: "2"

name: "campaigns"
doc-link: https://developers.facebook.com/docs/reference/ads-api/adcampaign/
singer-schema: https://github.com/singer-io/tap-facebook/blob/master/tap_facebook/schemas/campaigns.json
description: |
  The `campaigns` table contains info about the campaigns in your Facebook Ads account. Facebook defines campaigns as _"a grouping of ad sets organized by the same business objective."_

  **This is a Core Object table**.

  #### Deleted campaigns
   
  If the **Include data from deleted campaigns, ads, and adsets** box in the integration's settings is checked, this table will include data for deleted campaigns.

replication-method: "Key-based Incremental"
attribution-window: true
api-method:
  name: adCampaign - Reading
  doc-link: https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The campaign ID."
    foreign-key-id: "campaign-id"

  - name: "updated_time"
    type: "date-time"
    replication-key: true
    description: "The last time the campaign was updated."

  - name: "name"
    type: "string"
    description: "The name of the campaign."

  - name: "objective"
    type: "string"
    description: "The objective of the campaign."

  - name: "account_id"
    type: "string"
    description: "The ID of the ad account that owns the campaign."
    foreign-key-id: "account-id"

  - name: "effective_status"
    type: "string"
    doc-link: https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group
    description: |
      The effective status of the campaign. According to Facebook's documentation, possible values include:

      - `ACTIVE`
      - `PAUSED`
      - `DELETED`
      - `PENDING_REVIEW`
      - `DISAPPROVED`
      - `PREAPPROVED`
      - `PENDING_BILLING_INFO`
      - `CAMPAIGN_PAUSED`
      - `ARCHIVED`
      - `ADSET_PAUSED`

  - name: "buying_type"
    type: "string"
    description: |
      The campaign buying type. Possible values are:

      - `AUCTION` - This is the default.
      - `RESERVED` - For reach and frequency ads. [See Facebook's documentation for more info](https://developers.facebook.com/docs/marketing-api/reachandfrequency).

  - name: "spend_cap"
    type: "number"
    description: "The spend cap for the campaign."

  - name: "start_time"
    type: "date-time"
    description: "The campaign's start time."

  - name: "ads"
    type: "array"
    description: "The IDs of the ads associated with the campaign."
    subattributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The ID of an ad associated with the campaign."
        foreign-key-id: "ad-id"
---