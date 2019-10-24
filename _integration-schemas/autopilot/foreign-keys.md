---
tap-reference: "autopilot"

version: "1.0"

foreign-keys:
  - id: "contact-id"
    attribute: "contact_id"
    table: "contacts"
    all-foreign-keys:
      - table: "contacts"
        join-on: "id"
      - table: "list_contacts"
      - table: "smart_segments_contacts"

  - id: "segment-id"
    attribute: "segment_id"
    table: "smart_segments"
    all-foreign-keys:
      - table: "smart_segments"
      - table: "smart_segments_contacts"

  - id: "list-id"
    attribute: "list_id"
    table: "lists"
    all-foreign-keys:
      - table: "contacts"
        subtable: "lists"
        join-on: "value"
      - table: "lists"
        join-on: "id"
      - table: "list_contacts"
---