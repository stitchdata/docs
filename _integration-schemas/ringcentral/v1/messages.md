---
tap: "ringcentral"
version: "1"
key: ""

name: "messages"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-ringcentral/blob/master/tap_ringcentral/schemas/messages.json"
description: |
  The `{{ table.name }}` contains info about an extension mailbox's messages.

replication-method: "Key-based Incremental"

replication-key:
  name: "dateFrom : dateTo"

api-method:
    name: "Get Message List"
    doc-link: "https://developers.ringcentral.com/api-reference/Message-Store/listMessages"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The message ID."
    foreign-key-id: "message-id"

  - name: "conversationId"
    type: "anything"
    primary-key: true
    description: "The conversation ID."
    # foreign-key-id: "conversation-id"

  - name: "_contact_id"
    type: "integer"
    description: "The contact ID."
    foreign-key-id: "contact-id"

  - name: "attachments"
    type: "anything"
    description: "The list of message attachments."
    subattributes:
      - name: "id"
        type: "string"
        description: "The attachment ID."

      - name: "uri"
        type: "string"
        description: "Canonical URI of a message attachment."

      - name: "type"
        type: "string"
        description: |
          The type of message attachment. Possible values are:

          - `AudioRecording`
          - `AudioTranscription`
          - `Text`
          - `SourceDocument`
          - `RenderedDocument`
          - `MmsAttachment`

      - name: "contentType"
        type: "string"
        description: "MIME type for a given attachment, for instance 'audio/wav'."

      - name: "vmDuration"
        type: "integer"
        description: "Supported for `Voicemail` only. Duration of a voicemail in seconds."

      - name: "filename"
        type: "string"
        description: "The name of the attached file."

      - name: "size"
        type: "integer"
        description: "The size of the attachment, in bytes."

  - name: "availability"
    type: "string"
    description: "The message availability status."

  - name: "conversation"
    type: "anything"
    description: "SMS and Pager only. Details about the conversation the message belongs to."
    subattributes:
      - name: "id"
        type: "string"
        description: "The conversation ID."
        # foreign-key-id: "conversation-id"

  - name: "coverIndex"
    type: "integer"
    description: ""

  - name: "creationTime"
    type: "date-time"
    description: "The datetime of when the message was created. This value is in ISO 8601 format, including the timezone."

  - name: "deleted"
    type: "anything"
    description: "Indicates if the message has been deleted."

  - name: "direction"
    type: "string"
    description: |
      The direction of the message. Possible values are:

      - `inbound`
      - `outbound`

  - name: "faxPageCount"
    type: "integer"
    description: "The page count of a fax message."

  - name: "faxResolution"
    type: "string"
    description: |
      The resolution of a fax message. Possible values are:

      - `high`
      - `low`

  - name: "from"
    type: "object"
    description: "The sender."
    subattributes: &person-details
      - name: "extensionNumber"
        type: "string"
        description: "Extension short number (usually 3 or 4 digits). This property is filled when parties communicate by means of short internal numbers, for example when calling to other extension or sending/receiving Company Pager message."

      - name: "messageStatus"
        type: "string"
        description: |
          Status of a message. Returned for outbound fax messages only. Possible values are:

          - `Queued`
          - `Sent`
          - `Delivered`
          - `DeliveryFailed`
          - `SendingFailed`
          - `Received`

      - name: "faxErrorCode"
        type: "string"
        description: |
          Fax only. Error code returned in case of fax sending failure. Returned if `messageStatus: SendingFailed`.

          Possible values are:

          - `InternationalCallingDisabled`
          - `DestinationCountryDisabled`
          - `NoAnswer`
          - `LineBusy`
          - `CallerHungUp`
          - `UnknownCountryCode`
          - `InvalidNumber`
          - `NotAccepted`
          - `CallDeclined`
          - `TooManyCallsPerLine`
          - `NotEnoughCredits`
          - `SentPartially`
          - `CallFailed`

      - name: "location"
        type: "string"
        description: "Contains party location (city, state) if one can be determined from `phoneNumber`. This property is filled only when `phoneNumber` is not empty and server can calculate location information from it (for example, this information is unavailable for US toll-free numbers)."

      - name: "name"
        type: "string"
        description: "Symbolic name associated with a party. If the phone does not belong to the known extension, only the location is returned, the name is not determined."

      - name: "phoneNumber"
        type: "string"
        description: "Phone number of a party. Usually it is a plain number including country and area code like `18661234567`. But sometimes it could be returned from database with some formatting applied, for example `(866)123-4567`. This property is filled in all cases where parties communicate by means of global phone numbers, for example when calling to direct numbers or sending/receiving SMS."

  - name: "lastModifiedTime"
    type: "date-time"
    description: "The datetime of when the message was last modified. This value is in ISO 8601 format, including the timezone."

  - name: "messageStatus"
    type: "string"
    description: |
      The message's delivery status. Possible values are:

      - `Queued`
      - `Sent`
      - `Delivered`
      - `DeliveryFailed`
      - `SendingFailed`
      - `Received`

  - name: "priority"
    type: "string"
    description: "The message priority - `normal` or `high`."

  - name: "readStatus"
    type: "string"
    description: "The read status of a message - `read` or `unread`."

  - name: "smsSendingAttemptsCount"
    type: "anything"
    description: "The number of attempts made to send an outbound SMS."

  - name: "subject"
    type: "anything"
    description: "The message subject."

  - name: "to"
    type: "anything"
    description: "The recipient's information."
    subattributes: *person-details

  - name: "type"
    type: "string"
    description: "The message type."

  - name: "uri"
    type: "string"
    description: ""

  - name: "vmTranscriptionStatus"
    type: "anything"
    description: |
      Voicemail only. Status of voicemail to text transcription. If VoicemailToText feature is not activated for account, the `NotAvailable` value is returned. Possible values are:

      - `NotAvailable`
      - `InProgress`
      - `TimedOut`
      - `Completed` 
      - `CompletedPartially`
      - `Failed`
---