---
tap: "twilio"
version: "1"
key: ""

name: "conference_participants"
doc-link: "https://www.twilio.com/docs/voice/api/conference-participant-resource#read-multiple-participant-resources"
singer-schema: https://github.com/singer-io/tap-twilio/tree/master/tap_twilio/schemas/conference_participants.json
description: |
  The **{{ table.name }}** table returns the list of active participants in the {{ integration.display_name }} conference identified by `ConferenceSid`.

replication-method: "Full Table"

api-method:
    name: "Read multiple Participant resources"
    doc-link: "https://www.twilio.com/docs/voice/api/conference-participant-resource?code-sample=code-read-multiple-participant-resources&code-language=curl&code-sdk-version=json"

attributes:
  - name: "uri"
    type: "string"
    primary-key: true
    description: "The URI of the resource, relative to https://api.twilio.com."

  - name: "account_sid"
    type: "string"
    description: "The SID of the Account that created the Participant resource."

  - name: "call_sid"
    type: "string"
    description: "The SID of the Call the Participant resource is associated with."

  - name: "call_sid_to_coach"
    type: "string"
    description: "The SID of the participant who is being coached. The participant being coached is the only participant who can hear the participant who is coaching."

  - name: "coaching"
    type: "boolean"
    description: "Whether the participant is coaching another call. Can be: true or false. If not present, defaults to false unless call_sid_to_coach is defined. If true, call_sid_to_coach must be defined."

  - name: "conference_sid"
    type: "string"
    description: "The SID of the conference the participant is in."

  - name: "date_created"
    type: "date-time"
    description: "The date and time in GMT that the resource was created specified in RFC 2822 format."

  - name: "date_updated"
    type: "date-time"
    description: "The date and time in GMT that the resource was last updated specified in RFC 2822 format."

  - name: "end_conference_on_exit"
    type: "boolean"
    description: "Whether the conference ends when the participant leaves. Can be: true or false and the default is false. If true, the conference ends and all other participants drop out when the participant leaves."

  - name: "hold"
    type: "boolean"
    description: "Whether the participant is on hold. Can be true or false."

  - name: "label"
    type: "string"
    description: "The user-specified label of this participant, if one was given when the participant was created. This may be used to fetch, update or delete the participant."

  - name: "muted"
    type: "boolean"
    description: "Whether the participant is muted. Can be true or false."

  - name: "start_conference_on_enter"
    type: "boolean"
    description: "Whether the conference starts when the participant joins the conference, if it has not already started. Can be: true or false and the default is true. If false and the conference has not started, the participant is muted and hears background music until another participant starts the conference."

  - name: "status"
    type: "string"
    description: "The status of the participant's call in a session. Can be: queued, connecting, ringing, connected, complete, or failed."
---