---
tap: "linkedin-ads"
version: "1.0"
key: "creative"

name: "creatives"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-linkedin-ads/blob/master/tap_linkedin_ads/schemas/creatives.json"
description: |
  The `{{ table.name }}` table contains info about the creatives in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "Search For Creatives"
    doc-link: "https://docs.microsoft.com/en-us/linkedin/marketing/integrations/ads/account-structure/create-and-manage-creatives#search-for-creatives"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The creative ID."
  
  - name: "last_modified_time"
    type: "date-time"
    replication-key: true
    description: "The time the creative was last modified."

  - name: "campaign"
    type: "string"
    description: "The URN identifying the campaign associated with the creative."
  
  - name: "campaign_id"
    type: "integer"
    description: "The ID of the campaign associated with the creative."
    foreign-key-id: "campaign-id"
  
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
    description: "The time the campaign was created."
  
  - name: "reference"
    type: "string"
    description: "A reference URN for this object to an external system, with semantics varying based on the creative type."
  
  - name: "reference_share_id"
    type: "integer"
    description: ""
  
  - name: "review"
    type: "object"
    description: "Details about the review status of the creative."
    subattributes:
      - name: "review_status"
        type: "string"
        description: |
          The review status of the Ad entity. Possible values are:

          - `PENDING` - Ad entity is pending review and not serving.
          - `APPROVED` - Ad entity is approved for serving.
          - `REJECTED` - Ad entity is rejected.
          - `PREAPPROVED` - Ad entity has been preapproved; it's ready for serving but still needs further review.
          - `AUTO_APPROVED` - Ad entity has been auto approved by content model.
          - `NEEDS_REVIEW` - Ad entity has been rejected by content model or policy checker or returned by fallback case that auto approval didn't make any decision.
          - `AUTO_REJECTED` - Ad entity has been auto rejected by content model.
  
  - name: "status"
    type: "string"
    description: |
      The status of the creative. Possible values are:

      - `ACTIVE` - Creative creation is complete and creative is available for review and serve.
      - `PAUSED` - Creative creation is complete and creative is current, but should temporarily not be served.
      - `DRAFT` - Creative creation is incomplete and may still be edited.
      - `ARCHIVED` - Creative creation is complete, but creative should not be served and should be separated from non-archived creatives in any UI.
      - `CANCELED` - Creative is permanently canceled.

      Creative status is set independently from parent entity status, but parent entity status overrides creative status in effect. For example: Parent entity status may be `PAUSED` while creative status is `ACTIVE`, in which case creative is in effect `PAUSED`, and not served.
  
  - name: "type"
    type: "string"
    description: |
      The type of creative. Possible values are:

      - `TEXT_AD` - Text with Sponsored Link to landing page on your site.
      - `SPONSORED_STATUS_UPDATE` - Sponsored status update from a profile page.
      - `SPONSORED_INMAILS` - Sponsored InMails.
      - `SPONSORED_VIDEO` - Sponsored videos.
      - `SPONSORED_UPDATE_CAROUSEL` - Sponsored Carousels
      - `FOLLOW_COMPANY_V2` - Dynamic Follow Ad
      - `SPOTLIGHT_V2` - Dynamic Spotlight Ad
      - `JOBS_V2` - Dynamic Job Ad
  
  - name: "variables"
    type: "object"
    description: "Variables for rendering the creative."
    subattributes:
      - name: "click_uri"
        type: "string"
        description: "Required when creative type is `TEXT_AD`."
      - name: "type"
        type: "string"
        description: ""
      - name: "values"
        type: "null"
        description: ""
  
  - name: "version"
    type: "object"
    description: ""
    subattributes:
      - name: "version_tag"
        type: "string"
        description: ""
---