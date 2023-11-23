---
tap: "twilio"
version: "1"
key: ""

name: "outgoing_caller_ids"
doc-link: "https://www.twilio.com/docs/voice/api/outgoing-caller-ids?code-sample=code-list-an-accounts-outgoing-caller-ids&code-language=curl&code-sdk-version=json"
singer-schema: https://github.com/singer-io/tap-twilio/tree/master/tap_twilio/schemas/outgoing_caller_ids.json
description: |
  The **{{ table.name }}** table returns a list of `OutgoingCallerId` resource representations, each representing a Caller ID number valid for a {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List an Account's Outgoing Caller IDs"
    doc-link: "https://www.twilio.com/docs/voice/api/outgoing-caller-ids?code-sample=code-list-an-accounts-outgoing-caller-ids&code-language=curl&code-sdk-version=json"

attributes:
  - name: "sid"
    type: "string"
    primary-key: true
    description: "A 34 character string that uniquely identifies this resource."

  - name: "date_updated"
    type: "date-time"
    replication-key: true
    description: "The date that this resource was last updated, given in RFC 2822 format."

  - name: "account_sid"
    type: "string"
    description: "The unique ID of the Account responsible for this Caller Id."

  - name: "date_created"
    type: "date-time"
    description: "The date that this resource was created, given in RFC 2822 format."

  - name: "friendly_name"
    type: "string"
    description: "A human readable descriptive text for this resource, up to 64 characters long. By default, the FriendlyName is a nicely formatted version of the phone number."

  - name: "phone_number"
    type: "string"
    description: "The incoming phone number. Formatted with a '+' and country code e.g., +16175551212 (E.164 format)."

  - name: "uri"
    type: "string"
    description: "The URI for this resource, relative to https://api.twilio.com."
---