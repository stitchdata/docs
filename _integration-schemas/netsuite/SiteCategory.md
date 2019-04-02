---
tap: "netsuite"
# version: "1.0"

name: "SiteCategory"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/SiteCategory.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "categoryListLayout"
    type: "varies"
    description: ""

  - name: "correlatedItemsListLayout"
    type: "varies"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "excludeFromSitemap"
    type: "boolean, string"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "isOnline"
    type: "boolean, string"
    description: ""

  - name: "itemId"
    type: "string"
    description: ""

  - name: "itemListLayout"
    type: "varies"
    description: ""

  - name: "metaTagHtml"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "pageTitle"
    type: "string"
    description: ""

  - name: "parentCategory"
    type: "varies"
    description: ""

  - name: "presentationItemList"
    type: "varies"
    description: ""

  - name: "relatedItemsListLayout"
    type: "varies"
    description: ""

  - name: "searchKeywords"
    type: "string"
    description: ""

  - name: "sitemapPriority"
    type: "varies"
    description: ""

  - name: "storeDetailedDescription"
    type: "string"
    description: ""

  - name: "storeDisplayImage"
    type: "varies"
    description: ""

  - name: "storeDisplayThumbnail"
    type: "varies"
    description: ""

  - name: "translationsList"
    type: "varies"
    description: ""

  - name: "urlComponent"
    type: "string"
    description: ""

  - name: "website"
    type: "varies"
    description: ""
---
