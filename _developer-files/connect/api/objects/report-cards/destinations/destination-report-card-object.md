---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

type: "connect"
content-type: "api-structure"
key: "report-card-object--destination"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Destination Report Card"
description: "{{ api.data-structures.report-cards.destination.description }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "current_step"
    type: "integer"
    description: "The index (in the `steps` array) of the current step needed to configure the destination."

  - name: "details"
    type: "object"
    sub-type: "details"
    url: "{{ api.data-structures.details.section }}"
    description: |
      {{ api.data-structures.details.short | flatify }}

  - name: "steps"
    type: "array"
    description: "A sequential list of [Connection Step objects]({{ api.data-structures.connection-steps.section }}) required to complete configuration for the connection type."

  - name: "type"
    type: "string"
    description: "The destination connection type. Ex: `postgres` or `redshift`"


# -------------------------- #
#          EXAMPLES          #
# -------------------------- #

examples:
  - code: |
      {{ site.data.connect.code-examples.destination-report-cards.snowflake | remove: "+*" }}
---