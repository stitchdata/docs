---
tap: "hubspot"
version: "2"
key: "custom-objects"

name: "custom_objects"
doc-link: ""
singer-schema: https://github.com/singer-io/tap-hubspot/tree/master/tap_hubspot/schemas/custom_objects.json
description: | 
  Tables for custom CRM objects in your {{ integration.display_name }} account will be named following the pattern `custom_<object_name>`. For example, if you have a custom object named `cars`, the table will be named `custom_cars`.

  The fields listed below are standard fields; they are included in every custom object table. 

replication-method: "Key-based Incremental"

table-key-properties: "id"
valid-replication-keys: "updatedAt"

attributes:
  - name: "archived"
    type: "boolean"
    description: ""

  - name: "associations"
    type: "object"
    description: ""
    subattributes:
    - name: "emails"
      type: "object"
      description: ""
      subattributes:
      - name: "results"
        type: "array"
        description: ""
        subattributes:
        - name: "id"
          type: "string"
          description: ""

        - name: "type"
          type: "string"
          description: ""



    - name: "meetings"
      type: "object"
      description: ""
      subattributes:
      - name: "results"
        type: "array"
        description: ""
        subattributes:
        - name: "id"
          type: "string"
          description: ""

        - name: "type"
          type: "string"
          description: ""



    - name: "notes"
      type: "object"
      description: ""
      subattributes:
      - name: "results"
        type: "array"
        description: ""
        subattributes:
        - name: "id"
          type: "string"
          description: ""

        - name: "type"
          type: "string"
          description: ""



    - name: "tasks"
      type: "object"
      description: ""
      subattributes:
      - name: "results"
        type: "array"
        description: ""
        subattributes:
        - name: "id"
          type: "string"
          description: ""

        - name: "type"
          type: "string"
          description: ""



    - name: "calls"
      type: "object"
      description: ""
      subattributes:
      - name: "results"
        type: "array"
        description: ""
        subattributes:
        - name: "id"
          type: "string"
          description: ""

        - name: "type"
          type: "string"
          description: ""



    - name: "conversation_session"
      type: "object"
      description: ""
      subattributes:
      - name: "results"
        type: "array"
        description: ""
        subattributes:
        - name: "id"
          type: "string"
          description: ""

        - name: "type"
          type: "string"
          description: ""



    - name: "companies"
      type: "object"
      description: ""
      subattributes:
      - name: "results"
        type: "array"
        description: ""
        subattributes:
        - name: "id"
          type: "string"
          description: ""

        - name: "type"
          type: "string"
          description: ""



    - name: "contacts"
      type: "object"
      description: ""
      subattributes:
      - name: "results"
        type: "array"
        description: ""
        subattributes:
        - name: "id"
          type: "string"
          description: ""

        - name: "type"
          type: "string"
          description: ""



    - name: "deals"
      type: "object"
      description: ""
      subattributes:
      - name: "results"
        type: "array"
        description: ""
        subattributes:
        - name: "id"
          type: "string"
          description: ""

        - name: "type"
          type: "string"
          description: ""



    - name: "products"
      type: "object"
      description: ""
      subattributes:
      - name: "results"
        type: "array"
        description: ""
        subattributes:
        - name: "id"
          type: "string"
          description: ""

        - name: "type"
          type: "string"
          description: ""



    - name: "tickets"
      type: "object"
      description: ""
      subattributes:
      - name: "results"
        type: "array"
        description: ""
        subattributes:
        - name: "id"
          type: "string"
          description: ""

        - name: "type"
          type: "string"
          description: ""




  - name: "createdAt"
    type: "string"
    format: "date-time"
    description: ""

  - name: "id"
    type: "string"
    description: ""
	  primary-key: true

  - name: "properties"
    type: "object"
    description: ""

    - name: "hs_all_accessible_team_ids"
      type: "string"
      description: ""

    - name: "hs_all_assigned_business_unit_ids"
      type: "string"
      description: ""

    - name: "hs_all_owner_ids"
      type: "string"
      description: ""

    - name: "hs_all_team_ids"
      type: "string"
      description: ""

    - name: "hs_created_by_user_id"
      type: "number, string"
      description: ""

    - name: "hs_createdate"
      type: "string"
      format: "date-time"
      description: ""

    - name: "hs_lastmodifieddate"
      type: "string"
      format: "date-time"
      description: ""

    - name: "hs_merged_object_ids"
      type: "string"
      description: ""

    - name: "hs_object_id"
      type: "number, string"
      description: ""

    - name: "hs_object_source"
      type: "string"
      description: ""

    - name: "hs_object_source_id"
      type: "string"
      description: ""

    - name: "hs_object_source_label"
      type: "string"
      description: ""

    - name: "hs_object_source_user_id"
      type: "number, string"
      description: ""

    - name: "hs_pinned_engagement_id"
      type: "number, string"
      description: ""

    - name: "hs_read_only"
      type: "boolean"
      description: ""

    - name: "hs_unique_creation_key"
      type: "string"
      description: ""

    - name: "hs_updated_by_user_id"
      type: "number, string"
      description: ""

    - name: "hs_user_ids_of_all_notification_followers"
      type: "string"
      description: ""

    - name: "hs_user_ids_of_all_notification_unfollowers"
      type: "string"
      description: ""

    - name: "hs_user_ids_of_all_owners"
      type: "string"
      description: ""

    - name: "hs_was_imported"
      type: "boolean"
      description: ""

    - name: "hubspot_owner_assigneddate"
      type: "string"
      format: "date-time"
      description: ""

    - name: "hubspot_owner_id"
      type: "string"
      description: ""

    - name: "hubspot_team_id"
      type: "string"
      description: ""

  - name: "property_hs_all_accessible_team_ids"
    type: "string"
    description: ""

  - name: "property_hs_all_assigned_business_unit_ids"
    type: "string"
    description: ""

  - name: "property_hs_all_owner_ids"
    type: "string"
    description: ""

  - name: "property_hs_all_team_ids"
    type: "string"
    description: ""

  - name: "property_hs_created_by_user_id"
    type: "number, string"
    description: ""

  - name: "property_hs_createdate"
    type: "string"
    format: "date-time"
    description: ""

  - name: "property_hs_lastmodifieddate"
    type: "string"
    format: "date-time"
    description: ""

  - name: "property_hs_merged_object_ids"
    type: "string"
    description: ""

  - name: "property_hs_object_id"
    type: "number, string"
    description: ""

  - name: "property_hs_object_source"
    type: "string"
    description: ""

  - name: "property_hs_object_source_id"
    type: "string"
    description: ""

  - name: "property_hs_object_source_label"
    type: "string"
    description: ""

  - name: "property_hs_object_source_user_id"
    type: "number, string"
    description: ""

  - name: "property_hs_pinned_engagement_id"
    type: "number, string"
    description: ""

  - name: "property_hs_read_only"
    type: "boolean"
    description: ""

  - name: "property_hs_unique_creation_key"
    type: "string"
    description: ""

  - name: "property_hs_updated_by_user_id"
    type: "number, string"
    description: ""

  - name: "property_hs_user_ids_of_all_notification_followers"
    type: "string"
    description: ""

  - name: "property_hs_user_ids_of_all_notification_unfollowers"
    type: "string"
    description: ""

  - name: "property_hs_user_ids_of_all_owners"
    type: "string"
    description: ""

  - name: "property_hs_was_imported"
    type: "boolean"
    description: ""

  - name: "property_hubspot_owner_assigneddate"
    type: "string"
    format: "date-time"
    description: ""

  - name: "property_hubspot_owner_id"
    type: "string"
    description: ""

  - name: "property_hubspot_team_id"
    type: "string"
    description: ""

  - name: "updatedAt"
    type: "string"
    format: "date-time"
    description: ""
	  replication-key: true


---