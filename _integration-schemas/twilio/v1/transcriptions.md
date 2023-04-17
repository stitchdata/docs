---
tap: "twilio"
version: "1"
key: ""

name: "transcriptions"
doc-link: "https://www.twilio.com/docs/voice/api/recording-transcription#read-multiple-transcription-resources"
singer-schema: https://github.com/singer-io/tap-twilio/tree/master/tap_twilio/schemas/transcriptions.json
description: |
  The **{{ table.name }}** table returns the full set of transcriptions generated from all recordings in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "Read multiple Transcription resources"
    doc-link: "https://www.twilio.com/docs/voice/api/recording-transcription?code-sample=code-read-list-all-transcriptions&code-language=curl&code-sdk-version=json"

attributes:
  - name: "sid"
    type: "string"
    primary-key: true
    description: "The unique string that that we created to identify the Transcription resource."

  - name: "date_updated"
    type: "date-time"
    replication-key: true
    description: "The date and time in GMT that the resource was last updated specified in RFC 2822 format."

  - name: "account_sid"
    type: "string"
    description: "The SID of the Account that created the Transcription resource."

  - name: "api_version"
    type: "string"
    description: "The API version used to create the transcription."

  - name: "date_created"
    type: "date-time"
    description: "The date and time in GMT that the resource was created specified in RFC 2822 format."

  - name: "duration"
    type: "integer"
    description: "The duration of the transcribed audio in seconds."

  - name: "price"
    type: "number"
    description: "The charge for the transcript in the currency associated with the account. This value is populated after the transcript is complete so it may not be available immediately."

  - name: "price_unit"
    type: "string"
    description: "The currency in which price is measured, in ISO 4127 format (e.g. usd, eur, jpy)."

  - name: "recording_sid"
    type: "string"
    description: "The SID of the Recording from which the transcription was created."

  - name: "status"
    type: "string"
    description: "The status of the transcription. Can be: in-progress, completed, failed"

  - name: "transcription_text"
    type: "string"
    description: "The text content of the transcription."

  - name: "type"
    type: "string"
    description: "The transcription type. Can only be: fast."

  - name: "uri"
    type: "string"
    description: "The URI of the resource, relative to https://api.twilio.com."
---   
