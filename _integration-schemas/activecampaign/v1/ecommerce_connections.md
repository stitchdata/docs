---
tap: "activecampaign"
version: "0.3"
key: ""

name: "ecommerce_connections"
doc-link: "https://developers.activecampaign.com/reference#connections"
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/ecommerce_connections.json"
description: |
  The `{{ table.name }}` table contains information about accounts within your {{ integration.display_name }} account that are linked to an external e-commerce service.

replication-method: "Key-based Incremental"

api-method:
    name: "List all connections"
    doc-link: "https://developers.activecampaign.com/reference#list-all-connections"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ecommerce connection ID."
    foreign-key-id: "connection-id"

  - name: "udate"
    type: "date-time"
    description: "The connection udate."
    replication-key: true

  - name: "cdate"
    type: "date-time"
    description: ""
  - name: "externalid"
    type: "string"
    description: ""
  
  - name: "is_internal"
    type: "integer"
    description: ""
  - name: "last_sync"
    type: "date-time"
    description: ""
  - name: "link_url"
    type: "string"
    description: ""
  - name: "logo_url"
    type: "string"
    description: ""
  - name: "name"
    type: "string"
    description: ""
  - name: "service"
    type: "string"
    description: ""
  - name: "status"
    type: "integer"
    description: ""
  - name: "sync_status"
    type: "integer"
    description: ""

---
