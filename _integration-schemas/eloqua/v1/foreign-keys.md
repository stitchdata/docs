---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "eloqua"

version: "1.0"

foreign-keys:
  - id: "account-id"
    table: "accounts"
    attribute: "id"
    all-foreign-keys:
      - table: "accounts"
        join-on: "id"

  - id: "asset-id"
    table: "assets"
    attribute: "AssetId"
    all-foreign-keys:
      - table: "assets"
        join-on: "id"
      - table: "activity_bounceback"
      - table: "activity_email_clickthrough"
      - table: "activity_email_open"
      - table: "activity_email_send"
      - table: "activity_form_submit"
      - table: "activity_page_view"
      - table: "activity_subscribe"
      - table: "activity_unsubscribe"
      - table: "activity_web_visit"

  - id: "campaign-id"
    table: "campaigns"
    attribute: "CampaignId"
    all-foreign-keys:
      - table: "campaigns"
        join-on: "id"
      - table: "activity_bounceback"
      - table: "activity_email_clickthrough"
      - table: "activity_email_open"
      - table: "activity_email_send"
      - table: "activity_form_submit"
      - table: "activity_page_view"
      - table: "activity_subscribe"
      - table: "activity_unsubscribe"

  - id: "contact-id"
    table: "contacts"
    attribute: "ContactId"
    all-foreign-keys:
      - table: "contacts"
        join-on: "id"
      - table: "activity_bounceback"
      - table: "activity_email_clickthrough"
      - table: "activity_email_open"
      - table: "activity_email_send"
      - table: "activity_form_submit"
      - table: "activity_page_view"
      - table: "activity_subscribe"
      - table: "activity_unsubscribe"
      - table: "visitors"
        join-on: "contactId"

  - id: "form-id"
    table: "forms"
    attribute: "id"
    all-foreign-keys:
      - table: "forms"
        join-on: "id"
      - table: "emails"
        subtable: "forms"
---