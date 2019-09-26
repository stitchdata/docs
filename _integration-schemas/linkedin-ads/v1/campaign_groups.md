---
tap: "linkedin-ads"
version: "1.0"
key: "campaign-group"

name: "campaign_groups"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-linkedin-ads/blob/master/tap_linkedin_ads/schemas/campaign_groups.json"
description: |
  The `{{ table.name }}` table contains info about the campaign groups in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "Search For Campaign Groups"
    doc-link: "https://docs.microsoft.com/en-us/linkedin/marketing/integrations/ads/account-structure/create-and-manage-campaign-groups#search-for-campaign-groups"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The campaign group ID."
    foreign-key-id: "campaign-group-id"
  
  - name: "last_modified_time"
    type: "date-time"
    replication-key: true
    description: "The time the campaign group was last modified."

  - name: "account"
    type: "string"
    description: "URN identifying the advertising account associated with the campaign."
  
  - name: "account_id"
    type: "integer"
    description: "The ID of the account associated with the campaign group."
    foreign-key-id: "account-id"
  
  - name: "backfilled"
    type: "boolean"
    description: "Indicates whether the campaign group was created organically or to backfill existing campaigns."
  
  - name: "change_audit_stamps"
    type: "object"
    description: ""
    subattributes:
      - name: "created"
        type: "object"
        description: ""
        subattributes:
          - name: "time"
            type: "date-time"
            description: ""
      - name: "last_modified"
        type: "object"
        description: ""
        subattributes:
          - name: "time"
            type: "date-time"
            description: ""
  
  - name: "created_time"
    type: "date-time"
    description: "The time the campaign group was created."
  
  - name: "name"
    type: "string"
    description: "The name of the campaign group used to make it easier to reference a campaign group and recall its purpose."
  
  - name: "run_schedule"
    type: "object"
    description: "Details about the campaign group's run schedule."
    subattributes:
      - name: "end"
        type: "date-time"
        description: "Represents the exclusive (strictly less than) date when to stop running the associated campaigns under this campaign group. If this field is unset, it indicates an open range with no end date."

      - name: "start"
        type: "date-time"
        description: "Represents the inclusive (greater than or equal to) date when to start running the associated campaigns under this campaign group."
  
  - name: "serving_statuses"
    type: "array"
    description: "Array of enums that determine whether or not campaigns within the campaign group may be served."
    subattributes:
      - name: "value"
        type: "string"
        description: "The serving status."
  
  - name: "status"
    type: "string"
    description: |
      The status of campaign group. Possible values are:

      - `ACTIVE` - Denotes that the campaign group is capable of serving ads, subject to run date and budget limitations (as well as any other limitations at the account or campaign level).
      - `ARCHIVED` - Denotes that the campaign group is presently inactive, and should mostly be hidden in the UI until un-archived.
      - `CANCELED` - Denotes that the campaign group has been permanently canceled and cannot be reactivated.
      - `DRAFT` - Denotes that the campaign group is in a preliminary state and should temporarily not be served.
      - `PAUSED` - Denotes that the campaign group meets all requirements to be served, but temporarily should not be.
---