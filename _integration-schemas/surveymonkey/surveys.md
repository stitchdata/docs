---
tap: "surveymonkey"
version: "1"
key: "surveys"

name: "surveys"
doc-link: "https://developer.surveymonkey.com/api/v3/"
singer-schema: https://github.com/singer-io/tap-surveymonkey/tree/TDL-23990-changes/tap_surveymonkey/schemas/surveys.json
description: "This table contains information about your surveys."

replication-method: "Key-based Incremental"

attributes:
  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "date_modified"
    type: "date-time"
    description: ""
	replication-key: true

  - name: "id"
    type: "string"
    description: ""
	primary-key: true

  - name: "language"
    type: "string"
    description: ""

  - name: "nickname"
    type: "string"
    description: ""

  - name: "question_count"
    type: "integer"
    description: ""

  - name: "response_count"
    type: "integer"
    description: ""

  - name: "title"
    type: "string"
    description: ""
---