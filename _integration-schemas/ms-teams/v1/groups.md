---
tap: "ms-teams"
version: "1"
key: "group"

name: "groups"
doc-link: "https://docs.microsoft.com/en-us/graph/teams-list-all-teams?context=graph%2Fapi%2Fbeta&view=graph-rest-beta"
singer-schema: "https://github.com/singer-io/tap-ms-teams/blob/master/tap_ms_teams/schemas/groups.json"
description: |
  The `{{ table.name }}` table contains information about groups in your organization within your Microsoft account. Some old teams in your account will not have a `resource_provisioning_options` value. For more information, refer to [Microsoft's docs](https://docs.microsoft.com/en-us/graph/known-issues#missing-teams-in-list-all-teams){:target="new"}.

replication-method: "Full Table"

api-method:
  name: "Get a list of groups"
  doc-link: "https://docs.microsoft.com/en-us/graph/teams-list-all-teams?context=graph%2Fapi%2Fbeta&view=graph-rest-beta"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The group ID."
    foreign-key-id: "group-id"

  - name: "classification"
    type: "string"
    description: ""

  - name: "created_date_time"
    type: "date-time"
    description: ""

  - name: "creation_options"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "deleted_date_time"
    type: "date-time"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "display_name"
    type: "string"
    description: ""

  - name: "expiration_date_time"
    type: "date-time"
    description: ""

  - name: "group_types"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "is_assignable_to_role"
    type: "boolean"
    description: ""

  - name: "mail"
    type: "string"
    description: ""

  - name: "mail_enabled"
    type: "boolean"
    description: ""

  - name: "mail_nickname"
    type: "string"
    description: ""

  - name: "membership_rule"
    type: "string"
    description: ""

  - name: "membership_rule_processing_state"
    type: "string"
    description: ""

  - name: "onPremises_domain_name"
    type: "string"
    description: ""

  - name: "on_premises_last_sync_date_time"
    type: "date-time"
    description: ""

  - name: "on_premises_net_bios_name"
    type: "string"
    description: ""

  - name: "on_premises_provisioning_errors"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "on_premises_sam_account_name"
    type: "string"
    description: ""

  - name: "on_premises_security_identifier"
    type: "string"
    description: ""

  - name: "on_premises_sync_enabled"
    type: "boolean"
    description: ""

  - name: "preferred_data_location"
    type: "string"
    description: ""

  - name: "preferred_language"
    type: "string"
    description: ""

  - name: "proxy_addresses"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "renewed_date_time"
    type: "date-time"
    description: ""

  - name: "resource_behavior_options"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "resource_provisioning_options"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "security_edentifier"
    type: "string"
    description: ""

  - name: "security_enabled"
    type: "boolean"
    description: ""

  - name: "theme"
    type: "string"
    description: ""

  - name: "visibility"
    type: "string"
    description: ""
---