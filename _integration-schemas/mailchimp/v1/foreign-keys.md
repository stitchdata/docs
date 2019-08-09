---
tap-reference: "mailchimp"

version: "1.0"

foreign-keys:
  - id: "automations-id"
    attribute: "automation_id"
    table: "automations"
    all-foreign-keys:
      - table: "automations"
        join-on: "id"

  - id: "campaign-id"
    attribute: "campaign_id"
    table: "campaigns"
    all-foreign-keys:
      - table: "campaigns"
        join-on: "id"
      - table: "reports_email_activity"

  - id: "list-id"
    attribute: "list_id"
    table: "lists"
    all-foreign-keys:
      - table: "automations"
        subattribute: "recipients"
      - table: "campaigns"
        subattribute: "recipients"
      - table: "list_members"
      - table: "list_segment_members"
      - table: "list_segments"
      - table: "lists"
        join-on: "id"
      - table: "reports_email_activity"

  # - id: "list-member-id"
  #   attribute: ""
  #   table: "list_members"
  #   all-foreign-keys:

  # - id: "list-segment-member-id"
  #   attribute: ""
  #   table: "list_segment_members"
  #   all-foreign-keys:

  # - id: "list-segment-id"
  #   attribute: ""
  #   table: "list_segments"
  #   all-foreign-keys:
---