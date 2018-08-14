---
tap-reference: "intercom"

version: "15-10-2015"

foreign-keys:
  - id: "admin-id"
    attribute: "id"
    table: "admins"
    join-on: "id"
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
    join-on: "id"
    all-foreign-keys:
      - table: "admins"
      - table: "contacts"
      - table: "users"
      - table: "conversations"
        subtable: "conversation_parts__author"

  - id: "company-id"
    attribute: "id"
    table: "companies"
    join-on: "id"
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
    join-on: "id"
    all-foreign-keys:
      - table: "company_segments"
        join-on: "id"
      - table: "contacts"
        subtable: "segments"
        join-on: "id"

  - id: "contact-id"
    attribute: "id"
    table: "contacts"
    join-on: "id"
    all-foreign-keys:
      - table: "contacts"
        join-on: "id"
      - table: "conversations"
        subattribute: "user"

  - id: "conversation-id"
    attribute: "id"
    table: "conversations"
    join-on: "id"
    all-foreign-keys:
      - table: "conversations"
        join-on: "id"

  - id: "segment-id"
    attribute: "id"
    table: "segments"
    join-on: "id"
    all-foreign-keys:
      - table: "segments"
        join-on: "id"
      - table: "users"
        subtable: "segments"

  - id: "tag-id"
    attribute: "id"
    table: "tags"
    join-on: "id"
    all-foreign-keys:
      - table: "tags"
        join-on: "id"
      - table: "contacts"
        subtable: "tags"
        join-on: "id"
      - table: "conversations"
        subtable: "tags"
      - table: "users"
        subtable: "tags"

  - id: "user-id"
    attribute: "id"
    table: "users"
    join-on: "id"
    all-foreign-keys:
      - table: "users"
        join-on: "id"
      - table: "contacts"
      - table: "conversations"
        subattribute: "user"
      - table: "conversations"
        subtable: "customers"
---