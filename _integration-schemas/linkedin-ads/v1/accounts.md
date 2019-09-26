---
tap: "linkedin-ads"
version: "1.0"

name: "accounts"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-linkedin-ads/blob/master/tap_linkedin_ads/schemas/accounts.json"
description: |
  The `{{ table.name }}` table contains info about your {{ integration.display_name }} accounts.

replication-method: "Key-based Incremental"

api-method:
    name: "Ad Accounts"
    doc-link: "https://docs.microsoft.com/en-us/linkedin/marketing/integrations/ads/account-structure/create-and-manage-accounts#search-for-accounts"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The internal account ID."
    foreign-key-id: "account-id"
  
  - name: "last_modified_time"
    type: "date-time"
    description: ""
    replication-key: true

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
    description: ""
  
  - name: "currency"
    type: "string"
    description: "The ISO 4217 currency code."

  - name: "name"
    type: "string"
    description: "The account label."
  
  - name: "notified_on_campaign_optimization"
    type: "boolean"
    description: "Indicates if the campaign contact has been notified about an opportunity."
  
  - name: "notified_on_creative_approval"
    type: "boolean"
    description: "Indicates if the creative contact has been notified of approval."
  
  - name: "notified_on_creative_rejection"
    type: "boolean"
    description: "Indicates if the creative contact has been rejected."
  
  - name: "notified_on_end_of_campaign"
    type: "boolean"
    description: "Indicates if the campaign contact has been notified about the end of a campaign."
  
  - name: "reference"
    type: "string"
    description: "The entity on whose behalf the account advertises."
  
  - name: "reference_organization_id"
    type: "integer"
    description: ""
    foreign-key-id: "reference-organization-id"
  
  - name: "reference_person_id"
    type: "string"
    description: ""
    foreign-key-id: "reference-person-id"
  
  - name: "serving_statuses"
     type: "array"
     description: "Details about the account's system serving statuses."
     subattributes:
       - name: "value"
          type: "string"
          description: |
            The account's system serving status. If an account is eligible for serving, the value will be `RUNNABLE`.
            
            Other possible values that indicate why the account isn't servable:
 
            - `STOPPED`
            - `BILLING_HOLD`
            - `ACCOUNT_TOTAL_BUDGET_HOLD`
            - `ACCOUNT_END_DATE_HOLD`
            - `RESTRICTED_HOLD`
            - `INTERNAL_HOLD`
    type: "null"
    description: ""
  
  - name: "status"
    type: "string"
    description: "The account's active status."
  
  - name: "total_budget"
    type: "object"
    description: ""
    subattributes:
      - name: "amount"
        type: "number"
        description: ""
      - name: "currency_code"
        type: "string"
        description: ""
  
  - name: "total_budget_ends_at"
    type: "date-time"
    description: ""
  
  - name: "type"
    type: "string"
    description: "The account type - business or enterprise."
  
  - name: "version"
    type: "object"
    description: ""
    subattributes:
      - name: "version_tag"
        type: "string"
        description: ""
---
