---
tap: "twilio"
version: "1"
key: ""

name: "incoming_phone_numbers"
doc-link: "https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource#read-multiple-incomingphonenumber-resources"
singer-schema: https://github.com/singer-io/tap-twilio/tree/master/tap_twilio/schemas/incoming_phone_numbers.json
description: |
  The **{{ table.name }}** table returns a list of `IncomingPhoneNumbers` in your {{ integration.display_name }} account that require the specified address.

replication-method: "Key-based Incremental"

api-method:
    name: "Read multiple IncomingPhoneNumber resources"
    doc-link: "https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource?code-sample=code-list-all-incomingphonenumber-resources-for-your-account&code-language=curl&code-sdk-version=json"

attributes:
  - name: "sid"
    type: "string"
    primary-key: true
    description: "The unique string that that we created to identify this IncomingPhoneNumber resource."

  - name: "date_updated"
    type: "date-time"
    replication-key: true
    description: "The date and time in GMT that the resource was last updated specified in RFC 2822 format."

  - name: "account_sid"
    type: "string"
    description: "The SID of the Account that created the IncomingPhoneNumber resources to read."

  - name: "address_requirements"
    type: "string"
    description: "The type of Address resource the phone number requires. Can be: none, any, local, or foreign. none means no address is required. any means an address is required, but it can be anywhere in the world. local means an address in the phone number's country is required. foreign means an address outside of the phone number's country is required."

  - name: "address_sid"
    type: "string"
    description: "The SID of the Address resource associated with the phone number."

  - name: "api_version"
    type: "string"
    description: "The API version used to start a new TwiML session."

  - name: "beta"
    type: "boolean"
    description: "Whether to include phone numbers new to the Twilio platform. Can be: true or false and the default is true."

  - name: "bundle_sid"
    type: "string"
    description: "The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations."

  - name: "capabilities"
    type: "object"
    description: "The set of Boolean properties that indicate whether a phone number can receive calls or messages. Capabilities are Voice, SMS, MMS, and fax and each capability can be: true or false."
    subattributes:
    - name: "voice"
      type: "boolean"
      description: ""

    - name: "sms"
      type: "boolean"
      description: ""

    - name: "mms"
      type: "boolean"
      description: ""

    - name: "fax"
      type: "boolean"
      description: ""


  - name: "date_created"
    type: "date-time"
    description: "The date and time in GMT that the resource was created specified in RFC 2822 format."

  - name: "emergency_address_sid"
    type: "string"
    description: "The SID of the emergency address configuration that we use for emergency calling from this phone number."

  - name: "emergency_address_status"
    type: "string"
    description: "The status of address registration with emergency services. A registered emergency address will be used during handling of emergency calls from this number."

  - name: "emergency_status"
    type: "string"
    description: "The parameter displays if emergency calling is enabled for this number. Active numbers may place emergency calls by dialing valid emergency numbers for the country."

  - name: "friendly_name"
    type: "string"
    description: "A string that identifies the IncomingPhoneNumber resources to read."

  - name: "identity_sid"
    type: "string"
    description: "The SID of the Identity resource that we associate with the phone number. Some regions require an Identity to meet local regulations."

  - name: "origin"
    type: "string"
    description: "Whether to include phone numbers based on their origin. Can be: twilio or hosted. By default, phone numbers of all origin are included."

  - name: "phone_number"
    type: "string"
    description: "The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial numbers and use '*' as a wildcard for any digit."

  - name: "sms_application_sid"
    type: "string"
    description: "The SID of the application that handles SMS messages sent to the phone number. If an sms_application_sid is present, we ignore all sms_*_url values and use those of the application."

  - name: "sms_fallback_method"
    type: "string"
    description: "The HTTP method we use to call sms_fallback_url. Can be: GET or POST."

  - name: "sms_fallback_url"
    type: "string"
    description: "The URL that we call when an error occurs while retrieving or executing the TwiML from sms_url."

  - name: "sms_method"
    type: "string"
    description: "The HTTP method we use to call sms_url. Can be: GET or POST."

  - name: "sms_url"
    type: "string"
    description: "The URL we call when the phone number receives an incoming SMS message."

  - name: "status"
    type: "string"
    description: "Status of phone number"

  - name: "status_callback"
    type: "string"
    description: "The URL we call using the status_callback_method to send status information to your application."

  - name: "status_callback_method"
    type: "string"
    description: "The HTTP method we use to call status_callback. Can be: GET or POST."

  - name: "trunk_sid"
    type: "string"
    description: "The SID of the Trunk that handles calls to the phone number. If a trunk_sid is present, we ignore all of the voice urls and voice applications and use those set on the Trunk. Setting a trunk_sid will automatically delete your voice_application_sid and vice versa."

  - name: "uri"
    type: "string"
    description: "The URI of the resource, relative to https://api.twilio.com."

  - name: "voice_application_sid"
    type: "string"
    description: "The SID of the application that handles calls to the phone number. If a voice_application_sid is present, we ignore all of the voice urls and use those set on the application. Setting a voice_application_sid will automatically delete your trunk_sid and vice versa."

  - name: "voice_caller_id_lookup"
    type: "boolean"
    description: "Whether we look up the caller's caller-ID name from the CNAM database ($0.01 per look up). Can be: true or false."

  - name: "voice_fallback_method"
    type: "string"
    description: "The HTTP method we use to call voice_fallback_url. Can be: GET or POST."

  - name: "voice_fallback_url"
    type: "string"
    description: "The URL that we call when an error occurs retrieving or executing the TwiML requested by url."

  - name: "voice_method"
    type: "string"
    description: "The HTTP method we use to call voice_url. Can be: GET or POST."

  - name: "voice_receive_mode"
    type: "string"
    description: ""

  - name: "voice_url"
    type: "string"
    description: "The URL we call when the phone number receives a call. The voice_url will not be used if a voice_application_sid or a trunk_sid is set."
---