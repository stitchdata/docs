---
tap: "looker"
version: "1"
key: "connection"

name: "connections"
doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/connection#get_all_connections"
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/connections.json"
description: |
  The `{{ table.name }}` table contains information about connections in your {{ integration.display_name }} account.
  
replication-method: "Full Table"

api-method:
  name: "Get all connections"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/connection#get_all_connections"

attributes:
  - name: "name"
    type: "string"
    primary-key: true
    description: "The name of the connection."
    # foreign-key-id: "connection-name"

  - name: "after_connect_statements"
    type: "string"
    description: ""

  - name: "certificate"
    type: "string"
    description: ""

  - name: "created_at"
    type: "string"
    description: ""

  - name: "database"
    type: "string"
    description: ""

  - name: "db_timezone"
    type: "string"
    description: ""

  - name: "dialect"
    type: "object"
    description: ""
    subattributes:
      - name: "automatically_run_sql_runner_snippets"
        type: "boolean"
        description: ""

      - name: "connection_tests"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "label"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "persistent_table_distkey"
        type: "string"
        description: ""

      - name: "persistent_table_indexes"
        type: "string"
        description: ""

      - name: "persistent_table_sortkeys"
        type: "string"
        description: ""

      - name: "supports_cost_estimate"
        type: "boolean"
        description: ""

      - name: "supports_inducer"
        type: "boolean"
        description: ""

      - name: "supports_streaming"
        type: "boolean"
        description: ""

      - name: "supports_upload_tables"
        type: "boolean"
        description: ""

  - name: "dialect_name"
    type: "string"
    description: ""

  - name: "example"
    type: "boolean"
    description: ""

  - name: "file_type"
    type: "string"
    description: ""

  - name: "host"
    type: "string"
    description: ""

  - name: "jdbc_additional_params"
    type: "string"
    description: ""

  - name: "last_reap_at"
    type: "integer"
    description: ""

  - name: "last_regen_at"
    type: "integer"
    description: ""

  - name: "maintenance_cron"
    type: "string"
    description: ""

  - name: "max_billing_gigabytes"
    type: "number"
    description: ""

  - name: "max_connections"
    type: "integer"
    description: ""
  
  - name: "password"
    type: "string"
    description: ""

  - name: "pdt_context_override"
    type: "object"
    description: ""
    subattributes:
      - name: "after_connect_statements"
        type: "string"
        description: ""

      - name: "certificate"
        type: "string"
        description: ""

      - name: "context"
        type: "string"
        description: ""

      - name: "database"
        type: "string"
        description: ""

      - name: "file_type"
        type: "string"
        description: ""

      - name: "has_password"
        type: "boolean"
        description: ""

      - name: "host"
        type: "string"
        description: ""

      - name: "jdbc_additional_params"
        type: "string"
        description: ""

      - name: "password"
        type: "string"
        description: ""

      - name: "port"
        type: "string"
        description: ""

      - name: "schema"
        type: "string"
        description: ""

      - name: "username"
        type: "string"
        description: ""

  - name: "pool_timeout"
    type: "integer"
    description: ""

  - name: "port"
    type: "string"
    description: ""

  - name: "query_timezone"
    type: "string"
    description: ""

  - name: "schema"
    type: "string"
    description: ""

  - name: "snippets"
    type: "array"
    description: ""
    subattributes:
      - name: "label"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "sql"
        type: "string"
        description: ""

  - name: "sql_runner_precache_tables"
    type: "boolean"
    description: ""

  - name: "ssl"
    type: "boolean"
    description: ""

  - name: "tmp_db_name"
    type: "string"
    description: ""

  - name: "user_attribute_fields"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "user_db_credentials"
    type: "boolean"
    description: ""

  - name: "user_id"
    type: "string"
    description: ""
    foreign-key-id: "user-id"

  - name: "username"
    type: "string"
    description: ""

  - name: "uses_oauth"
    type: "boolean"
    description: ""

  - name: "verify_ssl"
    type: "boolean"
    description: ""
---