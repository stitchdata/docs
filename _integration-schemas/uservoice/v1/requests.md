---
tap: "uservoice"
# version: "1.0"

name: "requests"
doc-link: https://developer.uservoice.com/docs/api/v2/reference/#/
singer-schema: https://github.com/singer-io/tap-uservoice/blob/master/tap_uservoice/streams/requests.py
description: |
  The `{{ table.name }}` table contains info about requests, which are specific pieces of feedback submitted by your end users. Requests are associated with suggestions, and users are counted as supporters of the suggestion.

  Unlike suggestions, requests are captured by your team on behalf of end users.

replication-method: "Key-based Incremental"

api-method:
  name: List requests
  doc-link: https://developer.uservoice.com/docs/api/v2/reference/#list-requests

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The request ID."
    #foreign-key-id: "request-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the request was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the request was created."

  - name: "body"
    type: "string"
    description: "The text of the request. For example: `User considers the lack of this feature a blocker.`"

  - name: "body_mime_type"
    type: "string"
    description: "The MIME type of the `body`."

  - name: "source_url"
    type: "string"
    description: "The URL of the page the request was captured on, such as a Facebook post or Tweet."

  - name: "source_type"
    type: "string"
    description: "The type of the source."

  - name: "source_guid"
    type: "string"
    description: "The GUID of the source."

  - name: "channel"
    type: "string"
    description: "The channel used to create the request. For example: `api`"

  - name: "severity"
    type: "integer"
    description: "The severity of the request."

  - name: "links"
    type: "object"
    description: "Details about the suggestion(s), user(s), ticket(s), etc. associated with the request."
    object-attributes: 
      - name: "suggestion"
        type: "integer"
        description: "The ID of the suggestion associated with the request."
        foreign-key-id: "suggestion-id"

      - name: "user"
        type: "integer"
        description: "The ID of the end user associated with the request."
        foreign-key-id: "user-id"

      - name: "ticket"
        type: "integer"
        description: "The ID of the ticket associated with the request."

      - name: "created_by"
        type: "integer"
        description: "The ID of the user who created the request."
        foreign-key-id: "user-id"

      - name: "updated_by"
        type: "integer"
        description: "The ID of the user who last updated the request."
        foreign-key-id: "user-id"

      - name: "supporter"
        type: "integer"
        description: "The ID of the supporter associated with the request."
        foreign-key-id: "supporter-id"

      - name: "sfdc_opportunity"
        type: "integer"
        description: "The ID of the Salesforce opportunity associated with the request."
---