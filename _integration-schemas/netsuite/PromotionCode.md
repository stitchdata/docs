---
tap: "netsuite"
version: "1"

name: "PromotionCode"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/promotioncode.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/PromotionCode.json"
description: |
  The `{{ table.name }}` table contains info about the promotion codes in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "promotion-code"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "promotion-code-id"

  - name: "applyDiscountTo"
    type: "varies"
    description: ""

  - name: "code"
    type: "string"
    description: ""

  - name: "codePattern"
    type: "string"
    description: ""

  - name: "currencyList"
    type: "varies"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "customForm"
    type: "varies"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "discount"
    type: "varies"
    description: ""

  - name: "discountType"
    type: "boolean, string"
    description: ""

  - name: "displayLineDiscounts"
    type: "boolean, string"
    description: ""

  - name: "endDate"
    type: "date-time"
    description: ""

  - name: "excludeItems"
    type: "boolean, string"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "freeShipMethod"
    type: "varies"
    description: ""

  - name: "implementation"
    type: "varies"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "isPublic"
    type: "boolean, string"
    description: ""

  - name: "itemsList"
    type: "varies"
    description: ""

  - name: "locationList"
    type: "varies"
    description: ""

  - name: "minimumOrderAmount"
    type: "number, string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "numberToGenerate"
    type: "integer, string"
    description: ""

  - name: "partnersList"
    type: "varies"
    description: ""

  - name: "rate"
    type: "string"
    description: ""

  - name: "startDate"
    type: "date-time"
    description: ""

  - name: "useType"
    type: "varies"
    description: ""
---