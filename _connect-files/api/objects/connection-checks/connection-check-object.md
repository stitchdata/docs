---
content-type: "api-structure"
key: "connection-check-object"

title: "Connection Checks"
description: "A connection check object shows the results from a test of a connection's parameters. The nature of the test varies by connection type."

object-attributes:
  - name: "error"
    type: "boolean"
    description: "Indicates if the last connection check resulted in an error."

  - name: "started_at"
    type: "timestamp"
    description: "The time the last check started."

  - name: "completed_at"
    type: "timestamp"
    description: "The time the last check completed."

examples:
  - code: |
      {
          "last_check":{
            "error": false,
            "started_at":"2018-02-06T16:15:19Z",
            "completed_at":"2018-02-06T16:16:21Z"
          }
      }
---