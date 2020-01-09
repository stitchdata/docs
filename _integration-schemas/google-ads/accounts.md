---
tap: "google-ads"
version: "1"

name: "accounts"
doc-link: https://developers.google.com/adwords/api/docs/reference/v201806/ManagedCustomerService.ManagedCustomer
singer-schema: https://github.com/singer-io/tap-adwords/blob/master/tap_adwords/schemas/accounts.json
description: |
  The `{{ table.name }}` table contains high-level info about the Google AdWords account(s) you’ve connected to Stitch.

  [This is a **Core Object** table](#replication).

replication-method: "Full Table"
attribution-window: true

attributes:
  - name: "customerId"
    type: "integer"
    primary-key: true
    description: "The ID of the AdWords account that the record belongs to."
    foreign-key-id: "customer-id"

  - name: "canManageClients"
    type: "boolean"
    description: "Indicates if the AdWords account can manage clients."

  - name: "currencyCode"
    type: "string"
    description: "The currency code used by the AdWords account."

  - name: "dateTimeZone"
    type: "string"
    description: "The local timezone used by the AdWords account."

  - name: "name"
    type: "string"
    description: "The name used by the manager to refer to the client."

  - name: "testAccount"
    type: "boolean"
    description: "Indicates if the managed customer's account is a test account."
---