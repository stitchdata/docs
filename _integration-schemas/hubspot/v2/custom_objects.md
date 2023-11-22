---
tap: "hubspot"
version: "2"
key: "custom-objects"

name: "custom_objects"
doc-link: "https://developers.hubspot.com/docs/api/crm/crm-custom-objects"
singer-schema: https://github.com/singer-io/tap-hubspot/tree/master/tap_hubspot/schemas/custom_objects.json
description: | 
  Tables for custom CRM objects in your {{ integration.display_name }} account will be named following the pattern `custom_<object_name>`. For example, if you have a custom object named `cars`, the table will be named `custom_cars`.

  The fields listed below are standard fields; they are included in every custom object table. A field will be added for each property you select when configuring the table. The property names will be prefixed with `property_`. For example, if you have a property named `model`, it will appear as `property_model`.

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

  - name: "updatedAt"
    type: "string"
    format: "date-time"
    description: ""
    replication-key: true
---