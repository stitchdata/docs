---
tap-reference: "uservoice"

version: "1.0"

foreign-keys:
  - id: "category-id"
    attribute: "category"
    table: "categories"
    all-foreign-keys:
      - table: "categories"
        join-on: "id"
        
      - table: "suggestions"
        subattribute: "links"

  - id: "comment-id"
    attribute: "comment"
    table: "comments"
    all-foreign-keys:
      - table: "comments"
        join-on: "id"

  - id: "external-account-id"
    attribute: ""
    table: "external_accounts"
    all-foreign-keys:
      - table: "external_accounts"
        join-on: "id"

      - table: "external_users"
        subattribute: "links"
        join-on: "external_accounts"

  - id: "external-user-id"
    attribute: "external_user"
    table: "external_users"
    all-foreign-keys:
      - table: "external_users"
        join-on: "id"

      - table: "users"
        subtable: "links__external_users"
        join-on: "value"

  - id: "feature-status-id"
    attribute: "feature_status"
    table: "feature_statuses"
    all-foreign-keys:
      - table: "features"
        subattribute: "links"

      - table: "feature_statuses"
        join-on: "id"

  - id: "forum-id"
    attribute: "forum"
    table: "forums"
    all-foreign-keys:
      - table: "categories"
        subattribute: "links"

      - table: "forums"
        join-on: "id"
      - table: "suggestions"
        subattribute: "links"

  - id: "label-id"
    attribute: ""
    table: "labels"
    all-foreign-keys:
      - table: "labels"
        join-on: "id"

      - table: "labels"
        subattribute: "links"
        join-on: "parent"

      - table: "suggestions"
        subtable: "links__labels"
        join-on: "value"

  - id: "nps-rating-id"
    attribute: ""
    table: "nps_ratings"
    all-foreign-keys:
      - table: "nps_ratings"
        join-on: "id"

  - id: "product-area-id"
    attribute: "product_area"
    table: "product_areas"
    all-foreign-keys:
      - table: "features"
        links: "product_area"

      - table: "product_areas"
        join-on: "id"

  - id: "request-id"
    attribute: ""
    table: "requests"
    all-foreign-keys:
      - table: "requests"
        join-on: "id"

  - id: "segmented-value-id"
    attribute: ""
    table: "segmented_values"
    all-foreign-keys:
      - table: "segmented_values"
        join-on: "id"

  - id: "segment-id"
    attribute: "segment"
    table: "segments"
    all-foreign-keys:
      - table: "segments"
        join-on: "id"

  - id: "status-id"
    attribute: ""
    table: "statuses"
    all-foreign-keys:
      - table: "status_updates"
        subattribute: "links"
        join-on: "new_status"

      - table: "status_updates"
        subattribute: "links"
        join-on: "old_status"

      - table: "statuses"
        join-on: "id"

      - table: "suggestions"
        subattribute: "links"

  - id: "status-update-id"
    attribute: ""
    table: "status_updates"
    all-foreign-keys:
      - table: "status_updates"
        join-on: "id"

      - table: "suggestions"
        subattribute: "links"
        join-on: "last_status_update"

  - id: "suggestion-id"
    attribute: "suggestion"
    table: "suggestions"
    all-foreign-keys:
      - table: "comments"
        subattribute: "links"

      - table: "requests"
        subattribute: "links"

      - table: "status_updates"
        subattribute: "links"

      - table: "suggestions"
        join-on: "id"

      - table: "suggestions"
        subattribute: "links"
        join-on: "parent_suggestion"

      - table: "supporter-id"
        subattribute: "links"

  - id: "supporter-id"
    attribute: "supporter"
    table: "supporters"
    all-foreign-keys:
      - table: "requests"
        subattribute: "links"

      - table: "supporters"
        join-on: "id"

  - id: "team-id"
    attribute: "team"
    table: "teams"
    all-foreign-keys:
      - table: "teams"
        join-on: "id"

      - table: "users"
        subtable: "links__teams"
        join-on: "value"

  - id: "user-id"
    attribute: "user"
    table: "users"
    all-foreign-keys:
      - table: "comments"
        subattribute: "links"
        join-on: "created_by"

      - table: "features"
        subattribute: "links"
        join-on: "updated_by"

      - table: "features"
        subattribute: "links"
        join-on: "created_by"

      - table: "feature_statuses"
        subattribute: "links"
        join-on: "updated_by"

      - table: "feature_statuses"
        subattribute: "links"
        join-on: "created_by"

      - table: "forums"
        subattribute: "links"
        join-on: "updated_by"

      - table: "nps_ratings"
        subattribute: "links"

      - table: "product_areas"
        subattribute: "links"
        join-on: "updated_by"

      - table: "product_areas"
        subattribute: "links"
        join-on: "created_by"

      - table: "requests"
        subattribute: "links"

      - table: "requests"
        subattribute: "links"
        join-on: "created_by"

      - table: "requests"
        subattribute: "links"
        join-on: "updated_by"

      - table: "segmented_values"
        subattribute: "links"
        join-on: "created_by"

      - table: "segmented_values"
        subattribute: "links"
        join-on: "updated_by"

      - table: "status_updates"
        subattribute: "links"

      - table: "suggestions"
        subattribute: "links"
        join-on: "created_by"

      - table: "supporters"
        subattribute: "links"
        join-on: "created_by"

      - table: "supporters"
        subattribute: "links"
        join-on: "updated_by"

      - table: "supporters"
        subattribute: "links"

      - table: "users"
        join-on: "id"
---