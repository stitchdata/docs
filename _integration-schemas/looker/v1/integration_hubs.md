---
tap: "looker"
version: "1"
key: ""
name: "integration_hubs"
doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/integration#get_all_integration_hubs"
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/integration_hubs.json"
description: |
  The `{{ table.name }}` table contains information about Integration Hubs in your {{ integration.display_name }} account.
  
replication-method: "Full Table"

api-method:
    name: "Get All Integration Hubs"
    doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/integration#get_all_integration_hubs"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The Integration Hub ID."

  - name: "authorization_token"
    type: "string"
    description: ""
  - name: "fetch_error_message"
    type: "string"
    description: ""
  - name: "has_authorization_token"
    type: "boolean"
    description: ""
  
  - name: "label"
    type: "string"
    description: ""
  - name: "legal_agreement_required"
    type: "boolean"
    description: ""
  - name: "legal_agreement_signed"
    type: "boolean"
    description: ""
  - name: "legal_agreement_text"
    type: "string"
    description: ""
  - name: "official"
    type: "boolean"
    description: ""
  - name: "url"
    type: "string"
    description: ""
---
