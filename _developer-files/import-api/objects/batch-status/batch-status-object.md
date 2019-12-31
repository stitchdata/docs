---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "import-api"
content-type: "api-structure"
key: "batch-status-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Batch Status"
description: "{{ site.data.import-api.data-structures.batch-status.description | flatify }}"
has-multiple-versions: "false"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "status"
    type: "string"
    description: |
      The batch status. Possible values are:

      - `OK` - Corresponds to a `201 Created` response code if using the [Push]({{ site.data.import-api.core-objects.push.anchor }}) endpoint, or a `200 OK` response code if using the [Validate]({{ site.data.import-api.core-objects.validate.anchor }}) endpoint
      - `Accepted` - Corresponds to a `202 Accepted` response code
    value: |
      OK

  - name: "message"
    type: "string"
    description: |
      A message describing the current status of the batch.
    value: |
      Batch Accepted!


# -------------------------- #
#          EXAMPLES          #
# -------------------------- #

examples:
  - type: "Validate - 200 response"
    code: |
      {
        "status": "OK",
        "message": "Batch is valid!"
      }

  - type: "Push - 201 response"
    code: |
      {
        "status": "OK",
        "message": "Batch Accepted!"
      }

  - type: "Push - 202 response"
    code: |
      {
        "status": "Accepted",
        "message": "The batch is queued to be processed."
      }
---