---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "pardot"

version: "1"

foreign-keys:
  - id: "campaign-id"
    table: "campaigns"
    attribute: "campaign_id"
    all-foreign-keys:
      - table: "campaigns"
        join-on: "id"
      - table: "opportunities"
      - table: "prospects"

  - id: "email-template-id"
    table: ""
    attribute: "email_template_id"
    all-foreign-keys:
      - table: "email_clicks"
      - table: "visitor_activities"

  - id: "list-email-id"
    table: ""
    attribute: "list_email_id"
    all-foreign-keys:
      - table: "email_clicks"
      - table: "visitor_activities"

  - id: "list-membership-id"
    table: "list_memberships"
    attribute: ""
    all-foreign-keys:
      - table: "list_memberships"
        join-on: "id"

  - id: "list-id"
    table: "lists"
    attribute: "list_id"
    all-foreign-keys:
      - table: "list_memberships"
      - table: "lists"
        join-on: "id"

  - id: "opportunity-id"
    table: "opportunities"
    attribute: "opportunity_id"
    all-foreign-keys:
      - table: "opportunities"
        join-on: "id"

  - id: "prospect-id"
    table: "prospects"
    attribute: "prospect_id"
    all-foreign-keys:
      - table: "email_clicks"
      - table: "list_memberships"
      - table: "prospects"
        join-on: "id"
      - table: "visitor_activities"
      - table: "visits"

  - id: "user-id"
    table: "users"
    attribute: ""
    all-foreign-keys:
      - table: "prospect_accounts"
        subattribute: "assigned_to.user"
        join-on: "id"
      - table: "users"
        join-on: "id"

  - id: "visitor-id"
    table: "visitors"
    attribute: "visitor_id"
    all-foreign-keys:
      - table: "visitor_activities"
      - table: "visitors"
        join-on: "id"
      - table: "visits"

  - id: "visit-id"
    table: "visits"
    attribute: "visit_id"
    all-foreign-keys:
      - table: "visits"
        join-on: "id"
---