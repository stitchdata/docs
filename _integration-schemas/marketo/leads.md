---
tap: "marketo"
version: "2.0"

name: "leads"
doc-link: http://developers.marketo.com/rest-api/endpoint-reference/lead-database-endpoint-reference/#!/Leads/getLeadsByFilterUsingGET
singer-schema:
description: |
  The `{{ table.name }}` table contains info about your {{ integration.display_name }} leads.

  #### {{ integration.display_name }} Corona and Replication Method for Leads

  Stitch replicates leads from {{ integration.display_name }} using the Bulk API. The replication method for this table will vary depending on your {{ integration.display_name }} account setup:

  - **If Corona is enabled**, this table will use Incremental Replication based on an `updatedAt` timestamp included in the API query. 
  - **If Corona isn't enabled**, this table will use Full Table Replication.

  [Read more about Corona](#corona-replication).

replication-method: "Key-based Incremental"
replication-key:
  name: "updatedAt"

api-method:
  name: "getLeads"
  doc-link: "http://developers.marketo.com/rest-api/endpoint-reference/lead-database-endpoint-reference/#!/Leads/getLeadsByFilterUsingGET"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the lead."
    foreign-key-id: "lead-id"

  - name: "acquiredBy"
    type: "boolean"
    description: "Indicates if the lead was acquired by the parent program."

  - name: "isExhausted"
    type: "boolean"
    description: "Indicates if the lead is currently exhausted in the stream, if applicable."

  - name: "membershipDate"
    type: "date"
    description: "The date the lead first became a member of the program."

  - name: "nurtureCadence"
    type: "string"
    description: "Cadence of the parent stream, if applicable."

  - name: "progressionStatus"
    type: "string"
    description: "The program status of the lead in the parent program."

  - name: "reachedSuccess"
    type: "boolean"
    description: "Indicates if the the lead is in a success-status in the parent program."

  - name: "reachedSuccessDate"
    type: "string"
    description: "The date the lead reached success in the parent program."

  - name: "stream"
    type: "string"
    description: "The stream that the lead is a member of, if the parent program is an engagement program."
---