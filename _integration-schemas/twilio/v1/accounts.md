---
tap: "twilio"
version: "1"
key: ""

name: "accounts"
doc-link: "https://www.twilio.com/docs/usage/api/account#read-multiple-account-resources"
singer-schema: https://github.com/singer-io/tap-twilio/tree/master/tap_twilio/schemas/accounts.json
description: |
  The **{{ table.name }}** table returns a list of accounts in your {{ integration.display_name }} account.

replication-method: "Full Table"  

api-method:
    name: "Read multiple Account resources"
    doc-link: "https://www.twilio.com/docs/usage/api/account?code-sample=code-list-all-accounts&code-language=curl&code-sdk-version=json"


attributes:
  - name: "sid"
    type: "string"
    primary-key: true
    description: "A 34 character string that uniquely identifies this resource."

  - name: "auth_token"
    type: "string"
    description: "The authorization token for this account. This token should be kept a secret, so no sharing."

  - name: "date_created"
    type: "date-time"
    description: "The date that this account was created, in GMT in RFC 2822 format"

  - name: "date_updated"
    type: "date-time"
    description: "The date that this account was last updated, in GMT in RFC 2822 format."

  - name: "friendly_name"
    type: "string"
    description: "A human readable description of this account, up to 64 characters long. By default the FriendlyName is your email address."

  - name: "owner_account_sid"
    type: "string"
    description: "The unique 34 character id that represents the parent of this account. The OwnerAccountSid of a parent account is it's own sid."

  - name: "status"
    type: "string"
    description: "The status of this account. Usually active, but can be suspended or closed."

  - name: "subresource_uris"
    type: "array"
    description: "Various subresources available for the given Account Instance"
    subattributes:
    - name: "subresource"
      type: "string"
      description: "Subresource type"

    - name: "uri"
      type: "string"
      description: "URI for the subresource, relative to https://api.twilio.com"

  - name: "type"
    type: "string"
    description: "The type of this account. Either Trial or Full if it's been upgraded"

  - name: "uri"
    type: "string"
    description: "The URI for this resource, relative to https://api.twilio.com"
---