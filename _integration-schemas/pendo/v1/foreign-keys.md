---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "pendo"

version: "1"

foreign-keys:
  - id: "account-id"
    table: "accounts"
    attribute: "account_id"
    all-foreign-keys:
      - table: "accounts"
        join-on: "id"
      - table: "events"
      - table: "feature_events"
      - table: "guide_events"
      - table: "guide_events"
        subattribute: "account_ids"
        join-on: "value"
      - table: "page_events"
      - table: "poll_events"
      - table: "poll_events"
        subattribute: "account_ids"
        join-on: "value"
      - table: "track_events"
      - table: "visitors"
        subattribute: "metadata_auto.accountid"
      - table: "visitors"
        subattribute: "metadata_auto.accountids"
        join-on: "value"

  - id: "app-id"
    table: ""
    attribute: "app_id"
    all-foreign-keys:
      - table: "events"
      - table: "feature_events"
      - table: "features"
        subattribute: "created_by_user"
      - table: "guide_events"
      - table: "page_events"
      - table: "track_events"
      - table: "visitor_history"

  - id: "feature-id"
    table: ""
    attribute: "feature_id"
    all-foreign-keys:
      - table: "events"
      - table: "feature_events"
      - table: "features"
        join-on: "id"
      - table: "visitor_history"

  - id: "group-id"
    table: ""
    attribute: "group.id"
    all-foreign-keys:
      - table: "features"
      - table: "pages"
      - table: "track_types"

  - id: "guide-id"
    table: "guides"
    attribute: "guide_id"
    all-foreign-keys:
      - table: "guide_events"
      - table: "guides"
        join-on: "id"
      - table: "guides"
        subattribute: "steps"
      - table: "poll_events"
      - table: "visitor_history"

  - id: "guide-step-id"
    table: "guides"
    attribute: "id"
    all-foreign-keys:
      - table: "guides"
        subattribute: "steps"
      - table: "visitor_history"

  - id: "page-id"
    table: ""
    attribute: "page_id"
    all-foreign-keys:
      - table: "events"
      - table: "feature_events"
      - table: "features"
      - table: "guides"
        subattribute: "steps"
      - table: "page_events"
      - table: "pages"
      - table: "visitor_history"

  - id: "poll-id"
    table: ""
    attribute: "poll_id"
    all-foreign-keys:
      - table: "guide_events"
      - table: "poll_events"

  - id: "track-type-id"
    table: "track_types"
    attribute: "track_type_id"
    all-foreign-keys:
      - table: "track_events"
      - table: "track_types"
        join-on: "id"

  - id: "user-id"
    table: ""
    attribute: "id"
    all-foreign-keys:
      - table: "features"
        subattribute: "created_by_user"
      - table: "features"
        subattribute: "group.created_by_user"
      - table: "features"
        subattribute: "group.last_updated_by_user"
      - table: "features"
        subattribute: "last_updated_by_user"
      - table: "guides"
        subattribute: "created_by_user"
      - table: "guides"
        subattribute: "lastUpdated_by_user"
      - table: "pages"
        subattribute: "created_by_user"
      - table: "pages"
        subattribute: "group.created_by_user"
      - table: "pages"
        subattribute: "group.last_updated_by_user"
      - table: "pages"
        subattribute: "last_updated_by_user"
      - table: "track_types"
        subattribute: "created_by_user"
      - table: "track_types"
        subattribute: "last_updated_by_user"

  - id: "visitor-id"
    table: "visitors"
    attribute: "visitor_id"
    all-foreign-keys:
      - table: "events"
      - table: "feature_events"
      - table: "guide_events"
      - table: "guides"
        subattribute: "audience.select"
      - table: "page_events"
      - table: "poll_events"
      - table: "track_events"
      - table: "visitor_history"
      - table: "visitors"
---