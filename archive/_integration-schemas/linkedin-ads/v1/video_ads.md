---
tap: "linkedin-ads"
version: "1"
key: "video-ad"

name: "video_ads"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-linkedin-ads/blob/master/tap_linkedin_ads/schemas/video_ads.json"
description: |
  The `{{ table.name }}` table contains info about the video ads in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "Account Finder; Sponsored Contents"
    doc-link: "https://docs.microsoft.com/en-us/linkedin/marketing/integrations/ads/advertising-targeting/create-and-manage-video#finders"

attributes:
  - name: "content_reference"
    type: "string"
    primary-key: true
    description: "The content URN."
    #foreign-key-id: "content-reference"

  - name: "last_modified_time"
    type: "date-time"
    replication-key: true
    description: "The time the video ad was last modified."

  - name: "account"
    type: "string"
    description: "The ad account associated with the video ad."
  
  - name: "account_id"
    type: "integer"
    description: "The ID of the account associated with the video ad."
    foreign-key-id: "account-id"
  
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
  
  - name: "content_reference_share_id"
    type: "integer"
    description: ""
  
  - name: "content_reference_ucg_post_id"
    type: "integer"
    description: ""
  
  - name: "created_time"
    type: "date-time"
    description: "The time the video ad was created."
  
  - name: "name"
    type: "string"
    description: "Name of the `adDirectSponsoredContents`."
  
  - name: "owner"
    type: "string"
    description: "The owner of the organization."
  
  - name: "owner_organization_id"
    type: "integer"
    description: ""
    #foreign-key-id: "owner-organization-id"
  
  - name: "type"
    type: "string"
    description: "This will be `video`."
---