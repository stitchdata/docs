---
tap: "hubspot"
version: "01-03-2017"

name: "owners"
doc-link: https://developers.hubspot.com/docs/methods/owners/owners_overview
singer-schema: https://github.com/singer-io/tap-hubspot/blob/v0.11.0/tap_hubspot/schemas/owners.json
description: |
  The `owners` table contains info about the owners that exist in your HubSpot portal. Owners are created and updated in HubSpot when new users are added or when owners are synced from Salesforce to HubSpot.

notes: 

replication-method: "Incremental"
api-method:
  name: getOwners
  doc-link: https://developers.hubspot.com/docs/methods/owners/get_owners

attributes:
## Primary Key
  - name: "ownerId"
    type: "integer"
    primary-key: true
    description: "The ID of the owner."

  - name: "portalId"
    type: "integer"
    primary-key: true
    description: "The ID of the portal the owner is associated with."

## Replication Key
  - name: "updatedAt"
    type: "date-time"
    replication-key: true
    description: "The time that the owner was last updated in {{ integration.display_name }}."

  - name: "type"
    type: "string"
    description: "The type of owner. For example: `person`"

  - name: "firstName"
    type: "string"
    description: "The first name of the owner."

  - name: "lastName"
    type: "string"
    description: "The last name of the owner."

  - name: "email"
    type: "string"
    description: "The email address associated with the owner."

  - name: "createdAt"
    type: "date-time"
    description: "The time that the owner was created in {{ integration.display_name }}."

  - name: "remoteList"
    type: "array"
    description: "Details about the remote list associated with the owner."
    array-attributes:
      - name: "portalId"
        type: "integer"
        description: "The ID of the portal the owner is associated with."

      - name: "ownerId"
        type: "integer"
        description: "The ID of the owner."

      - name: "remoteId"
        type: "string"
        description: "The ID of the remote list."

      - name: "remoteType"
        type: "string"
        description: "The remote list type."

      - name: "active"
        type: "boolean"
        description: "Indicates if the owner is active."
---