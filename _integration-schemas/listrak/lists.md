---
tap: "listrak"
# version: ""

name: "lists"
doc-link:
singer-schema: https://github.com/singer-io/tap-listrak/blob/master/tap_listrak/schemas/lists.json
description: |
  The `lists` table contains info about contact lists.

replication-method: "Full Table"

api-method:
  name: "GetContactListCollection"
  doc-link: https://webservices.listrak.com/v31/IntegrationService.asmx?op=GetContactListCollection

attributes:
  - name: "ListID"
    type: "integer"
    description: ""

  - name: "EnableGoogleAnalytics"
    type: "boolean"
    description: ""

  - name: "GoogleTrackingDomains"
    type: "object"
    description: ""

    object-attributes: 
  - name: "GoogleTrackingDomains"
    type: "string"
    description: ""

  - name: "EnableInternationalization"
    type: "boolean"
    description: ""

  - name: "ListName"
    type: "string"
    description: ""

  - name: "bounceHandling"
    type: "integer"
    description: ""

  - name: "CreateDate"
    type: "string"
    description: ""

  - name: "ShowEmailList"
    type: "boolean"
    description: ""

  - name: "BounceUnsubscribeCount"
    type: "integer"
    description: ""

  - name: "EnableRSS"
    type: "boolean"
    description: ""

  - name: "Vmta"
    type: "object"
    description: ""

    object-attributes: 
    - name: "Description"
      type: "string"
      description: ""

    - name: "VmtaID"
      type: "integer"
      description: ""

  - name: "EnableDoubleOptin"
    type: "boolean"
    description: ""

  - name: "EnableListHygiene"
    type: "boolean"
    description: ""

  - name: "DomainAliasLink"
    type: "string"
    description: ""

  - name: "EnableListRemoveHeader"
    type: "boolean"
    description: ""

  - name: "EnableDynamicContent"
    type: "boolean"
    description: ""

  - name: "EnableBrowserLink"
    type: "boolean"
    description: ""

  - name: "EnableRemovalLink"
    type: "boolean"
    description: ""

  - name: "FromName"
    type: "string"
    description: ""

  - name: "FromEmail"
    type: "string"
    description: ""

  - name: "ShowAdvancedPersonalization"
    type: "boolean"
    description: ""

  - name: "DomainAliasEmail"
    type: "string"
    description: ""
