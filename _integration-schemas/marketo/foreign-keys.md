---
tap-reference: "marketo"

version: "2"

foreign-keys:
  - id: "activity-id"
    attribute: "marketoGuid"
    table: "activities_[activity_type]"
    all-foreign-keys:
      - table: "activities_[activity_type]"

  - id: "activity-type-id"
    attribute: "activityTypeId"
    table: "activity_types"
    all-foreign-keys:
      - table: "activities_[activity_type]"
      - table: "activity_types"
        join-on: "id"

  - id: "campaign-id"
    attribute: "campaignId"
    table: "campaigns"
    all-foreign-keys:
      - table: "campaigns"
        join-on: "id"

  - id: "lead-id"
    attribute: "leadId"
    table: "leads"
    all-foreign-keys:
      - table: "activities"
      - table: "leads"
        join-on: "id"

  - id: "list-id"
    attribute: "listId"
    table: "lists"
    all-foreign-keys:
      - table: "lists"
        join-on: "id"

  - id: "program-id"
    attribute: "programId"
    table: "programs"
    all-foreign-keys:
      - table: "campaigns"
      - table: "programs"
        join-on: "id"
---