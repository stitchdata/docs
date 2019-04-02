---
tap: "netsuite"
# version: "1.0"

name: "EntityGroup"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/EntityGroup.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "comments"
    type: "string"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "groupName"
    type: "string"
    description: ""

  - name: "groupOwner"
    type: "varies"
    description: ""

  - name: "groupType"
    type: "varies"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "isFunctionalTeam"
    type: "boolean, string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "isManufacturingWorkCenter"
    type: "boolean, string"
    description: ""

  - name: "isPrivate"
    type: "boolean, string"
    description: ""

  - name: "isProductTeam"
    type: "boolean, string"
    description: ""

  - name: "isSalesRep"
    type: "boolean, string"
    description: ""

  - name: "isSalesTeam"
    type: "boolean, string"
    description: ""

  - name: "isSavedSearch"
    type: "boolean, string"
    description: ""

  - name: "isSupportRep"
    type: "boolean, string"
    description: ""

  - name: "issueRole"
    type: "varies"
    description: ""

  - name: "laborResources"
    type: "integer, string"
    description: ""

  - name: "machineResources"
    type: "integer, string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "parentGroupType"
    type: "varies"
    description: ""

  - name: "restrictionGroup"
    type: "varies"
    description: ""

  - name: "savedSearch"
    type: "varies"
    description: ""

  - name: "subsidiary"
    type: "varies"
    description: ""

  - name: "workCalendar"
    type: "varies"
    description: ""
---
