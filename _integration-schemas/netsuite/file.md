---
tap: "netsuite"
# version: "1.0"

name: "File"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/File.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "_class"
    type: "string"
    description: ""

  - name: "altTagCaption"
    type: "string"
    description: ""

  - name: "attachFrom"
    type: "varies"
    description: ""

  - name: "bundleable"
    type: "boolean, string"
    description: ""

  - name: "caption"
    type: "string"
    description: ""

  - name: "content"
    type: "string"
    description: ""

  - name: "createdDate"
    type: "date-time"
    description: ""

  - name: "department"
    type: "string"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "encoding"
    type: "varies"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "featuredDescription"
    type: "string"
    description: ""

  - name: "fileSize"
    type: "number, string"
    description: ""

  - name: "fileType"
    type: "varies"
    description: ""

  - name: "folder"
    type: "varies"
    description: ""

  - name: "hideInBundle"
    type: "boolean, string"
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

  - name: "isPrivate"
    type: "boolean, string"
    description: ""

  - name: "lastModifiedDate"
    type: "date-time"
    description: ""

  - name: "mediaFile"
    type: "varies"
    description: ""

  - name: "mediaTypeName"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "owner"
    type: "varies"
    description: ""

  - name: "siteCategoryList"
    type: "varies"
    description: ""

  - name: "siteDescription"
    type: "string"
    description: ""

  - name: "storeDisplayThumbnail"
    type: "varies"
    description: ""

  - name: "textFileEncoding"
    type: "varies"
    description: ""

  - name: "url"
    type: "string"
    description: ""

  - name: "urlComponent"
    type: "string"
    description: ""
---
