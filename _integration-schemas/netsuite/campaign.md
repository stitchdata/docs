---
tap: "netsuite"
version: "1.0"

name: "Campaign"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/campaign.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Campaign.json"
description: |
  The `{{ table.name }}` table contains info about the campaigns in your {{ integration.display_name }} account. Campaigns are used to manage marketing initiatives.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "campaign"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "campaign-id"

  - name: "audience"
    type: "varies"
    description: ""

  - name: "baseCost"
    type: "number, string"
    description: ""

  - name: "campaignDirectMailList"
    type: "varies"
    description: ""

  - name: "campaignEmailList"
    type: "varies"
    description: ""

  - name: "campaignEventList"
    type: "varies"
    description: ""

  - name: "campaignId"
    type: "string"
    description: ""

  - name: "category"
    type: "varies"
    description: ""

  - name: "convCostPerCustomer"
    type: "number, string"
    description: ""

  - name: "conversions"
    type: "integer, string"
    description: ""

  - name: "cost"
    type: "number, string"
    description: ""

  - name: "costPerCustomer"
    type: "number, string"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "customForm"
    type: "varies"
    description: ""

  - name: "endDate"
    type: "date-time"
    description: ""

  - name: "eventResponseList"
    type: "varies"
    description: ""

  - name: "expectedRevenue"
    type: "number, string"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "family"
    type: "varies"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "itemList"
    type: "varies"
    description: ""

  - name: "keyword"
    type: "string"
    description: ""

  - name: "leadsGenerated"
    type: "integer, string"
    description: ""

  - name: "local"
    type: "boolean, string"
    description: ""

  - name: "message"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "offer"
    type: "varies"
    description: ""

  - name: "owner"
    type: "varies"
    description: ""

  - name: "profit"
    type: "number, string"
    description: ""

  - name: "promotionCode"
    type: "varies"
    description: ""

  - name: "roi"
    type: "number, string"
    description: ""

  - name: "searchEngine"
    type: "varies"
    description: ""

  - name: "startDate"
    type: "date-time"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "totalRevenue"
    type: "number, string"
    description: ""

  - name: "uniqueVisitors"
    type: "integer, string"
    description: ""

  - name: "url"
    type: "string"
    description: ""

  - name: "vertical"
    type: "varies"
    description: ""
---