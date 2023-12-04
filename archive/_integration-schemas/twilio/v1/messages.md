---
tap: "twilio"
version: "1"
key: ""

name: "messages"
doc-link: "https://www.twilio.com/docs/sms/api/message-resource#read-multiple-message-resources"
singer-schema: https://github.com/singer-io/tap-twilio/tree/master/tap_twilio/schemas/messages.json
description: |
  The **{{ table.name }}** table returns a list of messages associated with your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "Read multiple Message resources"
    doc-link: "https://www.twilio.com/docs/sms/api/message-resource?code-sample=code-read-list-all-messages&code-language=curl&code-sdk-version=json"

attributes:
  - name: "sid"
    type: "string"
    primary-key: true
    description: "The unique string that that we created to identify the Message resource."

  - name: "date_updated"
    type: "date-time"
    replication-key: true
    description: "The date and time in GMT that the resource was last updated specified in RFC 2822 format."

  - name: "account_sid"
    type: "string"
    description: "The SID of the Account that sent the message that created the resource."

  - name: "api_version"
    type: "string"
    description: "The API version used to process the message."

  - name: "body"
    type: "string"
    description: "The message text. Can be up to 1,600 characters long."

  - name: "date_created"
    type: "date-time"
    description: "The date and time in GMT that the resource was created specified in RFC 2822 format."

  - name: "date_sent"
    type: "date-time"
    description: "The date and time in GMT that the resource was sent specified in RFC 2822 format. For outgoing messages, this is when we sent the message. For incoming messages, this is when we made the HTTP request to your application."

  - name: "direction"
    type: "string"
    description: "The direction of the message. Can be: inbound for incoming messages, outbound-api for messages initiated by a REST API, outbound-call for messages initiated during a call, or outbound-reply for messages initiated in response to an incoming message."

  - name: "error_code"
    type: "string"
    description: "The error code returned if your message status is failed or undelivered. The error_code provides more information about the failure. If the message was successful, this value is null."

  - name: "error_message"
    type: "string"
    description: "The description of the error_code if your message status is failed or undelivered. If the message was successful, this value is null."

  - name: "from"
    type: "string"
    description: "The phone number (in E.164 format), alphanumeric sender ID, or Wireless SIM that initiated the message. For incoming messages, this will be the number of the sending phone. For outgoing messages, this value will be one of your Twilio phone numbers or the alphanumeric sender ID used."

  - name: "messaging_service_sid"
    type: "string"
    description: "The SID of the Messaging Service used with the message. The value is null if a Messaging Service was not used."

  - name: "num_media"
    type: "integer"
    description: "The number of media files associated with the message. A message can send up to 10 media files."

  - name: "num_segments"
    type: "integer"
    description: "The number of segments that make up the complete message. A message body that is too large to be sent in a single SMS message is segmented and charged as multiple messages. Inbound messages over 160 characters are reassembled when the message is received. Note: When using a Messaging Service to send messages, num_segments will always be 0 in Twilio's response to your API request."

  - name: "price"
    type: "number"
    description: "The amount billed for the message, in the currency specified by price_unit. Note that your account is charged for each segment we send to the handset. Populated after the message has been sent. May not be immediately available."

  - name: "price_unit"
    type: "number"
    description: "The currency in which price is measured, in ISO 4127 format (e.g. usd, eur, jpy)."

  - name: "status"
    type: "string"
    description: "The status of the message. Can be: accepted, scheduled, canceled, queued, sending, sent, failed, delivered, undelivered, receiving, received, or read (WhatsApp only)."

  - name: "subresource_uris"
    type: "array"
    description: ""
    subattributes:
    - name: "subresource"
      type: "string"
      description: ""

    - name: "uri"
      type: "string"
      description: ""

  - name: "to"
    type: "string"
    description: "The phone number in E.164 format that received the message. For incoming messages, this will be one of your Twilio phone numbers. For outgoing messages, this will be the sending phone."

  - name: "uri"
    type: "string"
    description: "The URI of the resource, relative to https://api.twilio.com."
---