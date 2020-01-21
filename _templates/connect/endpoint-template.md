---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: ""
key: ""
version: ""


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: ""
method: ""
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.[endpoint].[method].short }}"
description: "{{ api.core-objects.[endpoint].[method].description | flatify }}"


# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

## This depends on the method being used, and the type of endpoint.

# arguments:
#   - name: ""
#     required: true/false
#     type: ""
#     description: ""
#     example-value: |


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of `200 OK` and [PLACEHOLDER]


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "request"
    language: "json"
    subexamples: ## Used if there's more than 1 example for an endpoint - see Create a Destination for an example
      - title: ""
        code: 

  - type: "response"
    language: "json"
    code: 

  - type: "errors"
    # Included only if there are errors for the endpoint
    # The errors live in: _data/connect/response-codes.yml
---