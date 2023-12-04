---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "surveymonkey"

version: "1"

foreign-keys:
  - id: "response-id"
    table: "responses"
    attribute: "id"
    all-foreign-keys:
      - table: "responses"
        join-on: "id"
      - table: "simplified_responses"
        join-on: "id"  

  - id: "survey-id"
    table: "survey_details"
    attribute: "id"
    all-foreign-keys:
      - table: "survey_details"
        join-on: "id"
      - table: "responses"
        join-on: "survey_id"
      - table: "simplified_responses"
        join-on: "survey_id"  
---