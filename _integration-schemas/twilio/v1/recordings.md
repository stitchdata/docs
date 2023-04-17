---
tap: "twilio"
version: "1"
key: ""

name: "recordings"
doc-link: "https://www.twilio.com/docs/voice/api/recording#read-multiple-recording-resources"
singer-schema: https://github.com/singer-io/tap-twilio/tree/master/tap_twilio/schemas/recordings.json
description: |
  The **{{ table.name }}** table returns a list of recordings, each representing a recording generated during a call or conference in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "Read multiple Recording Resources"
    doc-link: "https://www.twilio.com/docs/voice/api/recording?code-sample=code-get-all-recordings-for-an-account&code-language=curl&code-sdk-version=json"

attributes:
  - name: "sid"
    type: "string"
    primary-key: true
    description: "The unique string that that we created to identify the Recording resource."

  - name: "date_created"
    type: "date-time"
    replication-key: true
    description: "The date and time in GMT that the resource was created specified in RFC 2822 format."

  - name: "account_sid"
    type: "string"
    description: "The SID of the Account that created the Recording resource."

  - name: "api_version"
    type: "string"
    description: "The API version used during the recording."

  - name: "call_sid"
    type: "string"
    description: "The SID of the Call the Recording resource is associated with. This will always refer to the parent leg of a two-leg call."

  - name: "channels"
    type: "integer"
    description: "The number of channels in the final recording file. Can be: 1 or 2. You can split a call with two legs into two separate recording channels if you record using TwiML Dial or the Outbound Rest API."

  - name: "conference_sid"
    type: "string"
    description: "The Conference SID that identifies the conference associated with the recording, if a conference recording."

  - name: "date_updated"
    type: "date-time"
    description: "The date and time in GMT that the resource was last updated specified in RFC 2822 format."

  - name: "duration"
    type: "integer"
    description: "The length of the recording in seconds."

  - name: "encryption_details"
    type: "object"
    description: "How to decrypt the recording if it was encrypted using Call Recording Encryption feature."
    subattributes:
    - name: "type"
      type: "string"
      description: ""

    - name: "encryption_public_key_sid"
      type: "string"
      description: ""

    - name: "encryption_cek"
      type: "string"
      description: ""

    - name: "iv"
      type: "string"
      description: ""

  - name: "error_code"
    type: "string"
    description: "The error code that describes why the recording is absent. The error code is described in our Error Dictionary. This value is null if the recording status is not absent."

  - name: "price"
    type: "number"
    description: "The one-time cost of creating the recording in the price_unit currency."

  - name: "price_unit"
    type: "string"
    description: "The currency used in the price property. Example: USD."

  - name: "source"
    type: "string"
    description: "How the recording was created. Can be: DialVerb, Conference, OutboundAPI, Trunking, RecordVerb, StartCallRecordingAPI, and StartConferenceRecordingAPI."

  - name: "start_time"
    type: "date-time"
    description: "The start time of the recording in GMT and in RFC 2822 format."

  - name: "status"
    type: "string"
    description: "he status of the recording. Can be: processing, completed, absent or deleted."

  - name: "subresource_uris"
    type: "array"
    description: "A list of related resources identified by their relative URIs."
    subattributes:
    - name: "subresource"
      type: "string"
      description: ""

    - name: "uri"
      type: "string"
      description: ""

  - name: "uri"
    type: "string"
    description: "The URI of the resource, relative to https://api.twilio.com."
---