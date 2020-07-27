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
  - id: "adgroup-eid"
    table: "ad_groups"
    attribute: "eid"
    all-foreign-keys:
      - table: "ad_groups"
        join-on: "eid"

  - id: "ad-reports-eid"
    table: "ad_reports"
    attribute: "eid"
    all-foreign-keys:
      - table: "ad_reports"
        join-on: "eid"

  - id: "report-date"
    table: "ad_reports"
    attribute: "date"
    all-foreign-keys:
      - table: "ad_reports"
        join-on: "date"      

  - id: "ads-eid"
    table: "ads"
    attribute: "eid"
    all-foreign-keys:
      - table: "ads"
        join-on: "eid"
        
  - id: "advertisables-eid"
    table: "advertisables"
    attribute: "eid"
    all-foreign-keys:
      - table: "advertisables"
        join-on: "eid"
        
  - id: "campaign-eid"
    table: "campaigns"
    attribute: "eid"
    all-foreign-keys:
      - table: "campaigns"
        join-on: "eid"
        
  - id: "segment-eid"
    table: "segments"
    attribute: "eid"
    all-foreign-keys:
      - table: "segments"
        join-on: "eid"                              
---