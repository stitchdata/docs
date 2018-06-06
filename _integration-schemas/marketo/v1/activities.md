---
tap: "marketo"
version: "1.0"

name: "activities"
doc-link: "http://developers.marketo.com/rest-api/endpoint-reference/lead-database-endpoint-reference/#!/Activities/getLeadActivitiesUsingGET"
singer-schema: https://github.com/singer-io/tap-marketo/blob/14ea7da75ea0edd855500678c14764f5dad5b283/tap_marketo/schemas/activities.json
description: |
  The `activities` table contains info about lead activities.

notes: 

replication-method: "Incremental"
api-method:
  name: "getLeadActivities"
  doc-link: "http://developers.marketo.com/rest-api/endpoint-reference/lead-database-endpoint-reference/#!/Activities/getLeadActivitiesUsingGET"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the activity."

  - name: "activityDate"
    type: "date-time"
    replication-key: true
    description: "The date of the activity."

  - name: "leadId"
    type: "integer"
    description: "The ID of the lead associated with the activity."

  - name: "activityTypeId"
    type: "integer"
    description: "The ID of the activity type."

  - name: "primaryAttributeValue"
    type: "string"
    description: "Value of the activity's primary attribute."

  - name: "primaryAttributeValueId"
    type: "integer"
    description: "The ID of the activity's primary attribute."

  - name: "attributes"
    type: "array"
    description: "Secondary attributes of the activity."
    array-attributes:
      - name: "name"
        type: "string"
        description: "The name of the secondary attribute."

      - name: "value"
        type: "string"
        description: "The value of the secondary attribute."
---