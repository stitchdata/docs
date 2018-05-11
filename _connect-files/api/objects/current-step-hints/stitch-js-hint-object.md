---
content-type: "api-sub-structure"
key: "current-step-stitch-js-hint-object"

title: "JavaScript Hint"

object-attributes:
  - name: "function"
    type: "string"
    description: "The [JavaScript client]({{ js.section | flatify | prepend: site.baseurl }}) function required to complete the current step."

  - name: "options"
    type: "object"
    description: "The option values to pass into the corresponding JavaScript client `function`."
---