---
tap: "netsuite"
version: "1.0"

name: "SiteCategory"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/sitecategory.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/SiteCategory.json"
description: |
  The `{{ table.name }}` table contains info about the categories used to organize your website.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "site-category"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "site-category-id"

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