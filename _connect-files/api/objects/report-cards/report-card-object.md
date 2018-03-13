---
content-type: "api-structure"
key: "report-card-object"

title: "Report Cards"
description: "{{ api.data-structures.report-cards.description }}"

object-attributes:
  - name: "current_step"
    type: "integer"
    description: "The current step needed to configure the data source."

  - name: "current_step_hints"
    type: "object"
    sub-type: "current step hints "
    url: "{{ api.data-structures.current-step-hints.section }}"
    description: |
      If the current step requires the user to interact with the Stitch interface, this object will provide the function to call and properties to pass to [Stitch.js]({{ js.section | flatify | prepend: site.baseurl }}).

      Otherwise, this object will provide information about the next call to make to the API.

  - name: "steps"
    type: "array"
    description: "A sequential list of [Connection Step objects]({{ api.data-structures.connection-steps.section }}) required to complete configuration for the connection type."

  - name: "type"
    type: "string"
    description: "The connection type."

examples:
  - code: |
      {
        "report_card":{
            "type":"platform.salesforce",
            "current_step":1,
            "steps":[{ }]
         }
      }
---