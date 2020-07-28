---
tap-reference: "intercom"

version: "15-10-2015"

foreign-keys:
  - id: "admin-id"
    attribute: "id"
    table: "admins"
    all-foreign-keys:
      - table: "admins"
        join-on: "id"
      - table: "conversations"
        subtable: "conversation_parts"
        join-on: "assigned_to"
      - table: "conversations"
        subattribute: "assignee"

  - id: "author-id"
    attribute: "id"
    table: "authors"
    all-foreign-keys:
      - table: "admins"
      - table: "contacts"
      - table: "users"
      - table: "conversations"
        subtable: "conversation_parts__author"

  - id: "company-id"
    attribute: "id"
    table: "companies"
    all-foreign-keys:
      - table: "companies"
        join-on: "id"
      - table: "contacts"
        subtable: "companies"
        join-on: "id"
      - table: "users"
        subtable: "companies"

  - id: "company-segment-id"
    attribute: "id"
    table: "company_segments"
    all-foreign-keys:
      - table: "company_segments"
        join-on: "id"
      - table: "contacts"
        subtable: "segments"
        join-on: "id"

  - id: "contact-id"
    attribute: "id"
    table: "contacts"
    all-foreign-keys:
      - table: "contacts"
        join-on: "id"
      - table: "conversations"
        subattribute: "user"

  - id: "conversation-id"
    attribute: "id"
    table: "conversations"
    all-foreign-keys:
      - table: "conversations"
        join-on: "id"

  - id: "segment-id"
    attribute: "id"
    table: "segments"
    all-foreign-keys:
      - table: "companies"
        subtable: "segments__segments"
      - table: "contacts"
        subtable: "segments__segments"
      - table: "segments"
      - table: "users"
        subtable: "segments__segments"

  - id: "tag-id"
    attribute: "id"
    table: "tags"
    all-foreign-keys:
      - table: "companies"
        subtable: "tags__tags"
      - table: "contacts"
        subtable: "tags__tags"
      - table: "conversations"
        subtable: "tags__tags"
      - table: "tags"
      - table: "users"
        subtable: "tags__tags"

  - id: "user-id"
    attribute: "id"
    table: "users"
    all-foreign-keys:
      - table: "users"
      - table: "contacts"
      - table: "conversations"
        subattribute: "user"
      - table: "conversations"
        subtable: "customers"
---