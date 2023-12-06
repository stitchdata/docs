---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "impact"

version: "1"

foreign-keys:
  - id: "account-id"
    table: ""
    attribute: "account_id"
    all-foreign-keys:
      - table: "api_submissions"
      - table: "ftp_file_submissions"

  - id: "action-inquiry-id"
    table: "action_inquiries"
    attribute: ""
    all-foreign-keys:
      - table: "action_inquiries"
        join-on: "id"

  - id: "action-tracker-id"
    table: ""
    attribute: "action_tracker_id"
    all-foreign-keys:
      - table: "action_updates"
      - table: "actions"
      - table: "api_submissions"
      - table: "conversion_paths"
        subattribute: "events"
      - table: "exception_lists"
        subattribute: "action_trackers"

  - id: "action-update-id"
    table: "action_updates"
    attribute: "action_update_id"
    all-foreign-keys:
      - table: "action_updates"

  - id: "action-id"
    table: "actions"
    attribute: "action_id"
    all-foreign-keys:
      - table: "action_inquiries"
      - table: "action_updates"
      - table: "actions"
        join-on: "id"
      - table: "conversion_paths"
        subattribute: "events"

  - id: "ad-id"
    table: "ads"
    attribute: "ad_id"
    all-foreign-keys:
      - table: "action_updates"
      - table: "actions"
      - table: "ads"
      - table: "conversion_paths"
        subattribute: "events"

  - id: "advertiser-id"
    table: ""
    attribute: "advertiser_id"
    all-foreign-keys:
      - table: "catalogs"

  - id: "campaign-id"
    table: "campaigns"
    attribute: "campaign_id"
    all-foreign-keys:
      - table: "action_inquiries"
      - table: "action_updates"
      - table: "actions"
      - table: "ads"
      - table: "api_submissions"
      - table: "campaigns"
        join-on: "id"
      - table: "catalogs"
      - table: "clicks"
      - table: "contacts"
      - table: "conversion_paths"
      - table: "deals"
      - table: "exception_lists"
      - table: "invoices"
        subattribute: "line_items"
      - table: "media_partner_groups"
      - table: "media_partners"
        subattribute: "campaigns"
      - table: "notes"
      - table: "promo_codes"
      - table: "tracking_value_requests"
      - table: "unique_urls"

  - id: "catalog-item-id"
    table: "catalog_items"
    attribute: "catalog_item_id"
    all-foreign-keys:
      - table: "catalog_items"
        join-on: "id"

  - id: "catalog-id"
    table: "catalogs"
    attribute: "catalog_id"
    all-foreign-keys:
      - table: "catalog_items"
      - table: "catalogs"
        join-on: "id"

  - id: "contact-id"
    table: "contacts"
    attribute: "contact_id"
    all-foreign-keys:
      - table: "contacts"

  - id: "customer-id"
    table: ""
    attribute: "customer_id"
    all-foreign-keys:
      - table: "action_updates"
      - table: "actions"
      - table: "conversion_paths"

  - id: "deal-id"
    table: "deals"
    attribute: "deal_id"
    all-foreign-keys:
      - table: "ads"
      - table: "deals"
        join-on: "id"
      - table: "promo_codes"
      - table: "tracking_value_requests"

  - id: "exception-list-item-id"
    table: "exception_list_items"
    attribute: "exception_list_item_id"
    all-foreign-keys:
      - table: "exception_list_items"

  - id: "exception-list-id"
    table: "exception_lists"
    attribute: "list_id"
    all-foreign-keys:
      - table: "exception_list_items"
      - table: "exception_lists"
        join-on: "id"

  - id: "invoice-id"
    table: "invoices"
    attribute: "invoice_id"
    all-foreign-keys:
      - table: "invoices"
        join-on: "id"

  - id: "media-id"
    table: ""
    attribute: "media_id"
    all-foreign-keys:
      - table: "clicks"
      - table: "conversion_paths"
        subattribute: "events"
      - table: "invoices"
      - table: "notes"

  - id: "media-partner-group-id"
    table: "media_partner_groups"
    attribute: "group_id"
    all-foreign-keys:
      - table: "media_partner_groups"
        join-on: "id"
      - table: "media_partners"
        subattribute: "groups"

  - id: "media-partner-id"
    table: "media_partners"
    attribute: "media_partner_id"
    all-foreign-keys:
      - table: "action_inquiries"
      - table: "action_updates"
      - table: "actions"
      - table: "api_submissions"
      - table: "media_partner_groups"
        subattribute: "media_partners"
      - table: "media_partners"
        join-on: "id"
      - table: "tracking_value_requests"
      - table: "unique_urls"

  - id: "phone-number-id"
    table: "phone_numbers"
    attribute: "phone_number_id"
    all-foreign-keys:
      - table: "phone_numbers"
        join-on: "id"
      - table: "tracking_value_requests"
        subattribute: "phone_numbers"
        join-on: "id"

  - id: "promo-code-id"
    table: "promo_codes"
    attribute: "promo_code_id"
    all-foreign-keys:
      - table: "promo_codes"
        join-on: "id"
      - table: "tracking_value_requests"
        subattribute: "promo_codes"
        join-on: "id"

  - id: "report-id"
    table: "reports"
    attribute: "id"
    all-foreign-keys:
      - table: "report_metadata"
      - table: "reports"

  - id: "unique-url-id"
    table: "unique_urls"
    attribute: "id"
    all-foreign-keys:
      - table: "tracking_value_requests"
        subattribute: "unique_urls"
        join-on: "id"
      - table: "unique_urls"
        join-on: "id"
---