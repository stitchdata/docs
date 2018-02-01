---
content-type: "embed-object"
endpoint: "destinations"

title: "Destination"
description: "Destinations are the data warehouses into which Stitch writes data."
endpoint-url: "/destinations"
version: "3"

object-attributes:
  - name: "id"
    type: "integer"
    description: "A unique identifier for this destination."

  - name: "connection"
    type: "destination-properties" # this = destination form properties?
    description: "Parameters for connecting to the destination, excluding any sensitive credentials."

  - name: "created_at"
    type: "timestamp"
    description: "The time at which the destination object was created."

  - name: "last_check"
    type: "connection-check"
    description: "The status and results of the most recent check run for this destination connection."

  - name: "type"
    type: "string"
    description: "The destination type. Possible values are `redshift` and `postgres`."

  - name: "updated_at"
    type: "timestamp"
    description: "The time at which the destination object was last updated."
---