---
content-type: "api-structure"
key: "current-step-hint-object"

title: "Current Step Hint"
description: "{{ api.data-structures.current-step-hints.description | flatify }}"

object-attributes:
  - name: "api"
    type: "object"
    sub-type: "API Hint"
    url: "{{ api.data-structures.current-step-hints.api-hints.section }}"
    description: "{{ api.data-structures.current-step-hints.api-hints.description | flatify }}"

  - name: "js"
    type: "object"
    sub-type: "JavaScript Hint"
    url: "{{ api.data-structures.current-step-hints.stitch-connect-js-hints.section }}"
    description: "{{ api.data-structures.current-step-hints.stitch-connect-js-hints.description | flatify }}"

sub-structures:
  - key: "current-step-api-hint-object"
  - key: "current-step-stitch-js-hint-object"

examples:
  - code: |
      {
         "current_step_hints":{
            "api":{
               "method":"POST",
               "url":"{{ api.core-objects.sources.create.name | flatify }}"
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