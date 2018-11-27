---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-structure"
key: "connection-check-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Connection Check"
description: "{{ api.data-structures.connection-checks.description | flatify }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "error"
    type: "boolean"
    description: "Indicates if the last connection check resulted in an error."
    value: |
      false

  - name: "started_at"
    type: "timestamp"
    description: "The time the last check started."
    value: |
      "2018-02-06T16:15:19Z"

  - name: "completed_at"
    type: "timestamp"
    description: "The time the last check completed."
    value: |
      "2018-02-06T16:16:21Z"

examples:
---