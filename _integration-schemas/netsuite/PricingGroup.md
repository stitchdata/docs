---
tap: "netsuite"
version: "1.0"

name: "PricingGroup"
doc-link: "https://975200-sb2.app.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/pricinggroup.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/PricingGroup.json"
description: |
  The `{{ table.name }}` table contains info about the pricing groups in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

permission:
  tab: "Setup"
  name: "Accounting Lists"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "pricing-group-id"

  - name: "externalId"
    type: "string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""
---