---
tap: "taboola"
# version: 

name: "campaign"
doc-link: https://github.com/taboola/Backstage-API/blob/master/Backstage%20API%20-%20Campaigns.pdf
singer-schema: https://github.com/singer-io/tap-taboola/blob/master/tap_taboola/schemas.py#L2
description: |
  The `campaign` table contains info about the campaigns in your Taboola account.

  #### Replication

  During every replication job, all campaigns in your Taboola account will be extracted, or "fully replicated." If you look in the Extraction logs in the Stitch app, you'll see lines like this:

  ```
  2017-10-25 13:46:52,254Z tap - INFO Synced 100 campaigns.
  2017-10-25 13:46:52,255Z tap - INFO Done syncing campaigns.
  ```

  Roughly the same amount of campaigns should be extracted during every job, unless brand new campaigns are added between jobs.

  When Stitch loads the extracted records into your data warehouse, however, only new and updated campaigns will be loaded. **This means that only new and updated campaign records will count towards your row count**.

  #### Deleted Campaigns

  Currently, [the Singer tap](https://github.com/singer-io/tap-taboola) powering this integration has no way to account for campaigns that are hard-deleted in Taboola. This means that if a campaign is deleted at the source, the record for that campaign will remain in the data warehouse.

  #### NULL Dates
  On occasion, Taboola's API will push `NULL` for `start_date` and `999-12-31` for `end_date`. [The Singer tap](https://github.com/singer-io/tap-taboola#gotchas) behind this integration will convert `NULL` dates to `999-12-31` for consistency.
  
replication-method: "Key-based Incremental"
api-method:
  name: listCampaignsAssociatedWithAnAccount
  doc-link: https://github.com/taboola/Backstage-API/blob/master/Backstage%20API%20-%20Campaigns.pdf

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    #  foreign-keys:
    #    - table: "campaign_performance"
    #    - attribute: "campaign_id"
    description: "The campaign ID."

  - name: "n/a"
    replication-key: true

  - name: "start_date"
    type: "date"
    description: "The start date for the campaign."

  - name: "end_date"
    type: "date"
    description: "The end date for the campaign."

  - name: "advertiser_id"
    type: "string"
    description: "The advertiser ID. Ex: `taboola-demo-advertiser`"

  - name: "name"
    type: "string"
    description: "The name of the campaign."

  - name: "tracking_code"
    type: "string"
    description: "The tracking code of the campaign. Ex: `taboola-track`"

  - name: "cpc"
    type: "number"
    description: "The cost per click for the campaign."

  - name: "daily_cap"
    type: "number"
    description: "The daily cap for the campaign."

  - name: "spending_limit"
    type: "number"
    description: "The spending limit for the campaign."

  - name: "spending_limit_model"
    type: "string"
    description: "Indicates if the campaign has a monthly recurring budget or an overall budget. Possible values are `MONTHLY` and `ENTIRE`."

  - name: "country_targeting"
    type: "object"
    description: "The list of countries the campaign will target or exclude."
    subattributes:
      - name: "type"
        type: "string"
        description: "The type of targeting for the associated country. Possible values are `INCLUDE` or `EXCLUDE`."

      - name: "value"
        type: "array"
        description: "The targeted countries' country codes."
        subattributes:
          - name: "type"
            type: "string"
            description: "The targeted country's country code."

  - name: "platform_targeting"
    type: "object"
    description: "Details about the platforms the campaign will target or exclude."
    subattributes:
      - name: "type"
        type: "string"
        description: "The type of targeting for the associated platform. Possible values are `INCLUDE` or `EXCLUDE`."

      - name: "value"
        type: "array"
        description: "The platform types that will be included/excluded."
        subattributes:
          - name: "type"
            type: "string"
            description: "The type of platform. Possible values are `DESK` (desktop) and `PHON` (smartphone)."

  - name: "publisher_targeting"
    type: "object"
    description: "Details about the publishers that blacklisted from publishing the campaign."
    subattributes:
      - name: "type"
        type: "string"
        description: "The type of targeting for the associated publisher. This will always be `EXCLUDE`."

      - name: "value"
        type: "array"
        description: "The account IDs of blacklisted publishers."
        subattributes:
          - name: "type"
            type: "string"
            description: "The account ID of the blacklisted publisher."

  - name: "approval_state"
    type: "string"
    description: |
      The approval state for the campaign, which indicates if the campaign is approved to be served. Possible values:

       - `APPROVED`
       - `REJECTED`
       - `PENDING` 

  - name: "is_active"
    type: "boolean"
    description: "Indicates if the campaign is active."

  - name: "spent"
    type: "number"
    description: "The estimated amount of money the campaign has consumed."

  - name: "status"
    type: "string"
    description: "The status of the campaign. Ex: `RUNNING`"
---