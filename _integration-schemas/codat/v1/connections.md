---
tap: "codat"
version: "1"
key: "connection"

name: "connections"
doc-link: "https://docs.codat.io/reference/connection#connection_getconnection"
singer-schema: "https://github.com/singer-io/tap-codat/blob/master/tap_codat/schemas/connections.json"
description: |
  The {{ table.name }} table contains information about company connections in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "Get connections"
  doc-link: "https://docs.codat.io/reference/connection#connection_getconnection"

attributes:
  - name: "companyId"
    type: "string"
    primary-key: true
    description: "The company ID."
    foreign-key-id: "company-id"

  - name: "id"
    type: "string"
    primary-key: true
    description: "The connection ID."
    foreign-key-id: "connection-id"

  - name: "integrationId"
    type: "string"
    description: ""

  - name: "linkUrl"
    type: "string"
    description: ""

  - name: "platformName"
    type: "string"
    description: ""

  - name: "sourceId"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""
---