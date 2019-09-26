---
tap: "linkedin-ads"
version: "1.0"

name: "campaign_groups"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-linkedin-ads/blob/master/tap_linkedin_ads/schemas/campaign_groups.json"
description: ""

replication-method: "Key-based Incremental"

replication-key:
  name: "last_modified_time"

api-method:
    name: "Create and Manage Campaign Groups"
    doc-link: "https://docs.microsoft.com/en-us/linkedin/marketing/integrations/ads/account-structure/create-and-manage-campaign-groups#search-for-campaign-groups"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "Numerical identifier for the campaign group."
    foreign-key-id: "campaign-group-id"
  
  - name: "last_modified_time"
    type: "date-time"
    description: "The time the campaign group was last modified."
    replication-key: true

  - name: "account"
    type: "string"
    description: "URN identifying the advertising account associated with the campaign."
  
  - name: "account_id"
    type: "integer"
    description: ""
    foreign-key-id: "account-id"
  
  - name: "backfilled"
    type: "boolean"
    description: "Flag that denotes whether the campaign group was created organically or to backfill existing campaigns."
  
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
    description: ""
    subattributes:
      - name: "end"
        type: "date-time"
        description: "Represents the exclusive (strictly less than) date when to stop running the associated campaigns under this campaign group. If this field is unset, it indicates an open range with no end date."
      - name: "start"
        type: "date-time"
        description: "Represents the inclusive (greater than or equal to) date when to start running the associated campaigns under this campaign group."
  
  - name: "serving_statuses"
    type: "null"
    description: "Array of enums that determine whether or not campaigns within the campaign group may be served."
  
  - name: "status"
    type: "string"
    description: "Status of campaign group."
---
