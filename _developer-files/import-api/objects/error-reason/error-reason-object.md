---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "import-api"
content-type: "api-structure"
key: "error-reason-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Error Reason"
description: "{{ site.data.import-api.api.data-structures.error-reason.description | flatify }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "reason"
    type: "string, object"
    description: |
      A string or an object describing the reason for the error. 

      When an object, the structure of this object is `"[field_name]": ["error_reason"]`, where `field_name` is the name of the argument that caused the error, and `error_reason` is an array of strings describing the reason for the error. 

      For example: `"data": ["data must include keys"]`


# -------------------------- #
#          EXAMPLES          #
# -------------------------- #

examples:
  - type: "With reason as a string"
    code: |
      {
        "status": "ERROR",
        "error": "Request cannot be processed; see errors.",
        "errors": [
          {
            "reason": "The batch contains data points for multiple clients. Only client_id <CLIENT_ID> is allowed"
          }
        ]
      }

  - type: "With reason as an object"
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
---