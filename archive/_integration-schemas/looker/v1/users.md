---
tap: "looker"
version: "1"
key: "user"

name: "users"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/users.json"
description: |
  The `{{ table.name }}` table contains info about users associated with your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "Get all users"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/user#get_all_users"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The user ID."
    foreign-key-id: "user-id"

  - name: "avatar_url"
    type: "string"
    description: ""

  - name: "avatar_url_without_sizing"
    type: "string"
    description: ""

  - name: "credentials_api3"
    type: "array"
    description: ""
    subattributes:
      - name: "client_id"
        type: "string"
        description: ""

      - name: "created_at"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""

      - name: "is_disabled"
        type: "boolean"
        description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""

  - name: "credentials_email"
    type: "object"
    description: ""
    subattributes:
      - name: "created_at"
        type: "string"
        description: ""

      - name: "email"
        type: "string"
        description: ""

      - name: "forced_password_reset_at_next_login"
        type: "boolean"
        description: ""

      - name: "is_disabled"
        type: "boolean"
        description: ""

      - name: "logged_in_at"
        type: "string"
        description: ""

      - name: "password_reset_url"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""

      - name: "user_url"
        type: "string"
        description: ""

  - name: "credentials_embed"
    type: "array"
    description: ""
    subattributes:
      - name: "created_at"
        type: "string"
        description: ""

      - name: "external_group_id"
        type: "string"
        description: ""

      - name: "external_user_id"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""

      - name: "is_disabled"
        type: "boolean"
        description: ""

      - name: "logged_in_at"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""

  - name: "credentials_google"
    type: "object"
    description: ""
    subattributes:
      - name: "created_at"
        type: "string"
        description: ""

      - name: "domain"
        type: "string"
        description: ""

      - name: "email"
        type: "string"
        description: ""

      - name: "google_user_id"
        type: "string"
        description: ""

      - name: "is_disabled"
        type: "boolean"
        description: ""

      - name: "logged_in_at"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""

  - name: "credentials_ldap"
    type: "object"
    description: ""
    subattributes:
      - name: "created_at"
        type: "string"
        description: ""

      - name: "email"
        type: "string"
        description: ""

      - name: "is_disabled"
        type: "boolean"
        description: ""

      - name: "ldap_dn"
        type: "string"
        description: ""

      - name: "ldap_id"
        type: "string"
        description: ""

      - name: "logged_in_at"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""

  - name: "credentials_looker_openid"
    type: "object"
    description: ""
    subattributes:
      - name: "created_at"
        type: "string"
        description: ""

      - name: "email"
        type: "string"
        description: ""

      - name: "is_disabled"
        type: "boolean"
        description: ""

      - name: "logged_in_at"
        type: "string"
        description: ""

      - name: "logged_in_ip"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""

      - name: "user_url"
        type: "string"
        description: ""

  - name: "credentials_oidc"
    type: "object"
    description: ""
    subattributes:
      - name: "created_at"
        type: "string"
        description: ""

      - name: "email"
        type: "string"
        description: ""

      - name: "is_disabled"
        type: "boolean"
        description: ""

      - name: "logged_in_at"
        type: "string"
        description: ""

      - name: "oidc_user_id"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""

  - name: "credentials_saml"
    type: "object"
    description: ""
    subattributes:
      - name: "created_at"
        type: "string"
        description: ""

      - name: "email"
        type: "string"
        description: ""

      - name: "is_disabled"
        type: "boolean"
        description: ""

      - name: "logged_in_at"
        type: "string"
        description: ""

      - name: "saml_user_id"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""

  - name: "credentials_totp"
    type: "object"
    description: ""
    subattributes:
      - name: "created_at"
        type: "string"
        description: ""

      - name: "is_disabled"
        type: "boolean"
        description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""

      - name: "verified"
        type: "boolean"
        description: ""

  - name: "display_name"
    type: "string"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "embed_group_space_id"
    type: "string"
    description: ""

  - name: "first_name"
    type: "string"
    description: ""

  - name: "group_ids"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "integer"
        description: ""
        foreign-key-id: "group-id"

  - name: "home_folder_id"
    type: "string"
    description: ""
    foreign-key-id: "folder-id"

  - name: "home_space_id"
    type: "string"
    description: ""
    foreign-key-id: "space-id"

  - name: "is_disabled"
    type: "boolean"
    description: ""

  - name: "last_name"
    type: "string"
    description: ""

  - name: "locale"
    type: "string"
    description: ""

  - name: "looker_versions"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""
        foreign-key-id: "looker-version-id"

  - name: "models_dir_validated"
    type: "boolean"
    description: ""

  - name: "personal_folder_id"
    type: "string"
    description: ""
    foreign-key-id: "folder-id"

  - name: "personal_space_id"
    type: "string"
    description: ""
    foreign-key-id: "space-id"

  - name: "presumed_looker_employee"
    type: "boolean"
    description: ""

  - name: "role_ids"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "integer"
        description: ""
        foreign-key-id: "role-id"

  - name: "roles_externally_managed"
    type: "boolean"
    description: ""

  - name: "sessions"
    type: "array"
    description: ""
    subattributes:
      - name: "browser"
        type: "string"
        description: ""

      - name: "city"
        type: "string"
        description: ""

      - name: "country"
        type: "string"
        description: ""

      - name: "created_at"
        type: "string"
        description: ""

      - name: "credentials_type"
        type: "string"
        description: ""

      - name: "expires_at"
        type: "string"
        description: ""

      - name: "extended_at"
        type: "string"
        description: ""

      - name: "extended_count"
        type: "integer"
        description: ""

      - name: "id"
        type: "string"
        description: ""
        foreign-key-id: "user-session-id"

      - name: "ip_address"
        type: "string"
        description: ""

      - name: "operating_system"
        type: "string"
        description: ""

      - name: "state"
        type: "string"
        description: ""

      - name: "sudo_user_id"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""

  - name: "ui_state"
    type: "object"
    description: ""

  - name: "url"
    type: "string"
    description: ""

  - name: "verified_looker_employee"
    type: "boolean"
    description: ""
---