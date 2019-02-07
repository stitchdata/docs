---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "import-api"
content-type: "api-structure"
key: "error-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Error"
description: "{{ site.data.import-api.api.data-structures.error.description | flatify }}"
has-multiple-versions: "false"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "status"
    type: "string"
    description: |
      This will always be `ERROR`.
    value: |
      ERROR

  - name: "message"
    type: "string"
    description: |
      A message describing the error.
    value: |
      Request cannot be processed; see errors.

  - name: "error"
    type: "string"
    description: |
      The reason for the error.
    value: |
      Request rejected: request size (<BYTE>s bytes) exceeds the maximum

  - name: "errors"
    type: "array"
    sub-type: "error reason"
    url: "{{ site.data.import-api.api.data-structures.error-reason.section }}"
    description: |
      An array of [error reason objects]({{ site.data.import-api.api.data-structures.error-reason.section }}) that describe the properties causing the error.

sub-structures:
  - key: "error-reason-object"

# -------------------------- #
#          EXAMPLES          #
# -------------------------- #

examples:
  - type: "With error reason object"
    code: |
      {
        "status": "ERROR",
        "error": "Request cannot be processed; see errors.",
        "errors": [
          {
            "reason": {
              "data": [
                "data must include keys"
              ]
            }
          }
        ]
      }

  - type: "Without error reason object"
    code: |
      {
        "status": "ERROR",
        "message": "An array of records is expected"
      }
---