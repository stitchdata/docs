---
tap: "xero"
version: "1"

name: "users"
doc-link: &api-doc https://developer.xero.com/documentation/api/users
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/users.json
description: |
  The `{{ table.name }}` table contains info about the users in an organisation.

replication-method: "Key-based Incremental"

api-method:
  name: getUsers
  doc-link: *api-doc

attributes:
  - name: "UserID"
    type: "string"
    primary-key: true
    description: "The user ID."
    foreign-key-id: "user-id"

  - name: "UpdatedDateUTC"
    type: "date-time"
    replication-key: true
    description: "The date the user was last updated, in UTC."

  - name: "EmailAddress"
    type: "string"
    description: "The email address of the user."

  - name: "FirstName"
    type: "string"
    description: "The first name of the user."

  - name: "LastName"
    type: "string"
    description: "The last name of the user."

  - name: "IsSubscriber"
    type: "boolean"
    description: "If `true`, the user is the subscriber."

  - name: "OrganisationRole"
    type: "string"
    doc-link: https://developer.xero.com/documentation/api/types#userRoles
    description: |
      The organisation role of the user. Possible values are:

      - `READONLY`
      - `INVOICEONLY`
      - `STANDARD`
      - `FINANCIALADVISER`
      - `MANAGEDCLIENT`
      - `CASHBOOKCLIENT`

  - name: "ValidationErrors"
    type: "array"
    description: "Details about the validation errors associated with the user, if any."
    subattributes:
      - name: "Message"
        type: "string"
        description: "The validation error message."
---