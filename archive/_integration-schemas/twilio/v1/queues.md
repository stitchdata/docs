---
tap: "twilio"
version: "1"
key: ""

name: "queues"
doc-link: "https://www.twilio.com/docs/voice/api/queue-resource#read-multiple-queue-resources"
singer-schema: https://github.com/singer-io/tap-twilio/tree/master/tap_twilio/schemas/queues.json
description: |
  The **{{ table.name }}** table returns the list of call queues within your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "Read multiple Queue resources"
    doc-link: "https://www.twilio.com/docs/voice/api/queue-resource?code-sample=code-read-multiple-queue-resources&code-language=curl&code-sdk-version=json"

attributes:
  - name: "sid"
    type: "string"
    primary-key: true
    description: "The unique string that that we created to identify this Queue resource."

  - name: "date_updated"
    type: "date-time"
    replication-key: true
    description: "The date and time in GMT that this resource was last updated, specified in RFC 2822 format."

  - name: "account_sid"
    type: "string"
    description: "The SID of the Account that created this Queue resource."

  - name: "average_wait_time"
    type: "integer"
    description: "The average wait time in seconds of the members in this queue. This is calculated at the time of the request."

  - name: "current_size"
    type: "integer"
    description: "The number of calls currently in the queue."

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "friendly_name"
    type: "string"
    description: "A string that you assigned to describe this resource."

  - name: "max_size"
    type: "integer"
    description: "The maximum number of calls that can be in the queue. The default is 1000 and the maximum is 5000."

  - name: "subresource_uris"
    type: "array"
    description: "A list of related resources identified by their URIs relative to https://api.twilio.com."
    subattributes:
    - name: "subresource"
      type: "string"
      description: ""

    - name: "uri"
      type: "string"
      description: ""

  - name: "uri"
    type: "string"
    description: "The URI of this resource, relative to https://api.twilio.com."
---