---
content-type: "api-structure"
key: "current-step-hint-object"

title: "Current Step Hints"
description: |
  Contained within the Report Card object, the Current Step Hint object provides the function to call and properties to pass to [Stitch.js]({{ page.anchors.stitch-js.section }}).

  Otherwise, this object will provide information about the next call to make to the API.

object-attributes:
  - name: "api"
    type: "api hint object"
    url: ""
    description: "Describes the actions required to complete the current connection step using the API, if applicable."

  - name: "js"
    type: "stitch js hint object"
    url: ""
    description: "Describes the actions required to complete the current connection step using [Stitch.js]({{ page.anchors.stitch-js.section }}) if applicable."

sub-structures:
  - key: "current-step-api-hint-object"
  - key: "current-step-stitch-js-hint-object"

examples:
  - code: |
      {
         "current_step_hints":{
            "api":{
               "method":"POST",
               "url":"/v4/sources"
            },
            "js":{
               "function":"authorizeSource",
               "options":{
                  "id":<SOURCE_ID>
               }
            }
         }
      }

---