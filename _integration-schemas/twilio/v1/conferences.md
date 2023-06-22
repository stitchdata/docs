---
tap: "twilio"
version: "1"
key: ""

name: "conferences"
doc-link: "https://www.twilio.com/docs/voice/api/conference-resource#read-multiple-conference-resources"
singer-schema: https://github.com/singer-io/tap-twilio/tree/master/tap_twilio/schemas/conferences.json
description: |
  The **{{ table.name }}** table returns all the conferences within your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "Read multiple Conference resources"
    doc-link: "https://www.twilio.com/docs/voice/api/conference-resource?code-sample=code-read-multiple-conference-resources&code-language=curl&code-sdk-version=json"

attributes:
  - name: "sid"
    type: "string"
    primary-key: true
    description: "The unique string that that we created to identify this Conference resource."

  - name: "date_updated"
    type: "date-time"
    replication-key: true
    description: "The date and time in GMT that this resource was last updated, specified in RFC 2822 format."

  - name: "account_sid"
    type: "string"
    description: "The SID of the Account that created this Conference resource."

  - name: "api_version"
    type: "string"
    description: "The API version used to create this conference."

  - name: "call_sid_ending_conference"
    type: "string"
    description: "The call SID that caused the conference to end." 

  - name: "date_created"
    type: "date-time"
    description: "The date and time in GMT that this resource was created specified in RFC 2822 format."

  - name: "friendly_name"
    type: "string"
    description: "A string that you assigned to describe this conference room. Maxiumum length is 128 characters."

  - name: "reason_conference_ended"
    type: "string"
    description: "The reason why a conference ended. When a conference is in progress, will be null. When conference is completed, can be: conference-ended-via-api, participant-with-end-conference-on-exit-left, participant-with-end-conference-on-exit-kicked, last-participant-kicked, or last-participant-left."

  - name: "region"
    type: "string"
    description: "A string that represents the Twilio Region where the conference audio was mixed. May be us1, ie1, de1, sg1, br1, au1, and jp1. Basic conference audio will always be mixed in us1. Global Conference audio will be mixed nearest to the majority of participants."

  - name: "status"
    type: "string"
    description: "The status of this conference. Can be: init, in-progress, or completed."

  - name: "subresource_uris"
    type: "array"
    description: "A list of related resources identified by their URIs relative to https://api.twilio.com."
    subattributes:
    - name: "subresource"
      type: "string"
      description: "Subresource type"

    - name: "uri"
      type: "string"
      description: "URI for the subresource, relative to https://api.twilio.com"

  - name: "uri"
    type: "string"
    description: "The URI of this resource, relative to https://api.twilio.com."
---