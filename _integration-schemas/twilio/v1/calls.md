---
tap: "twilio"
version: "1"
key: ""

name: "calls"
doc-link: "https://www.twilio.com/docs/voice/api/call-resource#read-multiple-call-resources"
singer-schema: https://github.com/singer-io/tap-twilio/tree/master/tap_twilio/schemas/calls.json
description: |
  The **{{ table.name }}** table returns a list of phone calls made to and from an account in your {{ integration.display_name }} account, identified by its `AccountSid`.

replication-method: "Key-based Incremental"  

api-method:
    name: "Read multiple Call resources"
    doc-link: "https://www.twilio.com/docs/voice/api/call-resource?code-sample=code-read-multiple-call-resources&code-language=curl&code-sdk-version=json"

attributes:
  - name: "sid"
    type: "string"
    primary-key: true
    description: "The unique string that we created to identify this Call resource."

  - name: "date_updated"
    type: "date-time"
    replication-key: true
    description: "The date and time in GMT that this resource was last updated, specified in RFC 2822 format."

  - name: "account_sid"
    type: "string"
    description: "The SID of the Account that created this Call resource."

  - name: "annotation"
    type: "string"
    description: ""

  - name: "answered_by"
    type: "string"
    description: "Either human or machine if this call was initiated with answering machine detection. Empty otherwise."

  - name: "api_version"
    type: "string"
    description: "The API version used to create the call."

  - name: "caller_name"
    type: "string"
    description: "The caller's name if this call was an incoming call to a phone number with caller ID Lookup enabled. Otherwise, empty."

  - name: "date_created"
    type: "date-time"
    description: "The date and time in GMT that this resource was created specified in RFC 2822 format."

  - name: "direction"
    type: "string"
    description: "A string describing the direction of the call. Can be: inbound for inbound calls, outbound-api for calls initiated via the REST API or outbound-dial for calls initiated by a <Dial> verb. Using Elastic SIP Trunking, the values can be trunking-terminating for outgoing calls from your communications infrastructure to the PSTN or trunking-originating for incoming calls to your communications infrastructure from the PSTN."

  - name: "duration"
    type: "integer"
    description: "The length of the call in seconds. This value is empty for busy, failed, unanswered, or ongoing calls."

  - name: "end_time"
    type: "date-time"
    description: "The time the call ended, given as GMT in RFC 2822 format. Empty if the call did not complete successfully."

  - name: "forwarded_from"
    type: "string"
    description: "The forwarding phone number if this call was an incoming call forwarded from another number (depends on carrier supporting forwarding). Otherwise, empty."

  - name: "from"
    type: "string"
    description: "The phone number, SIP address, Client identifier or SIM SID that made this call. Phone numbers are in E.164 format (e.g., +16175551212). SIP addresses are formatted as name@company.com. Client identifiers are formatted client:name. SIM SIDs are formatted as sim:sid."

  - name: "from_formatted"
    type: "string"
    description: "The calling phone number, SIP address, or Client identifier formatted for display. Non-North American phone numbers are in E.164 format (e.g., +442071838750)."

  - name: "group_sid"
    type: "string"
    description: "The Group SID associated with this call. If no Group is associated with the call, the field is empty."

  - name: "parent_call_sid"
    type: "string"
    description: "The SID that identifies the call that created this leg."

  - name: "phone_number_sid"
    type: "string"
    description: "If the call was inbound, this is the SID of the IncomingPhoneNumber resource that received the call. If the call was outbound, it is the SID of the OutgoingCallerId resource from which the call was placed."

  - name: "price"
    type: "number"
    description: "The charge for this call, in the currency associated with the account. Populated after the call is completed. May not be immediately available."

  - name: "price_unit"
    type: "string"
    description: "The currency in which Price is measured, in ISO 4127 format (e.g., USD, EUR, JPY). Always capitalized for calls."

  - name: "queue_time"
    type: "integer"
    description: "The wait time in milliseconds before the call is placed."

  - name: "start_time"
    type: "date-time"
    description: "The start time of the call, given as GMT in RFC 2822 format. Empty if the call has not yet been dialed."

  - name: "status"
    type: "string"
    description: "The status of this call. Can be: queued, ringing, in-progress, canceled, completed, failed, busy or no-answer"

  - name: "subresource_uris"
    type: "array"
    description: "A list of subresources available to this call, identified by their URIs relative to https://api.twilio.com."
    subattributes:
    - name: "subresource"
      type: "string"
      description: "Subresource type"

    - name: "uri"
      type: "string"
      description: "URI for the subresource, relative to https://api.twilio.com"

  - name: "to"
    type: "string"
    description: "The phone number, SIP address, Client identifier or SIM SID that received this call. Phone numbers are in E.164 format (e.g., +16175551212). SIP addresses are formatted as name@company.com. Client identifiers are formatted client:name. SIM SIDs are formatted as sim:sid."

  - name: "to_formatted"
    type: "string"
    description: "The phone number, SIP address or Client identifier that received this call. Formatted for display. Non-North American phone numbers are in E.164 format (e.g., +442071838750)."

  - name: "trunk_sid"
    type: "string"
    description: "The unique identifier of the trunk resource that was used for this call. The field is empty if the call was not made using a SIP trunk or if the call is not terminated."

  - name: "uri"
    type: "string"
    description: "The URI of this resource, relative to https://api.twilio.com."
---