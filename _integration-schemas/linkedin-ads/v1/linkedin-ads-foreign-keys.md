---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "integration"

version: "1.0"

foreign-keys:
  - id: "account-id"
    table: "accounts"
    attribute: "id"
    all-foreign-keys:
      - table: "account_users"
        join-on: "account_id"
      - table: "accounts"
        join-on: "id" 
      - table: "campaigns"
        join-on: "account_id"
      - table: "campaign_groups"
        join-on: "account_id"
      - table: "video_ads"
        join-on: "account_id"      

  - id: "reference-organization-id"
    table: ""
    attribute: ""
    all-foreign-keys:
      - table: "accounts"
        join-on: "reference_organization_id"

  - id: "reference-person-id"
    table: ""
    attribute: ""
    all-foreign-keys:
      - table: "accounts"
        join-on: "reference_person_id"

  - id: "user-id"
    table: "account_users"
    attribute: "user_person_id"
    all-foreign-keys:
      - table: "account_users"
        join-on: "user_person_id"

  - id: "campaign-group-id"
    table: "campaign_groups"
    attribute: "id"
    all-foreign-keys:
      - table: "campaign_groups"
        join-on: "id"
       
  - id: "campaign-id"
    table: "campaigns"
    attribute: "id"
    all-foreign-keys:
      - table: "campaigns"
        join-on: "id"
      - table: "creatives"
        join-on: "campaign_id"
      - table: "ad_analytics_by_campaign"
        join-on: "campaign_id" 
        
  - id: "creative-id"
    table: "creatives"
    attribute: "id"
    all-foreign-keys:
      - table: "creatives"
        join-on: "id"
      - table: "ad_analytics_by_creative"
        join-on: "creative_id"
        
  - id: "owner-organization-id"
    table: ""
    attribute: ""
    all-foreign-keys:
      - table: "video_ads"
        join-on: "owner_organization_id"

  - id: "start-at"
    table: "ad_analytics_by_campaign"
    attribute: "start_at"
    all-foreign-keys:
      - table: "ad_analytics_by_campaign"
        join-on: "start_at"

  - id: "content-reference"
    table: "video_ads"
    attribute: "content_reference"
    all-foreign-keys:
      - table: "video_ads"
        join-on: "content_reference"      
                                           
---