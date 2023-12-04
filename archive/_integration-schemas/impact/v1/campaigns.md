---
tap: "impact"
version: "1"
key: "campaign"

name: "campaigns"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-impact/blob/master/tap_impact/schemas/campaigns.json"
description: |
  The `{{ table.name }}` table contains info about campaigns in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "Get campaigns"
  doc-link: "https://developer.impact.com/default#operations-Campaigns-GetCampaigns"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "campaign-id"

  - name: "categories"
    type: "object"
    description: ""
    subattributes:
      - name: "additional_category"
        type: "string"
        description: ""

      - name: "additional_sub_categories"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "primary_category"
        type: "string"
        description: ""

      - name: "primary_sub_categories"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

  - name: "company_contacts"
    type: "array"
    description: ""
    subattriubtes:
      - name: "email_address"
        type: "string"
        description: ""

      - name: "first_name"
        type: "string"
        description: ""

      - name: "last_name"
        type: "string"
        description: ""

      - name: "phone_number"
        type: "string"
        description: ""

  - name: "direct_tracking_settings"
    type: "object"
    description: ""
    subattributes:
      - name: "session_window_length"
        type: "integer"
        description: ""

      - name: "unidentified_source_name"
        type: "string"
        description: ""

  - name: "display_future_ads"
    type: "boolean"
    description: ""

  - name: "display_servicing_agency"
    type: "boolean"
    description: ""

  - name: "gateway_tracking_settings"
    type: "object"
    description: ""
    subattributes:
      - name: "campaign_tracking_template"
        type: "string"
        description: ""

      - name: "deep_link_domains"
        type: "string"
        description: ""

      - name: "deep_linking"
        type: "boolean"
        description: ""

      - name: "default_landing_page"
        type: "string"
        description: ""

      - name: "media_partner_tracking_template"
        type: "string"
        description: ""

      - name: "ssl_support"
        type: "boolean"
        description: ""

      - name: "third_party_gateway_query_string_parameters"
        type: "string"
        description: ""

      - name: "third_party_gateway_url"
        type: "string"
        description: ""

      - name: "unique_click_window_length"
        type: "string"
        description: ""

      - name: "unique_click_window_type"
        type: "string"
        description: ""

  - name: "gift_card_payouts"
    type: "boolean"
    description: ""

  - name: "identity_collapsing"
    type: "string"
    description: ""

  - name: "impression_tracking"
    type: "boolean"
    description: ""

  - name: "list_in_marketplace"
    type: "boolean"
    description: ""

  - name: "long_description"
    type: "string"
    description: ""

  - name: "mobile_ready_ads"
    type: "boolean"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "promo_code_tracking"
    type: "boolean"
    description: ""

  - name: "rating"
    type: "integer"
    description: ""

  - name: "resources"
    type: "object"
    description: ""
    subattributes:
      - name: "additional_related_links"
        type: "array"
        description: ""
        subattributes:
          - name: "link_display_name"
            type: "string"
            description: ""

          - name: "link_type"
            type: "string"
            description: ""

          - name: "link_url"
            type: "string"
            description: ""

      - name: "company_homepage"
        type: "string"
        description: ""

      - name: "example_landing_page"
        type: "string"
        description: ""

      - name: "information_page"
        type: "string"
        description: ""

  - name: "search_keywords"
    type: "string"
    description: ""

  - name: "shipping_regions"
    type: "string"
    description: ""

  - name: "short_description"
    type: "string"
    description: ""

  - name: "site_definition"
    type: "string"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "third_party_impression_pixel"
    type: "string"
    description: ""

  - name: "tracking_domain"
    type: "string"
    description: ""

  - name: "trademark_bidding"
    type: "boolean"
    description: ""

  - name: "view_through_crediting"
    type: "boolean"
    description: ""
---