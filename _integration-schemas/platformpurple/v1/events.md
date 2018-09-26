---
tap: "platformpurple"
# version: "1.0"

name: "events"
doc-link: 
singer-schema: https://github.com/singer-io/tap-platformpurple/blob/master/tap_platformpurple/schemas/events.json
description: |
  ## description of the table

replication-method: "Key-based Incremental / Full Table"

replication-key:
  name: ""

api-method:
  name: ""
  doc-link: ""

attributes:
  - name: "docID"
    type: "string"
    description: ""

  - name: "dateTime"
    type: "date-time"
    description: ""  

  - name: "referer"
    type: "string"
    description: ""

  - name: "productID"
    type: "integer"
    description: ""

  - name: "sessionGroup"
    type: "string"
    description: ""

  - name: "userID"
    type: "integer"
    description: ""

  - name: "clientTimestamp"
    type: "date-time"
    description: ""

  - name: "productName"
    type: "string"
    description: ""

  - name: "elapsed"
    type: "integer"
    description: ""

  - name: "lastUpdated"
    type: "integer"
    description: ""

  - name: "productSKU"
    type: "string"
    description: ""

  - name: "osVersion"
    type: "string"
    description: ""

  - name: "browser"
    type: "string"
    description: ""

  - name: "browserVersion"
    type: "string"
    description: ""

  - name: "userEmail"
    type: "string"
    description: ""

  - name: "chapterTitle"
    type: "string"
    description: ""

  - name: "timestamp"
    type: "integer"
    description: ""

  - name: "os"
    type: "string"
    description: ""

  - name: "receivedTimestamp"
    type: "integer"
    description: ""

  - name: "mediaStartSeconds"
    type: "integer"
    description: ""

  - name: "cpu"
    type: "object"
    description: ""
      - name: "architecture"
        type: "string"
        description: ""

  - name: "mediaType"
    type: "string"
    description: ""

  - name: "eventType"
    type: "string"
    description: ""

  - name: "referrer"
    type: "string"
    description: ""

  - name: "environment"
    type: "string"
    description: ""

  - name: "publisherID"
    type: "integer"
    description: ""

  - name: "anonymousUserID"
    type: "string"
    description: ""

  - name: "appVersionNumber"
    type: "string"
    description: ""

  - name: "firstVisitToEnvironment"
    type: "boolean"
    description: ""
---