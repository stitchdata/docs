---
tap: "helpscout"
version: "1.0"

key: "customer"
name: "customers"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-helpscout/blob/master/tap_helpscout/schemas/customers.json"
description: |
  The `{{ table.name }}` table contains info about the customers in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List customers"
    doc-link: "https://developer.helpscout.com/mailbox-api/endpoints/customers/list/"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The customer ID."
    foreign-key-id: "customer-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The UTC time when the customer was last updated."

  - name: "address"
    type: "object"
    description: "The customer's physical address."
    subattributes:
      - name: "city"
        type: "string"
        description: "The city."

      - name: "country"
        type: "string"
        description: "The country."

      - name: "lines"
        type:  "array"
        description: "The street lines of the address."
        subattributes:
          - name: "value"
            type: "string"
            description: "The street line of the address."

      - name: "postal_code"
        type: "string"
        description: "The postal code."

      - name: "state"
        type: "string"
        description: "The state."

  - name: "age"
    type: "string"
    description: "The customer's age."

  - name: "background"
    type: "string"
    description: "The contents of the **Notes** field from the user interface in {{ integration.display_name }}."

  - name: "chats"
    type: "array"
    description: "Details about the customer's chat handles."
    subattributes:
      - name: "id"
        type: "integer"
        description: "The chat handle ID."

      - name: "value"
        type: "string"
        description: "The chat handle."

      - name: "type"
        type: "string"
        description: "The type of the chat handle. For example: `icq`"

  - name: "created_at"
    type: "date-time"
    description: "The UTC time when the customer was created."

  - name: "emails"
    type: "array"
    description: "Details about the customer's email addresses."
    subattributes:
      - name: "id"
        type: "integer"
        description: "The email address ID."

      - name: "value"
        type: "string"
        description: "The email address."

      - name: "type"
        type: "string"
        description: "The type of the email address. For example: `work`"

  - name: "first_name"
    type: "string"
    description: "The first name of the customer."

  - name: "gender"
    type: "string"
    description: |
      The customer's gender. Possible values are:

      - `male`
      - `female`
      - `unknown`

  - name: "job_title"
    type: "string"
    description: "The customer's job title."

  - name: "last_name"
    type: "string"
    description: "The last name of the customer."

  - name: "location"
    type: "string"
    description: "The location of the customer."

  - name: "organization"
    type: "string"
    description: "The organization the customer is associated with."

  - name: "phones"
    type: "array"
    description: "Details about the customer's phone number(s)."
    subattributes:
      - name: "id"
        type: "integer"
        description: "The phone number ID."

      - name: "value"
        type: "string"
        description: "The phone number."

      - name: "type"
        type: "string"
        description: "The type of phone number. For example: `mobile`"

  - name: "photo_type"
    type: "string"
    description: |
      The type of photo associated with the customer. Possible values are:

      - `unknown`
      - `gravatar`
      - `twitter`
      - `facebook`
      - `googleprofile`
      - `googleplus`
      - `linkedin`

  - name: "photo_url"
    type: "string"
    description: "The URL of the customer's photo."

  - name: "social_profiles"
    type: "array"
    description: "Details about the customer's social profiles."
    subattributes:
      - name: "id"
        type: "integer"
        description: "The social profile ID."

      - name: "value"
        type: "string"
        description: "The URL of the customer's social profile."

      - name: "type"
        type: "string"
        description: "The type of social profile. For example: `twitter`"

  - name: "websites"
    type: "array"
    description: "Details about the customer's websites."
    subattributes:
      - name: "id"
        type: "integer"
        description: "The website ID."

      - name: "value"
        type: "string"
        description: "The URL of the website."
---