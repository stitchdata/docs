---
content-type: "embed-structure"
key: "connection-check-object"

title: "Connection Checks"
description: "A connection check object shows the results from a test of a connection's parameters. The nature of the test varies by connection type."

object-attributes:
  - name: "message"
    type: "string"
    description: "A message describing an error, if one occurred during the check."

  - name: "status"
    type: "string"
    description: "A status description. Possible values are `PENDING`, `OK`, `FAILED`."

  - name: "updated_at"
    type: "timestamp"
    description: "The time the check was last updated."
---