---
content-type: "embed-structure"
key: "connection-step-object"

title: "Connection Steps"
description: "The connection steps object contains the steps necessary to configure a data source or destination."

object-attributes:
  - name: "type"
    type: "string"
    description: |
      The type of step. Possible values are:

      - `form` - The first step in every source's creation.
      - `oauth` - If required, the OAuth step for the source's creation.
      - `profile` - 
      - `discover_schema` - The step in which Stitch performs a [structure sync](#terminology) to detect the tables and attributes available in the source.
      - `field_selection` - The step in which tables and columns are selected for replication.
      - `fully_configured` - Achieved when the source has a successful connection and `field_selection` is complete.

  - name: "properties"
    type: "array"
    description: "An array of properties objects."
---