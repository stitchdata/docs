---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

type: "connect"
content-type: "api-object"
endpoint: "destination-types"
order: 5


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Destination Type"
description: "{{ api.core-objects.destination-types.description }}"
endpoint-url: "/destination-types"


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
  - id: "get-a-destination-type"
    title: "Get a destination type"
    method: "get"
    short: "{{ api.core-objects.destination-types.get.short | flatify }}"

  - id: "list-destination-types"
    title: "List all destination types"
    method: "get"
    short: "{{ api.core-objects.destination-types.list.short | flatify }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "report_card"
    type: "object"
    sub-type: "destination report card"
    url: "{{ api.data-structures.report-cards.destination.section }}"
    description: "The destination Report Card object corresponding to the destination's `type`. For example: `s3` or `snowflake`."
---