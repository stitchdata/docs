---
tap: "lever"
version: "1"
key: "posting"

name: "postings"
doc-link: "https://hire.lever.co/developer/documentation#postings"
singer-schema: "https://github.com/singer-io/tap-lever/blob/master/tap_lever/schemas/postings.json"
description: |
  The `{{ table.name }}` table contains info about job postings in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "List all postings"
  doc-link: "https://hire.lever.co/developer/documentation#list-all-postings"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The job posting ID."
    foreign-key-id: "posting-id"

  - name: "updatedAt"
    type: "date-time"
    replication-key: true
    description: "The datetime when the posting was last updated."

  - name: "categories"
    type: "object"
    description: ""
    subattributes:
      - name: "commitment"
        type: "string"
        description: "The tag for the position's work type. For example: `Full-time`, `Part-time`, etc."

      - name: "department"
        type: "string"
        description: "The tag for the department to which the posting's team belongs."

      - name: "level"
        type: "string"
        description: "**This field has been deprecated by {{ integration.display_name }}.** The tag for the posting's level. For example: `Senior`"

      - name: "location"
        type: "string"
        description: "The tag for the posting's position location."

      - name: "team"
        type: "string"
        description: "The tag for the team to which the posting belongs. For example: `Engineering`, `Documentation`"

  - name: "content"
    type: "object"
    description: "The content of the posting, including any custom questions."
    subattributes:
      - name: "closing"
        type: "string"
        description: "The plaintext closing statement on the posting."

      - name: "customQuestions"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "description"
        type: "string"
        description: "The plaintext posting description shown at the top of the jobs page."

      - name: "lists"
        type: "array"
        description: "A list of requirements, responsibilities, etc. added to the posting."
        subattributes:
          - name: "content"
            type: "string"
            description: "The HTML content of the list."

          - name: "text"
            type: "string"
            description: "The title of the list."

  - name: "createdAt"
    type: "date-time"
    description: "The datetime when the posting was created."

  - name: "distributionChannels"
    type: "array"
    description: "A list of job sites that a `published` posting appears on."
    subattributes:
      - name: "value"
        type: "string"
        description: "The job site."

  - name: "followers"
    type: "string"
    description: "A list of IDs of users following the posting."
    subattributes:
      - name: "value"
        type: "string"
        description: "The user ID."
        foreign-key-id: "user-id"

  - name: "hiringManager"
    type: "string"
    description: "The user ID of the hiring manager for the job posting."
    foreign-key-id: "user-id"

  - name: "owner"
    type: "string"
    description: "The ID of the posting owner. The posting owner is the user who is responsible for managing all candidates who applied to the position."
    foreign-key-id: "user-id"

  - name: "reqCode"
    type: "string"
    description: "The requisition code associated with the posting. **This field has been deprecated by {{ integration.display_name }}.**"

  - name: "state"
    type: "string"
    description: |
      The posting's current status. Refer to [{{ integration.display_name }}'s documentation](https://hire.lever.co/developer/documentation#postings){:target="new"} for a list of possible values.

  - name: "tags"
    type: "array"
    description: "A list of additional posting tags."
    subattributes:
      - name: "value"
        type: "string"
        description: "The posting tag."

  - name: "text"
    type: "string"
    description: "The title of the job posting."

  - name: "urls"
    type: "object"
    description: "A list of the list, show, and apply URLs for the posting."
    subattributes:
      - name: "apply"
        type: "string"
        description: "The URL for the posting's apply page."

      - name: "list"
        type: "string"
        description: "The URL for the account's list of postings."

      - name: "show"
        type: "string"
        description: "The URL for the posting's information page."

  - name: "user"
    type: "string"
    description: "The ID of the user who created the posting."
    foreign-key-id: "user-id"
---