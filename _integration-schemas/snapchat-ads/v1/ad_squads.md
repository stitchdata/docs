---
tap: "snapchat-ads"
version: "1"
key: ""

name: "ad_squads"
doc-link: https://developers.snapchat.com/api/docs/#get-all-ad-squads-under-an-ad-account
singer-schema: https://github.com/singer-io/tap-snapchat-ads/blob/master/tap_snapchat_ads/schemas/ad_squads.json
description: "This stream retrieves all ad squads within a specified ad account."

replication-method: "Key-based Incremental"

table-key-properties: "id"
valid-replication-keys: "updated_at"

attributes:
  - name: "ad_account_id"
    type: "string"
    description: "AD Account ID"

  - name: "auto_bid"
    type: "boolean"
    description: "Allow Snapchat to automatically set the bid to recommended amount"

  - name: "bid_micro"
    type: "integer"
    description: "Max Bid (micro-currency)"

  - name: "bid_strategy"
    type: "string"
    description: "Bidding strategy for this Ad Squad. Example: AUTO_BID, LOWEST_COST_WITH_MAX_BID, MIN_ROAS, TARGET_COST"

  - name: "billing_event"
    type: "string"
    description: "Billing Event. Example: IMPRESSION"

  - name: "campaign_id"
    type: "string"
    description: "Campaign ID"

  - name: "cap_and_exclusion_config"
    type: "object"
    description: "The frequency cap and exclusion spec"
    subattributes:

  - name: "created_at"
    type: "date-time"
    description: "Date and Time at which AD Squad was created"

  - name: "daily_budget_micro"
    type: "integer"
    description: "Daily Budget (micro-currency)"

  - name: "delivery_constraint"
    type: "string"
    description: "Type of delivery"

  - name: "end_time"
    type: "date-time"
    description: "End time"

  - name: "id"
    primary-key: true
    type: "string"
    description: "AD Squad ID"

  - name: "impression_goal"
    type: "string"
    description: "Reach goal as specified in the Forecasting request"

  - name: "lifetime_budget_micro"
    type: "integer"
    description: "Lifetime budget (micro-currency)"

  - name: "name"
    type: "string"
    description: "AD Squad name"

  - name: "optimization_goal"
    type: "string"
    description: "Optimization Goal. Example: MPRESSIONS, SWIPES, APP_INSTALLS, VIDEO_VIEWS, VIDEO_VIEWS_15_SEC, USES, STORY_OPENS, PIXEL_PAGE_VIEW, PIXEL_ADD_TO_CART, PIXEL_PURCHASE, PIXEL_SIGNUP, APP_ADD_TO_CART, APP_PURCHASE, APP_SIGNUP"

  - name: "pacing_type"
    type: "string"
    description: "Type of pacing. Example: STANDARD (default), ACCELERATED"

  - name: "pixel_id"
    type: "string"
    description: "Pixel to be associated with the Ad Squad"

  - name: "placement"
    type: "string"
    description: ""

  - name: "placement_v2"
    type: "object"
    description: "Placement, Json object containing advanced placement"
    subattributes:
    - name: "config"
      type: "string"
      description: "Configuration for placement"

    - name: "platforms"
      type: "string"
      description: "The platform to place the ads"

    - name: "inclusion"
      type: "object"
      description: "Details about the content types to be included"
      subattributes:
      - name: "content_types"
        type: "array, null"
        description: "List of possible content types"
        subattributes:
        - type: "string"
          description: "Content Type"


    - name: "exclusion"
      type: "object"
      description: "Details about the content types to be excluded"
      subattributes:
      - name: "content_types"
        type: "array, null"
        description: "List of possible content types"
        subattributes:
        - type: "string"
          description: "Content Type"



  - name: "product_properties"
    type: "object"
    description: "Product Properties to be associated with the Ad Squad"
    subattributes:
      - name: "product_set_id"
      type: "object"
      description: "The Product Set ID to be associated with the Ad Squad"
      subattributes:
        - name: "catalog_id"
        type: "string"
        description: "Catalog ID"

    - name: "catalog_vertical"
      type: "string"
      description: "Catalog vertical, automatically set by the Catalog"

  - name: "reach_and_frequency_micro"
    type: "integer"
    description: "reach and frequency budget (micro-currency)"

  - name: "reach_and_frequency_status"
    type: "string"
    description: "Status of the reach and frequency booking"

  - name: "reach_goal"
    type: "string"
    description: "Reach goal as specified in the Forecasting request"

  - name: "start_time"
    type: "date-time"
    description: "Start Time"

  - name: "status"
    type: "string"
    description: "Ad Squad status. Example: ACTIVE, PAUSED"

  - name: "target_bid"
    type: "boolean"
    description: "Allows Snapchat to adjust the bid aiming to keep your average CPA at or below the amount set by the ad set end date"

  - name: "targeting"
    type: "object"
    description: "Targeting spec"
    subattributes:
    - name: "regulated_content"
      type: "boolean"
      description: ""

    - name: "enable_targeting_expansion"
      type: "boolean"
      description: ""

    - name: "demographics"
      type: "array, null"
      description: ""
      subattributes:
      - name: "items"
        type: "object"
        description: ""

    - name: "devices"
      type: "array, null"
      description: ""
      subattributes:
      - name: "items"
        type: "object"
        description: ""

    - name: "geos"
      type: "array, null"
      description: ""
      subattributes:
      - name: "items"
        type: "object"
        description: ""

    - name: "interests"
      type: "array, null"
      description: ""
      subattributes:
      - name: "items"
        type: "object"
        description: ""

    - name: "segments"
      type: "array, null"
      description: ""
      subattributes:
      - name: "items"
        type: ""
        description: ""


  - name: "targeting_reach_status"
    type: "string"
    description: "Status of target reach. Example: VALID, INVALID"

  - name: "type"
    type: "string"
    description: "AD Squad type"

  - name: "updated_at"
    type: "date-time"
    description: "Date and Time at which AD squad was last updated"


