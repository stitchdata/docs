---
tap: "linkedin-ads"
version: "1.0"
key: "account-user"

name: "account_users"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-linkedin-ads/blob/master/tap_linkedin_ads/schemas/account_users.json"
description: |
  The `{{ table.name }}` table contains info about the users who have permissions to an ad account.

replication-method: "Key-based Incremental"

api-method:
  name: "Find Ad Account Users by Accounts"
  doc-link: "https://docs.microsoft.com/en-us/linkedin/marketing/integrations/ads/account-structure/create-and-manage-account-users#find-ad-account-users-by-accounts"

attributes:
  - name: "account_id"
    type: "integer"
    primary-key: true
    description: "The ID of the account associated with the user."
    #foreign-key-id: "account-id"

  - name: "user_person_id"
    type: "string"
    primary-key: true
    description: "The user's person ID."
    foreign-key-id: "user-id" 
  
  - name: "last_modified_time"
    type: "date-time"
    replication-key: true
    description: "The time the user was last modified."

  - name: "account"
    type: "string"
    description: "The advertising account's URN." 

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
    description: "The time the user was las modified."
  
  - name: "role"
    type: "string"
    description: |
      The user's role in the account. Possible values are:

      - `VIEWER`
      - `CREATIVE_MANAGER`
      - `CAMPAIGN_MANAGER`
      - `ACCOUNT_MANAGER`
      - `ACCOUNT_BILLING_ADMIN`
  
  - name: "user"
    type: "string"
    description: "The associated user's URN."
---