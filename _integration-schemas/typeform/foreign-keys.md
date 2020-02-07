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
# Forms doesn't currently have its own table, but it might some day
  # - id: "form-id"
  #   table: ""
  #   attribute: "form_id"
  #   all-foreign-keys:
  #     - table: "forms"

  - id: "landing-id"
    table: "landings"
    attribute: "landing_id"
    all-foreign-keys:
      - table: "landings"
      - table: "answers"

  - id: "question-id"
    table: "questions"
    attribute: "question_id"
    all-foreign-keys:
      - table: "answers"
      - table: "questions"
---