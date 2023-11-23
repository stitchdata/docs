---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "google-search-console"

version: "1"

foreign-keys:
  - id: "site-url"
    table: "sites"
    attribute: "site_url"
    all-foreign-keys:
      - table: "sites"
        join-on: "site_url"
      - table: "sitemaps"
        join-on: "site_url"
      - table: "performance_report_country"
        join-on: "site_url"
      - table: "performance_report_custom"
        join-on: "site_url"  
      - table: "performance_report_date"
        join-on: "site_url"
      - table: "performance_report_device"
        join-on: "site_url"
      - table: "performance_report_page"
        join-on: "site_url"  
      - table: "performance_report_query"
        join-on: "site_url"      

  - id: "search-type"
    table: "performance_report_query"
    attribute: "search_type"
    all-foreign-keys:
      - table: "performance_report_query"
        join-on: "search_type"
      - table: "performance_report_country"
        join-on: "search_type" 
      - table: "performance_report_custom"
        join-on: "search_type" 
      - table: "performance_report_date"
        join-on: "search_type"
      - table: "performance_report_page"
        join-on: "search_type"
      - table: "performance_report_device"
        join-on: "search_type"                   
---