---
tap: "snapchat-ads"
version: "1"
key: ""

name: "billing_centers"
doc-link: https://marketingapi.snapchat.com/docs/#billing-centers
singer-schema: https://github.com/singer-io/tap-snapchat-ads/tree/master/tap_snapchat_ads/schemas/billing_centers.json
description: "Billing Centers allow Businesses to have multiple invoicing locations to choose from. A Billing Center is the contact that will be receiving invoices."

replication-method: "Key-based Incremental"

table-key-properties: "id"
valid-replication-keys: "updated_at"

attributes:
  - name: "address_line_1"
    type: "string"
    description: "Address line 1"

  - name: "administrative_district_level_1"
    type: "string"
    description: "District"

  - name: "alternative_email_addresses"
    type: "string"
    description: "Array of email addresses"

  - name: "country"
    type: "string"
    description: "Country"

  - name: "created_at"
    type: "date-time"
    description: "Date of creation"

  - name: "email_address"
    type: "string"
    description: "Email address"

  - name: "id"
    primary-key: true
    type: "string"
    description: "Billing Center ID"

  - name: "locality"
    type: "string"
    description: "Locality name"

  - name: "name"
    type: "string"
    description: "Billing center name"

  - name: "organization_id"
    type: "string"
    description: "Organization ID"

  - name: "postal_code"
    type: "string"
    description: "Post code"

  - name: "updated_at"
    type: "date-time"
    description: "Date and Time at which the billing center was last updated"
    replication-key: true
---