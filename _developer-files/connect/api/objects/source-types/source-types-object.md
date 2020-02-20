---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-object"
endpoint: "source-types"
order: 5


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Source Type"
endpoint-url: "/source-types"

description: "{{ api.core-objects.source-types.description }}"
intro-short: "Retrieve configuration info for data sources" # Used in the API functionality section of the docs

# -------------------------- #
#        VERSION INFO        #
# -------------------------- #

latest-version: "4"
versions:
  - number: "4"
    deprecated: false


# -------------------------- #
#      AVAILABLE METHODS     #
# -------------------------- #

available-methods:
  - id: "get-a-source-type"
    title: "Get a source type"
    method: "get"
    short: "{{ api.core-objects.source-types.get.short | flatify }}"

  - id: "list-source-types"
    title: "List all source types"
    method: "get"
    short: "{{ api.core-objects.source-types.list.short | flatify }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "report_card"
    type: "object"
    sub-type: "source report card"
    url: "{{ api.data-structures.report-cards.source.section }}"
    description: "The Source Report Card object corresponding to the source's `type`. For example: `platform.marketo` or `platform.hubspot`."
---