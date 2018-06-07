---
tap: "bronto"
# version: ""

name: "list"
doc-link: http://dev.bronto.com/api/soap/objects/general/maillistobject/
singer-schema: https://github.com/singer-io/tap-bronto/blob/master/tap_bronto/endpoints/list.py#L16
description: |
  A list is a logical collection of contacts in your Bronto account.

replication-method: "Full Table"

api-method:
  name: "readLists"
# How do we handle SOAP API endpoints?
#  doc-link: https://developer.github.com/v3/issues/assignees/#list-assignees

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The unique id assigned to the list."

  - name: "label"
    type: "string"
    description: "The external (customer facing) name of the list. "

  - name: "status"
    type: "string"
    description: "The status of the list. Valid values are active, deleted, and tmp"

  - name: "activeCount"
    type: "integer"
    description: "The number of active contacts of currently on the list."

  - name: "id"
    type: "string"
    description: "The unique id assigned to the list."

  - name: "name"
    type: "string"
    description: "The internal name of the list."
---
