---
content-type: "embed-structure"
key: "current-step-hint-object"

title: "Current Step Hint"
description: |
  The current step hint object provides the function to call and properties to pass to [Stitch.js](#stitch-js).

  Otherwise, this object will provide information about the next call to make to the {{ page.api-name }}.

object-attributes:
  - name: "api"
    type: "api-hints"
    description: "Describes the actions required to complete the current connection step using the {{ page.api-name }}, if applicable."

  - name: "js"
    type: "stitch-js-hints"
    description: "Describes the actions required to complete the current connection step using the Stitch.js, if applicable."
---