---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-table-schema/
## FOR INSTRUCTIONS & REFERENCE INFO


tap: "heap"
version: "1.0" 

name: "[event_type]"
doc-link: https://docs.heapanalytics.com/docs/heap-sql-retroactive-s3-specification
description: |
  For every event type defined in {{ integration.display_name }}, a table will display in the Stitch app. The name of the table will be the event name, which {{ integration.display_name }} will first strip the non-alphanumeric characters from. For example: The table name for `Sign Up - Click Link` will be transformed into `sign_up_click_link` by {{ integration.display_name }}.

  **Note**: Custom attributes are supported for this table. As {{ integration.display_name }} schemas are dynamic, Stitch's `{{ table.name }}` documentation will only list the non-custom attributes outlined in {{ integration.display_name }}'s documentation.

replication-method: "Key-based Incremental"

replication-key:
  name: "[See Replication](#incremental-replication-for-heap)"

attributes:
  - name: "event_id"
    type: "string"
    primary-key: true
    description: "The event ID."
    foreign-key-id: "event-id"

  - name: "user_id"
    type: "integer"
    description: "The ID of the associated user."
    foreign-key-id: "user-id"

  - name: "session_id"
    type: "integer"
    description: "The ID of the associated session."
    foreign-key-id: "session-id"

  - name: "Custom Attributes"
    type: 
    description: "Any custom attributes applied to this event type model in {{ integration.display_name }}."

  - name: "time"
    type: "string"
    description: "The UTC timestamp when the event happened."

  - name: "session_time"
    type: "string"
    description: "The timestamp when the session started. **Note**: According to {{ integration.display_name }}, this field is primarily used for {{ integration.display_name }}'s internal use and shouldn't be relied on for analysis."

  - name: "type"
    type: "string"
    description: |
      For web auto-tracked events, can be any of view page, click, submit, change, with push state events registered as view page events.

      For iOS auto-tracked events, can be touch, edit field, or a gesture recognizer you've defined.

      For custom events, this will be the custom event name.

  - name: "library"
    type: "string"
    description: |
      The version of the heap library which initiated the session. Possible values are:

      - `web`
      - `iOS`

  - name: "platform"
    type: "string"
    description: "The user's operating system."

  - name: "device_type"
    type: "string"
    description: |
      The user's device type. Possible values are:

      - `Mobile`
      - `Tablet`
      - `Desktop`

  - name: "country"
    type: "string"
    description: "The country in which the user session occurred, based on IP."

  - name: "region"
    type: "string"
    description: "The region in which the user session occurred, based on IP."

  - name: "city"
    type: "string"
    description: "The city in which the user session occurred, based on IP."

  - name: "IP"
    type: "string"
    description: "The IP address for the session."

  - name: "referrer"
    type: "string"
    description: "**Applicable only to `library: Web`.** The URL that linked to the site and initiated the session. If the user navigated directly to the site or referral headers were stripped, this value will be `direct`."

  - name: "landing_page"
    type: "string"
    description: "**Applicable only to `library: Web`.** The URL of the first pageview of the session."

  - name: "browser"
    type: "string"
    description: "**Applicable only to `library: Web`.** The user's browser."

  - name: "search_keyword"
    type: "string"
    description: "**Applicable only to `library: Web`.** The search term that brought the user to the site."

  - name: "utm_source"
    type: "string"
    description: "**Applicable only to `library: Web`**. The GA-based `utm_source` tag associated with the session's initial pageview."

  - name: "utm_campaign"
    type: "string"
    description: "**Applicable only to `library: Web`**. The GA-based `utm_campaign` tag associated with the session's initial pageview."

  - name: "utm_medium"
    type: "string"
    description: "**Applicable only to `library: Web`**. The GA-based `utm_medium` tag associated with the session's initial pageview."

  - name: "utm_term"
    type: "string"
    description: "**Applicable only to `library: Web`**. The GA-based `utm_term` tag associated with the session's initial pageview."

  - name: "utm_content"
    type: "string"
    description: "**Applicable only to `library: Web`**.The GA-based `utm_content` tag associated with the session's initial pageview."

  - name: "path"
    type: "string"
    description: "**Applicable only to `library: Web`.** The path of the pageview."

  - name: "query"
    type: "string"
    description: "**Applicable only to `library: Web`.** The query parameters associated with the pageview."

  - name: "hash"
    type: "string"
    description: "**Applicable only to `library: Web`.** The hash parameters associated with the pageview."

  - name: "title"
    type: "string"
    description: "**Applicable only to `library: Web`.** The title of the current page."

  - name: "href"
    type: "string"
    description: "The `href` property of link."

  - name: "device"
    type: "string"
    description: "**Applicable only to `library: iOS`.** The user's device model."

  - name: "carrier"
    type: "string"
    description: "**Applicable only to `library: iOS`.** The user's mobile phone carrier."

  - name: "app_name"
    type: "string"
    description: "**Applicable only to `library: iOS`.** The current name of the iOS app."

  - name: "app_version"
    type: "string"
    description: "**Applicable only to `library: iOS`.** The current version of the iOS app."

  - name: "action_method"
    type: "string"
    description: "The name of the action method triggered by this event. For example: `loginButtonWasPressed`"

  - name: "view_controller"
    type: "string"
    description: "**Applicable only to `library: iOS`.** The name of the current view controller."

  - name: "screen_ally_id"
    type: "string"
    description: "**Applicable only to `library: iOS`.** The accessibility identifier for the current view controller."

  - name: "screen_ally_label"
    type: "string"
    description: "**Applicable only to `library: iOS`.** The accessibility label for the current view controller."

  - name: "target_view_class"
    type: "string"
    description: "The underlying class name of an iOS action's target."

  - name: "target_view_name"
    type: "string"
    description: "The instance variable name of an iOS action's target."

  - name: "target_ally_id"
    type: "string"
    description: "**Applicable only to `library: iOS`.** The name of an iOS action's target."

  - name: "target_ally_label"
    type: "string"
    description: "**Applicable only to `library: iOS`.** The label of an iOS action's target."

  - name: "target_text"
    type: "string"
    description: "The button text of the event target."
---