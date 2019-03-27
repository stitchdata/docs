---
tap: "netsuite"
# version: "1.0"

name: "Campaign"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Campaign.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "audience"
    type: "anything"
    description: ""

  - name: "baseCost"
    type: "number, string"
    description: ""

  - name: "campaignDirectMailList"
    type: "anything"
    description: ""

  - name: "campaignEmailList"
    type: "anything"
    description: ""

  - name: "campaignEventList"
    type: "anything"
    description: ""

  - name: "campaignId"
    type: "string"
    description: ""

  - name: "category"
    type: "anything"
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
    type: "anything"
    description: ""

  - name: "customForm"
    type: "anything"
    description: ""

  - name: "endDate"
    type: "date-time"
    description: ""

  - name: "eventResponseList"
    type: "anything"
    description: ""

  - name: "expectedRevenue"
    type: "number, string"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "family"
    type: "anything"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "itemList"
    type: "anything"
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
    type: "anything"
    description: ""

  - name: "offer"
    type: "anything"
    description: ""

  - name: "owner"
    type: "anything"
    description: ""

  - name: "profit"
    type: "number, string"
    description: ""

  - name: "promotionCode"
    type: "anything"
    description: ""

  - name: "roi"
    type: "number, string"
    description: ""

  - name: "searchEngine"
    type: "anything"
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
    type: "anything"
    description: ""
---