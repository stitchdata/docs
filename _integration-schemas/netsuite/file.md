---
tap: "netsuite"
version: "1.0"

name: "File"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/file.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/File.json"
description: |
  The `{{ table.name }}` table contains info about the files in your {{ integration.display_name }} File Cabinet.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "file"

replication-method: "Key-based Incremental"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "file-id"

  - name: "lastModifiedDate"
    type: "date-time"
    replication-key: true
    description: ""

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

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "isOnline"
    type: "boolean, string"
    description: ""

  - name: "isPrivate"
    type: "boolean, string"
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