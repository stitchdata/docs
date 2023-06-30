---
tap: "snapchat-ads"
version: "1"
key: ""

name: "ad_accounts"
doc-link: https://developers.snapchat.com/api/docs/#get-all-ad-accounts
singer-schema: https://github.com/singer-io/tap-snapchat-ads/blob/master/tap_snapchat_ads/schemas/ad_accounts.json
description: "This stream retrieves all ad accounts for the specified Organization."

replication-method: "Key-based Incremental"

table-key-properties: "id"
valid-replication-keys: "updated_at"

attributes:
  - name: "advertiser"
    type: "string"
    description: "Name of the Advertiser"

  - name: "advertiser_organization_id"
    type: "string"
    description: "Organization ID of the Advertiser selected"

  - name: "agency_client_metadata"
    type: "object"
    description: "Client metadata is required if agency_representing_client is true and if the Advertiser is based in France or is targeting Ads to audiences in France"
    subattributes:
    - name: "name"
      type: "string"
      description: ""

    - name: "email"
      type: "string"
      description: ""

    - name: "address_line_1"
      type: "string"
      description: ""

    - name: "city"
      type: "string"
      description: ""

    - name: "administrative_district_level_1"
      type: "string"
      description: ""

    - name: "country"
      type: "string"
      description: ""

    - name: "zipcode"
      type: "string"
      description: ""

    - name: "tax_id"
      type: "string"
      description: ""


  - name: "agency_representing_client"
    type: "string"
    description: "Account name"

  - name: "billing_type"
    type: "string"
    description: "Type of billing"

  - name: "client_based_in_country"
    type: "string"
    description: "Required if agency_representing_client is true and if Advertiser is based in France or targeting Ads to audiences in France"

  - name: "client_paying_invoices"
    type: "boolean"
    description: "Required if agency_representing_client is true and if Advertiser is based in France or targeting Ads to audiences in France"

  - name: "created_at"
    type: "date-time"
    description: "Date and Time at which Ad Account was created"

  - name: "currency"
    type: "string"
    description: "Account currency"

  - name: "funding_source_ids"
    type: "array"
    description: "Array of Funding Source IDs"
    subattributes:
      - name: "items" 
        type: "string"
        description: "Funding Source ID"


  - name: "id"
    primary-key: true
    type: "string"
    description: "AD Account ID"
    primary-key: true

  - name: "lifetime_spend_cap_micro"
    type: "integer"
    description: "Required if billing_type is set to IO, the lifetime spend cap of the account in micro currency"

  - name: "name"
    type: "string"
    description: "Name of the AD Account"

  - name: "organization_id"
    type: "string"
    description: "Oragnization ID"

  - name: "paying_advertiser_name"
    type: "string"
    description: "Name of the paying advertiser/political entity"

  - name: "regulations"
    type: "object"
    description: "Required if the Ad Account will contain ads for Credit, Housing or Employment, this attribute is immutable once set to true"
    subattributes:
    - name: "restricted_delivery_signals"
      type: "boolean"
      description: ""


  - name: "status"
    type: "string"
    description: "Delivery status"

  - name: "timezone"
    type: "string"
    description: "AD Account timezone"

  - name: "type"
    type: "string"
    description: "Account type. Example: DIRECT, PARTNER"

  - name: "updated_at"
    type: "date-time"
    description: "Date and Time at which Ad Account was last updated"
    replication-key: true
---