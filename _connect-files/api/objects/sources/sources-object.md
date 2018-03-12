---
content-type: "embed-object"
endpoint: "sources"

title: "Source"
description: "Sources are the databases, APIs, and other data applications that Stitch replicates data from. Sources can be retrieved in a list or individually by ID."
endpoint-url: "/sources"
version: "4"

object-attributes:
  - name: "id"
    type: "integer"
    description: "The unique identifier for this source."

  - name: "created_at"
    type: "timestamp"
    description: "The time at which the source object was created."

  - name: "deleted_at"
    type: "timestamp"
    description: "The time at which the source object was deleted."

  - name: "display_name"
    type: "string"
    description: "The display name of the source connection."

  - name: "name"
    type: "string"
    description: |
      The name of the source connection, dynamically generated from `display_name`. The `name` corresponds to the schema name (for Postgres, Redshift, and Panoply destinations) or data set name (for BigQuery destinations) that the data from this source will be loaded into.

      Names must:
        - Contain only lowercase alphanumerics and underscores
        - Be unique within each Stitch client account

  - name: "paused_at"
    type: "timestamp"
    description: "If the connection was paused by the user, the time the pause began. Otherwise, or if the connection is active, this will be null."

  - name: "properties"
    type: "source form properties object"
    url: "{{ page.anchors.form-properties.source-forms.section }}"
    description: "The properties required to configure this source."

  - name: "report_card"
    type: "report card object"
    url: "{{ page.anchors.data-structures.report-cards }}"
    description: "A description of the source's configuration state."

  - name: "stitch_client_id"
    type: "integer"
    description: "The ID of the Stitch client account."

  - name: "system_paused_at"
    type: "timestamp"
    description: "If the connection was paused by the system, the time the pause began. Otherwise, or if the connection is active, this will be null."

  - name: "type"
    type: "string"
    description: "The source type."

  - name: "updated_at"
    type: "timestamp"
    description: "The time at which the object was last updated."
---