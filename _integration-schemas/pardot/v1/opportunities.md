---
tap: "pardot"
version: "1"
key: "opportunity"

name: "opportunities"
doc-link: "http://developer.pardot.com/kb/object-field-references/#opportunity"
singer-schema: "https://github.com/singer-io/tap-pardot/blob/master/tap_pardot/schemas/opportunities.json"
description: |
  The `{{ table.name }}` table contains info about the opportunities in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Query opportunities"
  doc-link: "http://developer.pardot.com/kb/api-version-3/opportunities/"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    replication-key: true
    description: "The ID of the opportunity."
    foreign-key-id: "opportunity-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the opportunity was last updated."

  - name: "campaign_id"
    type: "integer"
    description: "The ID of the campaign associated with the opportunity."
    foreign-key-id: "campaign-id"

  - name: "closed_at"
    type: "date-time"
    description: "The time the opportunity was closed."

  - name: "created_at"
    type: "date-time"
    description: "The time the opportunity was created."

  - name: "name"
    type: "string"
    description: "The name of the opportunity."

  - name: "probability"
    type: "integer"
    description: "The probability of the opportunity. This will be a value between `0` and `100`."

  - name: "stage"
    type: "string"
    description: "The stage of the opportunity."

  - name: "status"
    type: "string"
    description: |
      The status of the opportunity. Possible values are:

      - `won`
      - `lost`
      - `open`

  - name: "type"
    type: "string"
    description: "The type of the opportunity."

  - name: "value"
    type: "number"
    description: "The value of the opportunity."
---