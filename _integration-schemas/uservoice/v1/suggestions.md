---
tap: "uservoice"
version: "1.0"

name: "suggestions"
doc-link: https://developer.uservoice.com/docs/api/v2/reference/#/Suggestions
singer-schema: https://github.com/singer-io/tap-uservoice/blob/master/tap_uservoice/streams/suggestions.py
description: |
  The `{{ table.name }}` table contains info about suggestions, or requested changes to your product. Suggestions can be created by your end users, your product team, or other people from your company.

  Each suggestion is linked to a forum, where it can be visible publicly or to authorized users.

replication-method: "Key-based Incremental"

api-method:
  name: List suggestions
  doc-link: https://developer.uservoice.com/docs/api/v2/reference/#list-suggestions

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The suggestion ID."
    foreign-key-id: "suggestion-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the suggestion was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the suggestion was created."

  - name: "admin_url"
    type: "string"
    description: "The URL of the suggestion in the admin console for admins."

  - name: "approved_at"
    type: "date-time"
    description: "The time the suggestion was approved."

  - name: "average_engagement"
    type: "number"
    description: "The average engagement rate."

  - name: "body"
    type: "string"
    description: "The description of the suggestion."

  - name: "body_mime_type"
    type: "string"
    description: "The MIME type of the suggestion `body`."

  - name: "channel"
    type: "string"
    description: "The channel used to create the suggestion."

  - name: "closed_at"
    type: "date-time"
    description: "The time the suggestion was closed."

  - name: "comments_count"
    type: "integer"
    description: "The total number of comments associated with the suggestion."

  - name: "creator_browser"
    type: "string"
    description: "The browser the suggestion creator was using when creating the suggestion."

  - name: "creator_browser_version"
    type: "string"
    description: "The browser version the suggestion creator was using when creating the suggestion."

  - name: "creator_mobile"
    type: "boolean"
    description: "If `true`, the suggestion creator created the suggestion using a mobile device."

  - name: "creator_os"
    type: "string"
    description: "The operating system the suggestion creator was using when creating the suggestion."

  - name: "creator_referrer"
    type: "string"
    description: "The referrer URL for the suggestion."

  - name: "creator_user_agent"
    type: "string"
    description: "The user agent the suggestion creator was using when creating the suggestion."

  - name: "engagement_trend"
    type: "number"
    description: ""

  - name: "first_support_at"
    type: "date-time"
    description: "The time the suggestion first required support."

  - name: "inappropriate_flags_count"
    type: "integer"
    description: "The total number times end users have flagged the suggestion as inappropriate."

  - name: "is_blocker"
    type: "boolean"
    description: "If `true`, a sales opportunity associated with the suggestion considers this to be a blocker."

  - name: "notes_count"
    type: "integer"
    description: "The total number of internal (admin) notes associated with the suggestion."

  - name: "portal_url"
    type: "string"
    description: "The URL of the suggestion in the web portal (forum) for end users."

  - name: "recent_engagement"
    type: "integer"
    description: "The total number of new supporters, requests, and comments for the suggestion in the past 30 days."

  - name: "requests_count"
    type: "integer"
    description: "The total number of requests associated with the suggestion."

  - name: "satisfaction_detractor_count"
    type: "integer"
    description: "The total number supporters on the suggestion who are also NPS detractors."

  - name: "satisfaction_neutral_count"
    type: "integer"
    description: "The total number supporters on the suggestion who are also NPS passives."

  - name: "satisfaction_promoter_count"
    type: "integer"
    description: "The total number supporters on the suggestion who are also NPS promoters."

  - name: "state"
    type: "string"
    description: |
      The state of the suggestion. Possible values are:

      - `approved` - The suggestion went to moderation and was approved by an admin
      - `published` - The suggestion didn't go through moderation and is on the web portal

  - name: "supporter_mrr"
    type: "number"
    description: "The sum of supporter MRR for the accounts that have supporters associated with the suggestion."

  - name: "supporter_satisfaction_score"
    type: "number"
    description: "The average NPS satisfaction score for all supporters associated with the suggestion."

  - name: "supporters_count"
    type: "integer"
    description: "The total number of supporters associated with the suggestion."

  - name: "supporting_accounts_count"
    type: "integer"
    description: "The total number of supporting accounts associated with the suggestion."

  - name: "title"
    type: "string"
    description: "The suggestion title."

  - name: "votes_count"
    type: "integer"
    description: "The total number of votes associated with the suggestion."

  - name: "links"
    type: "object"
    description: ""
    object-attributes: 
      - name: "category"
        type: "integer"
        description: "The category associated with the suggestion."
        foreign-key-id: "category-id"

      - name: "created_by"
        type: "integer"
        description: "The ID of the user who created the suggestion."
        foreign-key-id: "user-id"

      - name: "forum"
        type: "integer"
        description: "The ID of the forum associated with the suggestion."
        foreign-key-id: "forum-id"

      - name: "labels"
        type: "array"
        description: "The IDs of the labels associated with the suggestion."
        array-attributes:
          - name: "value"
            type: "integer"
            description: "The ID of the label associated with the suggestion."
            foreign-key-id: "label-id"

      - name: "last_status_update"
        type: "integer"
        description: "The ID of the last status update event."
        foreign-key-id: "status-update-id"

      - name: "parent_suggestion"
        type: "integer"
        description: "If the suggestion is merged into another suggestion, this will be the ID of the suggestion it is merged into."
        foreign-key-id: "suggestion-id"

      - name: "parent_suggestions"
        type: "array"
        description: ""

      - name: "status"
        type: "integer"
        description: "The ID of the status associated with the suggestion."
        foreign-key-id: "status-id"

      - name: "ticket"
        type: "integer"
        description: "The ID of the ticket associated with the suggestion, if the suggestion is converted to a ticket."
---