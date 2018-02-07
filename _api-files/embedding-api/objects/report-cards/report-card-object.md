---
content-type: "embed-structure"
key: "report-card-object"

title: "Report Cards"
description: "A report card object contains information about a connection's configuration."

object-attributes:
  - name: "current_step"
    type: "integer"
    description: "The current step needed to configure the data source."

  - name: "current_step_hints"
    type: "current step hints object"
    url: "{{ page.anchors.data-structures.current-step-hints }}"
    description: |
      If the current step requires the user to interact with the Stitch interface, this object will provide the function to call and properties to pass to [Stitch.js]({{ page.anchors.stitch-js.section }}).

      Otherwise, this object will provide information about the next call to make to the {{ page.api-name }}.

  - name: "steps"
    type: "array"
    description: "A sequential list of [Connection Step objects]({{ page.anchors.data-structures.connection-steps }}) required to complete configuration for the connection type."

  - name: "type"
    type: "string"
    description: "The connection type."
---