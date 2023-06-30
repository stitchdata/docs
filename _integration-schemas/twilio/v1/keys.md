---
tap: "twilio"
version: "1"
key: ""

name: "keys"
doc-link: "https://www.twilio.com/docs/usage/api/keys?code-sample=code-read-a-key-resource&code-language=curl&code-sdk-version=json"
singer-schema: https://github.com/singer-io/tap-twilio/tree/master/tap_twilio/schemas/keys.json
description: |
  The **{{ table.name }}** table returns a list of API Keys in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "Read a Key resource"
    doc-link: "https://www.twilio.com/docs/usage/api/keys?code-sample=code-read-a-key-resource&code-language=curl&code-sdk-version=json"

attributes:
  - name: "sid"
    type: "string"
    primary-key: true
    description: "The Twilio-provided string that uniquely identifies the Key resource to update."

  - name: "date_updated"
    type: "date-time"
    replication-key: true
    description: "The date and time in GMT that the resource was last updated specified in RFC 2822 format."

  - name: "account_sid"
    type: "string"
    description: "The SID of the Account that created the Key resources to update."

  - name: "date_created"
    type: "date-time"
    description: "The date and time in GMT that the resource was created specified in RFC 2822 format."

  - name: "friendly_name"
    type: "string"
    description: "A descriptive string that you create to describe the resource. It can be up to 64 characters long."
---