---
tap: "hubspot"
version: "2"
key: "contact-list"

name: "contact_lists"
doc-link: https://developers.hubspot.com/docs/methods/lists/contact-lists-overview
singer-schema: https://github.com/singer-io/tap-hubspot/blob/master/tap_hubspot/schemas/contact_lists.json
description: |
  The `{{ table.name }}` table contains info about the contacts lists in your {{ integration.display_name }} account. Contact lists are used to segment contacts into groups, and there are two types: dynamic (smart lists) and static.

replication-method: "Key-based Incremental"
api-method:
  name: "Get contact lists"
  doc-link: https://developers.hubspot.com/docs/methods/lists/get_lists

attributes:
  - name: "listId"
    type: "integer"
    primary-key: true
    description: "The unique ID of the list."
    foreign-key-id: "contact-list-id"

  - name: "updatedAt"
    type: "date-time"
    replication-key: true
    description: "The time that the list was last updated."

  - name: "internalListId"
    type: "integer"
    description: "The list's internal list ID. This field has been deprecated by {{ integration.display_name }} - use `listId` in its place."

  - name: "parentId"
    type: "integer"
    description: "The ID of the folder that the list belongs to."

  - name: "metaData"
    type: "object"
    description: "Metadata about the contact list."
    subattributes:
      - name: "processing"
        type: "string"
        description: "Indicates the processing status of the contact list. "

      - name: "size"
        type: "integer"
        description: "The number of contacts in the list."

      - name: "error"
        type: "string"
        description: "Any errors that occurred the last time the list was processed."

      - name: "lastProcessingStateChangeAt"
        type: "date-time"
        description: "The last time that the processing status changed."

      - name: "lastSizeChangeAt"
        type: "date-time"
        description: "The last time that the size of the list changed."

  - name: "dynamic"
    type: "boolean"
    description: "Indicates if the contact list is a dynamic list."

  - name: "name"
    type: "string"
    description: "The name of the contact list."

  - name: "filters"
    type: "array"
    description: "A list of filters used to define list membership. For example: adding only contacts who have submitted a particular form."
    doc-link: https://developers.hubspot.com/docs/methods/lists/contact-lists-overview
    subattributes:
      - name: "value"
        type: "array"
        description: "Details about the filters used to define list membership."
        subattributes:
          - name: "filterFamily"
            type: "string"
            description: "The name of the filter family."

          - name: "withinTimeMode"
            type: "string"
            description: ""

          - name: "checkPastVersions"
            type: "boolean"
            description: "Indicates if past versions are checked."

          - name: "type"
            type: "string"
            description: "The type of the filter. For example: `string`"

          - name: "property"
            type: "string"
            description: "The property included in the filter. For example: `email`"

          - name: "value"
            type: "string"
            description: "The value of the filter."

          - name: "operator"
            type: "string"
            description: "The filter operator."

  - name: "portalId"
    type: "integer"
    description: "The ID of the portal the contact list belongs to."
    foreign-key-id: "portal-id"

  - name: "createdAt"
    type: "date-time"
    description: "The time that the list was created."

  - name: "readOnly"
    type: "boolean"
    description: "Indicates if the contact list is read-only."

  - name: "archived"
    type: "boolean"
    description: "Indicates if the contact list has been archived."

  - name: "deleteable"
    type: "boolean"
    description: "Indicates if the list can be deleted. If `false`, the list is a system list and cannot be deleted."

  - name: "listType"
    type: "string"
    description: "The type of list. For example: `static` or `dynamic`."
---