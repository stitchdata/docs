---
tap: "bronto"
# version: ""

name: "list"
doc-link: http://dev.bronto.com/api/soap/objects/general/maillistobject/
singer-schema: https://github.com/singer-io/tap-bronto/blob/master/tap_bronto/endpoints/list.py#L16
description: |
  The `lists` table contains info about the contact lists in your Bronto account. 

replication-method: "Full Table"

api-method:
  name: "readLists"
  doc-link: http://dev.bronto.com/api/soap/objects/general/maillistobject/

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
    description: |
      The status of the list. Possible values are:

      - `active`
      - `deleted`
      - `tmp`

  - name: "activeCount"
    type: "integer"
    description: "The number of active contacts of currently on the list."

  - name: "name"
    type: "string"
    description: "The internal name of the list."
---
