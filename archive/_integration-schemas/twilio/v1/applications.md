---
tap: "twilio"
version: "1"
key: ""

name: "applications"
doc-link: "https://www.twilio.com/docs/usage/api/applications#read-multiple-application-resources"
singer-schema: https://github.com/singer-io/tap-twilio/tree/master/tap_twilio/schemas/applications.json
description: |
  The **{{ table.name }}** table returns a list of application resource representations, each representing an application within your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "Read multiple Application resources"
    doc-link: "https://www.twilio.com/docs/usage/api/applications?code-sample=code-list-all-application-resource-representations&code-language=curl&code-sdk-version=json"

attributes:
  - name: "sid"
    type: "string"
    primary-key: true
    description: "The unique string that that we created to identify the Application resource."

  - name: "date_created"
    type: "date-time"
    replication-key: true
    description: "The date and time in GMT that the resource was created specified in RFC 2822 format."  

  - name: "account_sid"
    type: "string"
    description: "The SID of the Account that created the Application resources to read."

  - name: "api_version"
    type: "string"
    description: "The API version used to start a new TwiML session."

  - name: "date_updated"
    type: "date-time"
    description: "The date and time in GMT that the resource was last updated specified in RFC 2822 format."

  - name: "friendly_name"
    type: "string"
    description: "The string that you assigned to describe the resource."

  - name: "message_status_callback"
    type: "string"
    description: "The URL we call using a POST method to send message status information to your application."

  - name: "sms_fallback_method"
    type: "string"
    description: "The HTTP method we use to call sms_fallback_url. Can be: GET or POST."

  - name: "sms_fallback_url"
    type: "string"
    description: "The URL that we call when an error occurs while retrieving or executing the TwiML from sms_url."

  - name: "sms_method"
    type: "string"
    description: "The HTTP method we use to call sms_url. Can be: GET or POST."

  - name: "sms_status_callback"
    type: "string"
    description: "The URL we call using a POST method to send status information to your application about SMS messages that refer to the application."

  - name: "sms_url"
    type: "string"
    description: "The URL we call when the phone number receives an incoming SMS message."

  - name: "status_callback"
    type: "string"
    description: "The URL we call using the status_callback_method to send status information to your application."

  - name: "status_callback_method"
    type: "string"
    description: "The HTTP method we use to call status_callback. Can be: GET or POST."

  - name: "uri"
    type: "string"
    description: "The URI of the resource, relative to https://api.twilio.com."

  - name: "voice_callback_id_lookup"
    type: "boolean"
    description: "Whether we look up the caller's caller-ID name from the CNAM database (additional charges apply). Can be: true or false."

  - name: "voice_fallback_method"
    type: "string"
    description: "The HTTP method we use to call voice_fallback_url. Can be: GET or POST"

  - name: "voice_fallback_url"
    type: "string"
    description: "The URL that we call when an error occurs retrieving or executing the TwiML requested by url."

  - name: "voice_method"
    type: "string"
    description: "The HTTP method we use to call voice_url. Can be: GET or POST."

  - name: "voice_url"
    type: "string"
    description: "The URL we call when the phone number assigned to this application receives a call."
---    
