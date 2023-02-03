---
tap: "linkedin-ads"
version: "2"
key: "creatives"

name: "creatives"
doc-link: "https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads/account-structure/create-and-manage-creatives?view=li-lms-2023-01&tabs=http#search-for-creatives"
singer-schema: "https://github.com/singer-io/tap-linkedin-ads/tree/master/tap_linkedin_ads/schemas/creatives.json"
description: "The Creatives API contains all the data and information for visually rendering an ad."
​
replication-method: "Key-based Incremental"
​
attributes:
  - name: "account"
    type: "string"
    description: "URN identifying the advertising account associated with the creative."

  - name: "account_id"
    type: "integer"
    description: "ID identifying the advertising account associated with the creative."

  - name: "campaign"
    type: "string"
    description: "URN identifying the campaign associated with the creative"
    
  - name: "campaign_id"
    type: "integer"
    description: "ID identifying the campaign associated with the creative"

  - name: "content"
    type: "object"
    description: "Content sponsored in the creative."
    subattributes:
    - name: "reference"
      type: "string"
      description: "A reference must be a adInMailContent{id}, share{id}, or ugcPost{id}."

    - name: "text_ad"
      type: "object"
      description: "Text ads include a headline, brief text, and an image."
      subattributes:
      - name: "headline"
        type: "string"
        description: "The main message seen by the target audience on the ad. Use up to 25 characters, including spaces"

      - name: "description"
        type: "string"
        description: "The description that provides more information about the ad. Use up to 75 characters, including spaces."

      - name: "landing_page"
        type: "string"
        description: "The URL where the member should be redirected to, on clicking the text ad."

  - name: "created_at"
    type: "string"
    format: "date-time"
    description: "Creation time"

  - name: "created_by"
    type: "string"
    description: "Entity (e.g., a person URN) that developed the creative"

  - name: "id"
    type: "string"
    description: "Unique ID for a creative (e.g.,SponsoredCreativeUrn)."
    primary-key: true

  - name: "intended_status"
    type: "string"
    description: "Creative user intended status."

  - name: "is_serving"
    type: "boolean"
    description: "This indicates whether the creative is currently being served or not."

  - name: "is_test"
    type: "boolean"
    description: "True returns creatives only under test accounts. False returns creatives only under non-test accounts."

  - name: "last_modified_at"
    type: "string"
    format: "date-time"
    description: "Time at which the creative was last modified."
    replication-key: true

  - name: "last_modified_by"
    type: "string"
    description: "The entity (e.g., person URN) who modified the creative"

  - name: "serving_hold_reasons"
    type: "array"
    description: "Array that contains all the reasons why the creative is not serving."
    subattributes:
    - name: "items"
      type: "string"
      description: "Contains different reasons."
---