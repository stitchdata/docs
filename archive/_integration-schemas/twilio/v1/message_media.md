---
tap: "twilio"
version: "1"
key: ""

name: "message_media"
doc-link: "https://www.twilio.com/docs/sms/api/media-resource#read-multiple-media-resources"
singer-schema: https://github.com/singer-io/tap-twilio/tree/master/tap_twilio/schemas/message_media.json
description: |
  The **{{ table.name }}** table returns the list of media associated with your {{ integration.display_name }} message.

replication-method: "Full Table"

api-method:
    name: "Read multiple Media resources"
    doc-link: "https://www.twilio.com/docs/sms/api/media-resource?code-sample=code-read-media&code-language=curl&code-sdk-version=json"

attributes:
  - name: "sid"
    type: "string"
    primary-key: true
    description: "The unique string that that we created to identify this Media resource."

  - name: "account_sid"
    type: "string"
    description: "The SID of the Account that created this Media resource."

  - name: "content_type"
    type: "string"
    description: "The default mime-type of the media, for example image/jpeg, image/png, or image/gif"

  - name: "date_created"
    type: "date-time"
    description: "The date and time in GMT that this resource was created specified in RFC 2822 format."

  - name: "date_updated"
    type: "date-time"
    description: "The date and time in GMT that this resource was last updated, specified in RFC 2822 format."

  - name: "parent_sid"
    type: "string"
    description: "The SID of the resource that created the media."

  - name: "uri"
    type: "string"
    description: "The URI of this resource, relative to https://api.twilio.com."
---