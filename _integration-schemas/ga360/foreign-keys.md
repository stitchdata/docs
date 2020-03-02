---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "google-analytics-360" visitStartTime

version: "1"

foreign-keys:
  - id: "visit-id"
    table: "ga_sessions"
    attribute: "visitId"
    all-foreign-keys:
      - table: "ga_sessions"
        join-on: "visitId"
      - table: "ga_session_hits"  

  - id: "full-visitor-id"
    table: "ga_sessions"
    attribute: "fullVisitorId"
    all-foreign-keys:
      - table: "ga_sessions"
        join-on: "fullVisitorId"
      - table: "ga_session_hits"
        join-on: "fullVisitorId"

  - id: "visit-start-time"
    table: "ga_sessions"
    attribute: "visitStartTime"
    all-foreign-keys:
      - table: "ga_sessions"
        join-on: "visitStartTime"
      - table: "ga_session_hits"
        join-on: "visitStartTime"  
        
  - id: "hit-number"
    table: "ga_session_hits"
    attribute: "hitNumber"
    all-foreign-keys:
      - table: "ga_sessions_hits"
        join-on: "hitNumber"                   
---