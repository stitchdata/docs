---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "import-api"
content-type: "api-object"
endpoint: "status"
version: "2"
order: 1


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "API Status"
summary: &summary "{{ site.data.import-api.core-objects.api-status.object-description | flatify }}"

description: *summary
endpoint-url: "/import/status"


# -------------------------- #
#        VERSION INFO        #
# -------------------------- #

latest-version: "2"
versions:
  - number: "2"
    deprecated: false

# -------------------------- #
#      AVAILABLE METHODS     #
# -------------------------- #

available-methods:
  - id: "get-status"
    title: "Get Import API status"
    method: "get"
    short: "{{ site.data.import-api.core-objects.api-status.description | flatify }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

## The copy for these attributes lives in:
## _data/import-api/general.yml

object-attributes:
  - name: "name"
    type: "string"
    description: "This will always be `pipeline.gate`."
    value: "pipeline.gate"

  - name: "version"
    type: "string"
    description: "**Stitch internal field**."
    value: "0.3.3-SNAPSHOT"

  - name: "revision"
    type: "string"
    description: "**Stitch internal field**."
    value: "<REVISION>"

  - name: "status"
    type: "string"
    description: "The status of the Import API at the time of the request."
    value: "OK"

  - name: "reason"
    type: "string"
    description: "If applicable, the reason for the status."
    value: ""


# -------------------------- #
#           EXAMPLES         #
# -------------------------- #

examples:
  - code: |
      {{ site.data.import-api.code-examples.responses.get-status }}
---