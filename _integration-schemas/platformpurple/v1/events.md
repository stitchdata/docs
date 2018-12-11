---
tap: "platformpurple"
version: "1.0"

name: "events"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-platformpurple/blob/master/tap_platformpurple/schemas/events.json"
description: ""

replication-method: "Key-based Incremental"

attributes:
  - name: "docID"
    type: "string"
    primary-key: true
    description: "The event ID."
    # foreign-key-id: "event-id"

  - name: "dateTime"
    type: "date-time"
    replication-key: true
    description: "The time the event occured."

  - name: "anonymousUserID"
    type: "string"
    description: ""

  - name: "appVersionNumber"
    type: "string"
    description: "The version number of the app."

  - name: "browser"
    type: "string"
    description: "The browser used to create the event."

  - name: "browserVersion"
    type: "string"
    description: "The version of the browser used to created the event."

  - name: "chapterTitle"
    type: "string"
    description: ""

  - name: "clientTimestamp"
    type: "integer"
    description: ""

  - name: "cpu"
    type: "object"
    description: ""
    object-attributes:
      - name: "architecture"
        type: "string"
        description: ""

  - name: "elapsed"
    type: "integer"
    description: ""

  - name: "environment"
    type: "string"
    description: ""

  - name: "eventType"
    type: "string"
    description: "The event type."

  - name: "firstVisitToEnvironment"
    type: "boolean"
    description: ""

  - name: "lastUpdated"
    type: "integer"
    description: ""

  - name: "mediaEndSeconds"
    type: "integer"
    description: ""

  - name: "mediaStartSeconds"
    type: "integer"
    description: ""

  - name: "mediaType"
    type: "string"
    description: ""

  - name: "origin"
    type: "string"
    description: ""

  - name: "os"
    type: "string"
    description: ""

  - name: "osVersion"
    type: "string"
    description: ""

  - name: "productID"
    type: "integer"
    description: "The product ID."
    foreign-key-id: "product-id"

  - name: "productName"
    type: "string"
    description: "The product name."

  - name: "productSKU"
    type: "string"
    description: "The product SKU."

  - name: "publisherID"
    type: "integer"
    description: ""

  - name: "receivedTimestamp"
    type: "integer"
    description: ""

  - name: "referer"
    type: "string"
    description: ""

  - name: "referrer"
    type: "string"
    description: ""

  - name: "sessionGroup"
    type: "string"
    description: ""

  - name: "timestamp"
    type: "integer"
    description: ""

  - name: "userEmail"
    type: "string"
    description: ""

  - name: "userID"
    type: "integer"
    description: "THe user ID."
    foreign-key-id: "user-id"
---