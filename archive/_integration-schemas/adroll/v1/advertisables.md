---
tap: "adroll"
version: "1"
key: "advertisable"

name: "advertisables"
doc-link: "https://developers.nextroll.com/docs/crud-api/reference.html#get--api-v1-advertisable-get"
singer-schema: "https://github.com/singer-io/tap-adroll/blob/master/tap_adroll/schemas/advertisables.json"
description: |
  The `{{ table.name }}` table contains information about the advertisables in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "Get organization advertisables"
  doc-link: "https://developers.nextroll.com/docs/crud-api/reference.html#get--api-v1-organization-get_advertisables"

attributes:
  - name: "eid"
    type: "string"
    primary-key: true
    description: "The advertisable EID."
    foreign-key-id: "advertisable-id"

  - name: "abm_onboarding_status"
    type: "string"
    description: ""

  - name: "account"
    type: "string"
    description: ""

  - name: "account_country_code"
    type: "string"
    description: ""

  - name: "account_is_autobilled"
    type: "boolean"
    description: ""

  - name: "account_is_prepaid"
    type: "boolean"
    description: ""

  - name: "account_is_suspended"
    type: "boolean"
    description: ""

  - name: "account_suspension_reason"
    type: "string"
    description: ""

  - name: "admin_page_permission"
    type: "boolean"
    description: ""

  - name: "am_email"
    type: "string"
    description: ""

  - name: "approval_state"
    type: "string"
    description: ""

  - name: "attached_users"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "integer"
        description: ""

  - name: "blacklisted_sites"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "business_unit"
    type: "string"
    description: ""

  - name: "campaign_monitor_client_api_key"
    type: "string"
    description: ""

  - name: "campaign_monitor_client_id"
    type: "string"
    description: ""

  - name: "click_through_conversion_window"
    type: "integer"
    description: ""

  - name: "cm_networks"
    type: "string"
    description: ""

  - name: "company_phone"
    type: "string"
    description: ""

  - name: "constant_contact_code"
    type: "string"
    description: ""

  - name: "constant_contact_oauth_url"
    type: "string"
    description: ""

  - name: "country_code"
    type: "string"
    description: ""

  - name: "created_date"
    type: "date-time"
    description: ""

  - name: "csm_admin"
    type: "string"
    description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "default_homepage"
    type: "string"
    description: ""

  - name: "default_utm"
    type: "string"
    description: ""
  
  - name: "enable_customer_multi_dur_segs"
    type: "boolean"
    description: ""

  - name: "fb_offsite_pixels_tos_accepted"
    type: "boolean"
    description: ""

  - name: "fbx_account_id"
    type: "integer"
    description: ""

  - name: "fbx_page_id"
    type: "string"
    description: ""

  - name: "fbx_page_url"
    type: "string"
    description: ""

  - name: "has_approved_consent_solution"
    type: "boolean"
    description: ""

  - name: "has_approved_safari_add_on"
    type: "boolean"
    description: ""

  - name: "has_created_campaign"
    type: "boolean"
    description: ""

  - name: "has_offsite_pixels"
    type: "boolean"
    description: ""

  - name: "has_privacy_policy"
    type: "boolean"
    description: ""

  - name: "has_sales_and_leads_automation"
    type: "boolean"
    description: ""

  - name: "hide_optins_page"
    type: "boolean"
    description: ""

  - name: "homepage_enabled"
    type: "boolean"
    description: ""

  - name: "iab1_category_id"
    type: "integer"
    description: ""

  - name: "iab1_category_name"
    type: "string"
    description: ""

  - name: "iab2_category_id"
    type: "integer"
    description: ""

  - name: "iab2_category_name"
    type: "string"
    description: ""

  - name: "iab_content_id"
    type: "integer"
    description: ""

  - name: "instagram_actor_id"
    type: "string"
    description: ""

  - name: "ip_address_exclusions"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "is_abm_customer"
    type: "boolean"
    description: ""

  - name: "is_active"
    type: "boolean"
    description: ""

  - name: "is_b2b"
    type: "boolean"
    description: ""

  - name: "is_campaign_monitor_syncing"
    type: "boolean"
    description: ""

  - name: "is_constant_contact_syncing"
    type: "boolean"
    description: ""

  - name: "is_coop_approved"
    type: "string"
    description: ""

  - name: "is_kpi_eligible"
    type: "boolean"
    description: ""

  - name: "is_managed"
    type: "boolean"
    description: ""

  - name: "is_marketo_syncing"
    type: "boolean"
    description: ""

  - name: "is_salesforce_system_owned"
    type: "boolean"
    description: ""

  - name: "is_suspended"
    type: "boolean"
    description: ""

  - name: "is_trusted"
    type: "boolean"
    description: ""

  - name: "is_twitter_syncing"
    type: "boolean"
    description: ""

  - name: "liquidads"
    type: "string"
    description: ""

  - name: "logo_url"
    type: "string"
    description: ""

  - name: "magellan_legacy"
    type: "boolean"
    description: ""

  - name: "magellan_query"
    type: "boolean"
    description: ""

  - name: "marketo_api_endpoint"
    type: "string"
    description: ""

  - name: "marketo_client_id"
    type: "string"
    description: ""

  - name: "marketo_secret_key"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nbam_admin"
    type: "string"
    description: ""

  - name: "ops"
    type: "string"
    description: ""

  - name: "optimizer"
    type: "string"
    description: ""

  - name: "optimizer_email"
    type: "string"
    description: ""

  - name: "organization"
    type: "string"
    description: ""

  - name: "page_access_request_status"
    type: "string"
    description: ""

  - name: "path_name"
    type: "string"
    description: ""

  - name: "product_name"
    type: "string"
    description: ""

  - name: "recent_theme_color"
    type: "string"
    description: ""

  - name: "reskin_enabled"
    type: "boolean"
    description: ""

  - name: "revshare_click_percent"
    type: "number"
    description: ""

  - name: "revshare_view_percent"
    type: "number"
    description: ""

  - name: "rollcrawl_enabled"
    type: "boolean"
    description: ""

  - name: "rollworks_self_serve_ads"
    type: "boolean"
    description: ""

  - name: "safari_add_on_theme"
    type: "string"
    description: ""

  - name: "saleser"
    type: "string"
    description: ""

  - name: "self_serve_prospecting_enabled"
    type: "boolean"
    description: ""

  - name: "show_dpa"
    type: "boolean"
    description: ""

  - name: "show_web_dynamic_ads"
    type: "boolean"
    description: ""

  - name: "source"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "twitter_handle"
    type: "string"
    description: ""

  - name: "uhura_enabled"
    type: "boolean"
    description: ""

  - name: "updated_date"
    type: "string"
    description: ""

  - name: "url"
    type: "string"
    description: ""

  - name: "use_universal_campaigns"
    type: "boolean"
    description: ""

  - name: "view_through_conversion_window"
    type: "integer"
    description: ""

  - name: "zvelo_category_id"
    type: "integer"
    description: ""

  - name: "zvelo_category_name"
    type: "string"
    description: ""
---