---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "pinterest-ads"

version: "1"

foreign-keys:
  - id: "advertiser-id"
    table: "advertisers"
    attribute: "advertiser_id"
    all-foreign-keys:
      - table: "advertisers"
        join-on: "advertiser_id"
      - table: "advertiser_report"
        join-on: "advertiser_id"

  - id: "campaign-id"
    table: "campaign_report"
    attribute: "campaign_id"
    all-foreign-keys:
      - table: "campaign_report"
        join-on: "campaign_id"
      - table: "ad_group_report"
        join-on: "ad_group_campaign_id" 
      - table: "pin_promotion_report"
        join-on: "pin_promotion_campaign_id"
      - table: "advertisers"
        join-on: "campaign_ids"  

  - id: "adgroup-id"
    table: "ad_group_report"
    attribute: "ad_group_id"
    all-foreign-keys:
      - table: "ad_group_report"
        join-on: "ad_group_id"
      - table: "pin_promotion_report"
        join-on: "pin_promotion_ad_group_id"              
---