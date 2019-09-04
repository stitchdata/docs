---
tap: "linkedin-ads"
version: "1.0"

name: "account_users"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-linkedin-ads/blob/master/tap_linkedin_ads/schemas/account_users.json"
description: ""

replication-method: "Key-based Incremental"

replication-key:
  name: "last_modified_time"

api-method:
    name: "Ad Account Users"
    doc-link: "https://docs.microsoft.com/en-us/linkedin/marketing/integrations/ads/account-structure/create-and-manage-account-users#find-ad-account-users-by-accounts"

attributes:
  - name: "account_id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "account-id"

  - name: "user_person_id"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "user-id" 
  
  - name: "last_modified_time"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "account"
    type: "string"
    description: "The advertisering account's URN." 

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
  
  - name: "last_modified_time"
    type: "date-time"
    description: ""
  
  - name: "role"
    type: "string"
    description: "The associate user's role in the account."
  
  - name: "user"
    type: "string"
    description: "The associated user's URN."
  
  
---
