---
tap: "linkedin-ads"
version: "3"
key: "video-ad"

name: "video_ads"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-linkedin-ads/blob/master/tap_linkedin_ads/schemas/video_ads.json"
description: |
  The `{{ table.name }}` table contains info about the video ads in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "Account Finder; Sponsored Contents"
    doc-link: "https://docs.microsoft.com/en-us/linkedin/marketing/integrations/ads/advertising-targeting/create-and-manage-video?view=li-lms-unversioned&tabs=http&viewFallbackFrom=li-lms-2022-07#finders"

attributes:
  - name: "account"
    type: "string"
    description: ""

  - name: "account_id"
    type: "integer"
    description: ""

  - name: "ad_context"
    type: "object"
    description: ""
    subattributes:
    - name: "dsc_status"
      type: "string"
      description: ""

    - name: "dsc_name"
      type: "string"
      description: ""

    - name: "dsc_ad_type"
      type: "string"
      description: ""

    - name: "dsc_ad_account"
      type: "string"
      description: ""


  - name: "author"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "id"
    type: "string"
    description: ""
    primary-key: true

  - name: "last_modified_at"
    type: "date-time"
    description: ""
    replication-key: true

  - name: "name"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""
---