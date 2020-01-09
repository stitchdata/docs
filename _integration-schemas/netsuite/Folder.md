---
tap: "netsuite"
version: "1.0"

name: "Folder"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/folder.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Folder.json"
description: |
  The `{{ table.name }}` table contains info about the folders in your {{ integration.display_name }} File Cabinet.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "folder"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "folder-id"

  - name: "_class"
    type: "varies"
    description: ""

  - name: "bundleable"
    type: "boolean, string"
    description: ""

  - name: "department"
    type: "varies"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "folderType"
    type: "varies"
    description: ""

  - name: "group"
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

  - name: "location"
    type: "varies"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "parent"
    type: "varies"
    description: ""

  - name: "subsidiary"
    type: "varies"
    description: ""
---