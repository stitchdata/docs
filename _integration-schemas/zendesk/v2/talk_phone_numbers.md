---
tap: "zendesk"
version: "2"
key: ""

name: "talk_phone_numbers"
doc-link: "https://developer.zendesk.com/api-reference/voice/talk-api/phone_numbers/"
singer-schema: "https://github.com/singer-io/tap-zendesk/blob/master/tap_zendesk/schemas/talk_phone_numbers.json"
description: "This table contains data about phone numbers in Zendesk Talk."

api-method:
    name: "TalkPhoneNumbers"
    doc-link: "https://developer.zendesk.com/api-reference/voice/talk-api/phone_numbers/"

replication-method: "Full Table"

table-key-properties: "id"
valid-replication-keys: ""

attributes:
  - name: "brand_id"
    type: "integer"
    description: "ID of brand associated with the phone number"

  - name: "capabilities"
    type: "object"
    description: "Whether a phone number has mms, sms, or voice capability"
    subattributes:
    - name: "sms"
      type: "boolean"
      description: ""

    - name: "mms"
      type: "boolean"
      description: ""

    - name: "voice"
      type: "boolean"
      description: ""


  - name: "categorised_greetings"
    type: "object"
    description: "Greeting category ids and names."
    subattributes:

  - name: "categorised_greetings_with_sub_settings"
    type: "object"
    description: "The id and any settings associated with each greeting category. If the category has no settings, it defaults to the category name."
    subattributes:

  - name: "country_code"
    type: "string"
    description: "The ISO code of the country for this number"

  - name: "created_at"
    type:  "date-time"
    description: "The date and time the phone number was created"

  - name: "default_greeting_ids"
    type: "array"
    description: "The names of default system greetings associated with the phone number."
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "default_group_id"
    type: "integer"
    description: "Default group id. *Writeable on most of the plans."

  - name: "display_number"
    type: "string"
    description: "The formatted phone number"

  - name: "external"
    type: "boolean"
    description: "The external caller id number"

  - name: "greeting_ids"
    type: "array"
    description: "Custom greetings associated with the phone number."
    subattributes:
    - name: "items"
      type: "integer"
      description: ""

  - name: "group_ids"
    type: "array"
    description: "An array of associated groups. Writeable on most plans. If omnichannel routing is enabled, only the first group_id provided is accepted for routing purposes"
    subattributes:
    - name: "items"
      type: "integer"
      description: ""

  - name: "id"
    type: "integer"
    description: "Automatically assigned upon creation"
    primary-key: true

  - name: "ivr_id"
    type: "integer"
    description: "ID of IVR associated with the phone number"

  - name: "line_type"
    type: "string"
    description: "The type line, either phone or digital"
    
  - name: "location"
    type: "string"
    description: "The number's geographical location. For example, 'CA' or 'Leeds'"

  - name: "name"
    type: "string"
    description: "The nickname if one is set. Otherwise the display_number"

  - name: "nickname"
    type: "string"
    description: "The nickname of the number if one is set"

  - name: "number"
    type: "string"
    description: "The phone number digits"

  - name: "outbound_enabled"
    type: "boolean"
    description: "Whether or not the phone number has outbound enabled"

  - name: "priority"
    type: "integer"
    description: "Level of priority associated with the phone number"

  - name: "recorded"
    type: "boolean"
    description: "Whether calls for the number are recorded or not"

  - name: "schedule_id"
    type: "integer"
    description: "ID of schedule associated with the phone number"

  - name: "sms_enabled"
    type: "boolean"
    description: "Whether or not the phone number has sms enabled"

  - name: "sms_group_id"
    type: "integer"
    description: "The group associated with this phone number"

  - name: "token"
    type: "string"
    description: "A generated token, unique for each phone number and used when provisioning the number. *Writeable on create only."

  - name: "toll_free"
    type: "boolean"
    description: "Whether the number is toll-free or local"

  - name: "transcription"
    type: "boolean"
    description: "Whether calls for the number are transcribed or not"

  - name: "voice_enabled"
    type: "boolean"
    description: "Whether or not the phone number has voice enabled"
---