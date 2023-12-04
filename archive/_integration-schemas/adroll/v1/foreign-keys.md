---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "adroll"

version: "1"

foreign-keys:
  - id: "adgroup-id"
    table: "ad_groups"
    attribute: "eid"
    all-foreign-keys:
      - table: "ad_groups"
        join-on: "eid"
      - table: "ads"
        subattribute: "adgroups"
        join-on: "id"
      - table: "campaigns"
        subattribute: "adgroups"
        join-on: "value"

  - id: "ad-report-eid"
    table: "ad_reports"
    attribute: "eid"
    all-foreign-keys:
      - table: "ad_reports"
        join-on: "eid"

  - id: "ad-id"
    table: "ads"
    attribute: "id"
    all-foreign-keys:
      - table: "ad_groups"
        subattribute: "ads"
        join-on: "id"
      - table: "ad_reports"
        join-on: "ad"
      - table: "ads"
        join-on: "eid"
      - table: "ads"
        join-on: "original_ad"
        
  - id: "advertisable-id"
    table: "advertisables"
    attribute: "eid"
    all-foreign-keys:
      - table: "advertisables"
        join-on: "eid"
      - table: "campaigns"
        join-on: "advertisable"
      - table: "segments"
        join-on: "advertisable_eid"
        
  - id: "campaign-id"
    table: "campaigns"
    attribute: "eid"
    all-foreign-keys:
      - table: "campaigns"
        join-on: "eid"
        
  - id: "segment-id"
    table: "segments"
    attribute: "eid"
    all-foreign-keys:
      - table: "ad_groups"
        subattribute: "segments"
        join-on: "id"
      - table: "segments"
        join-on: "eid"                              
---