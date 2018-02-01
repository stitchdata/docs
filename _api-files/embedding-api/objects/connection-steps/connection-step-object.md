---
content-type: "embed-structure"
key: "connection-step-object"

title: "Connection Step"
description: "The connection steps object contains the steps necessary to configure a data source or destination."

object-attributes:
  - name: "type"
    type: "string"
    description: |
      The type of step. Possible values are:

      - `form`
      - `oauth`
      - `profile`
      - `discover_schema`
      - `field_selection`
      - `fully_configured`

  - name: "properties"
    type: "array"
    description: "An array of properties objects."
---