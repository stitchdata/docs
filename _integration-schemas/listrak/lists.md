---
tap: "listrak"
# version: ""

name: "lists"
doc-link:
singer-schema: https://github.com/singer-io/tap-listrak/blob/master/tap_listrak/schemas/lists.json
description: |
  The `lists` table contains info about your contact lists.

replication-method: "Full Table"

api-method:
  name: "GetContactListCollection"
  doc-link: https://webservices.listrak.com/v31/IntegrationService.asmx?op=GetContactListCollection

attributes:
  - name: "ListID"
    type: "integer"
    primary-key: true
    description: "The list ID."
    foreign-key-id: "list-id"

  - name: "bounceHandling"
    type: "integer"
    description: "Indicates how bounces are handled for the list."

  - name: "BounceUnsubscribeCount"
    type: "integer"
    description: "The number of bounces allowed before being automatically unsubscribed from the list."

  - name: "CreateDate"
    type: "string"
    description: "The time the list was created."

  - name: "DomainAliasEmail"
    type: "string"
    description: "The alias email for emails in the list's messages."

  - name: "DomainAliasLink"
    type: "string"
    description: "The alias domain for links in the list's messages."

  - name: "EnableBrowserLink"
    type: "boolean"
    description: "If `true`, browser links are enabled for the list."

  - name: "EnableDoubleOptin"
    type: "boolean"
    description: "If `true`, double opt-in is enabled for the list."

  - name: "EnableDynamicContent"
    type: "boolean"
    description: "If `true`, dynamic content is enabled for the list."

  - name: "EnableGoogleAnalytics"
    type: "boolean"
    description: "If `true`, Google Analytics is enabled for the list."

  - name: "EnableInternationalization"
    type: "boolean"
    description: "If `true`, internationalization is enabled for the list."

  - name: "EnableListHygiene"
    type: "boolean"
    description: "If `true`, list hygiene is enabled for the list."

  - name: "EnableListRemoveHeader"
    type: "boolean"
    description: "If `true`, unsubscribe information is automatically included in message headers."

  - name: "EnableRemovalLink"
    type: "boolean"
    description: "If `true`, list removal links are automatically included for the list."

  - name: "EnableRSS"
    type: "boolean"
    description: "If `true`, RSS is enabled for the list."

  - name: "FromName"
    type: "string"
    description: "The `From` name used by default when sending messages to the list."

  - name: "FromEmail"
    type: "string"
    description: "The `From` email used by default when sending messages to the list."

  - name: "GoogleTrackingDomains"
    type: "array"
    description: "The Google tracking domains associated with the list."
    subattributes: 
      - name: "GoogleTrackingDomains"
        type: "string"
        primary-key: true
        description: "The Google tracking domain."

  - name: "ListName"
    type: "string"
    description: "The name of the list."

  - name: "ShowAdvancedPersonalization"
    type: "boolean"
    description: "If `true`, advanced personalization is enabled for the list."

  # Commenting out undocumented fields - not in Listrak's docs

  # - name: "ShowEmailList"
  #   type: "boolean"
  #   description: "If `true`, "

  # - name: "Vmta"
  #   type: "object"
  #   description: ""
  #   subattributes: 
  #     - name: "Description"
  #       type: "string"
  #       description: ""

  #     - name: "VmtaID"
  #       type: "integer"
  #       description: ""
---