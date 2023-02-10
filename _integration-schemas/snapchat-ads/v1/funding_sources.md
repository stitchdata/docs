---
tap: "snapchat-ads"
version: "1"
key: ""

name: "funding_sources"
doc-link: https://marketingapi.snapchat.com/docs/#funding-sources
singer-schema: https://github.com/singer-io/tap-snapchat-ads/tree/master/tap_snapchat_ads/schemas/funding_sources.json
description: "An Funding Source is owned by an Organization and defines the financial instrument/terms responsible for the ad spend. Funding sources are assigned to an Ad Account in order to pay for the activity within that Ad Account."

replication-method: "Key-based Incremental"

table-key-properties: "id"
valid-replication-keys: "updated_at"

attributes:
  - name: "available_credit_micro"
    type: "integer"
    description: "Total available credit"

  - name: "budget_spent_micro"
    type: "integer"
    description: "Budget Spent (micro-currency)"

  - name: "card_type"
    type: "string"
    description: "Credit Card Type"

  - name: "created_at"
    type: "date-time"
    description: "date and time at which funding source was created"

  - name: "currency"
    type: "string"
    description: "Account currency"

  - name: "daily_spend_limit_currency"
    type: "string"
    description: "Currency for the daily_spend_limit_micro"

  - name: "daily_spend_limit_micro"
    type: "integer"
    description: "Daily spend limit for Credit Card (micro-currency)"

  - name: "email"
    type: "string"
    description: "Email associated with Paypal"

  - name: "end_date"
    type: "date-time"
    description: "End date of the COUPON"

  - name: "expiration_month"
    type: "string"
    description: "Expiration month of the Credit Card"

  - name: "expiration_year"
    type: "string"
    description: "Expiration year of the Credit Card"

  - name: "id"
    primary-key: true
    type: "string"
    description: "Funding source ID"

  - name: "last_4"
    type: "string"
    description: "Last 4 digits of the Credit Card"

  - name: "name"
    type: "string"
    description: "Name of the Credit Card"

  - name: "organization_id"
    type: "string"
    description: "Organization ID"

  - name: "start_date"
    type: "date-time"
    description: "Start date of the COUPON"

  - name: "status"
    type: "string"
    description: "Status of the funding source"

  - name: "total_budget_micro"
    type: "integer"
    description: "Total Budget (micro-currency)"

  - name: "type"
    type: "string"
    description: "Funding Source type"

  - name: "updated_at"
    type: "date-time"
    description: "Date of last update"

  - name: "value_micro"
    type: "integer"
    description: "Value of the COUPON (micro-currency)"
---