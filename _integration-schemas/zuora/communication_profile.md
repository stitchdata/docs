---
tap: "zuora"
version: 1.0

name: "communicationProfile"
doc-link: https://live-www.zuora.com/developer/api-reference/#operation/Object_GETCommunicationProfile
#singer-schema: 
description: |
  The `{{ table.name }}` table contains information about communication profiles, which are sets of policies that determine how to communicate with the contacts associated with a specific customer account.

replication-method: "Key-based Incremental"
api-method:
  name:
  doc-link:

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The communication profile ID."
    foreign-key-id: "communication-profile-id"

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the communication profile was last updated."

  - name: "createdById"
    type: "string"
    description: "The ID of the Zuora user who created the communication profile."

  - name: "createdDate"
    type: "date-time"
    description: "The date when the communication profile was created."

  - name: "deleted"
    type: "boolean"
    description: |
      **Only supported for the AQuA API.** If `true`, this record was deleted in Zuora.

  - name: "description"
    type: "string"
    description: "The description of the communication profile."

  - name: "profileName"
    type: "string"
    description: "The name of the communication profile."

  - name: "updatedById"
    type: "string"
    description: "The ID of the Zuora user who last updated the communication profile."
---