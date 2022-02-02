---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "typeform"

version: "1"

foreign-keys:
  - id: "form-id"
    table: "forms"
    attribute: "form_id"
    all-foreign-keys:
      - table: "forms"
      - table: "questions"

  - id: "landing-id"
    table: "landings"
    attribute: "landing_id"
    all-foreign-keys:
      - table: "answers"
      - table: "landings"

  - id: "question-id"
    table: "questions"
    attribute: "question_id"
    all-foreign-keys:
      - table: "answers"
      - table: "questions"
---