---
tap: "looker"
version: "1"
key: "integration"

name: "integrations"
doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/integration#get_all_integrations"
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/integrations.json"
description: |
  The `{{ table.name }}` table contains information about all integrations in your {{ integration.display_name }} instance.
  
replication-method: "Full Table"

api-method:
  name: "Get all integrations"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/integration#get_all_integrations"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The integration ID."
    foreign-key-id: "integration-id"
    
  - name: "delegate_oauth"
    type: "boolean"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "enabled"
    type: "boolean"
    description: ""

  - name: "icon_url"
    type: "string"
    description: ""
  
  - name: "installed_delegate_oauth"
    type: "string"
    description: ""

  - name: "integration_hub_id"
    type: "string"
    description: ""
    foreign-key-id: "integration-hub-id"

  - name: "label"
    type: "string"
    description: ""

  - name: "params"
    type: "array"
    description: ""
    subattributes:
      - name: "delegate_oauth_url"
        type: "string"
        description: ""

      - name: "description"
        type: "string"
        description: ""

      - name: "has_value"
        type: "boolean"
        description: ""

      - name: "label"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "per_user"
        type: "boolean"
        description: ""

      - name: "required"
        type: "boolean"
        description: ""

      - name: "sensitive"
        type: "boolean"
        description: ""

      - name: "user_attribute_name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""

  - name: "required_fields"
    type: "array"
    description: ""
    subattributes:
      - name: "all_tags"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "any_tag"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "tag"
        type: "string"
        description: ""

  - name: "supported_action_types"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "supported_download_settings"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "supported_formats"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "supported_formattings"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "supported_visualization_formattings"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "uses_oauth"
    type: "boolean"
    description: ""
---