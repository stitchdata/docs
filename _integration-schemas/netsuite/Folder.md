---
tap: "netsuite"
# version: "1.0"

name: "Folder"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Folder.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
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
